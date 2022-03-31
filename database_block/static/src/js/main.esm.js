/** @odoo-module **/
import { ActionContainer } from "@web/webclient/actions/action_container";
import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from "web.utils";
import { session } from "@web/session";

patch(ActionContainer.prototype, "database_block.action_container", {
    mounted() {
        this._super.apply(this, arguments);
        if (this.databaseBlockMessage) {
            const blockMessage = this.env.qweb.renderToString("database_block.BlockMessage", {
                "message": this.databaseBlockMessage,
            });
            $(".o_action_manager").block({message: blockMessage});
        }
    },

    get databaseBlockMessage() {
        if (!session.database_block_is_warning && session.database_block_message) {
            return session.database_block_message;
        }
        return null;
    },
});

patch(NavBar.prototype, "database_block.navbar", {
    get session() {
        return session;
    },
});
