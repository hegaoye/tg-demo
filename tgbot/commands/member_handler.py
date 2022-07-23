import logging

from telegram import Update
from telegram.ext import CallbackContext

from tgbot.api.user_api_client import UserApiClient
from tgbot.commands.base_handler import BaseHandler


class MemberJoinOrLeftGroupHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.user_api_client = UserApiClient()

    async def handle(self, update: Update, context: CallbackContext):
        """
        用户异动信息
        加群，退群等
        """
        logging.info("MemberJoinOrLeftGroupHandler:%s", update.effective_user.id)
        logging.info("MemberJoinOrLeftGroupHandler:%s", update.effective_user.username)

        bot = context.bot
        bot_id = bot.id
        chat_id = update.effective_chat.id

        user = update.message.left_chat_member
        if user:
            # 退群
            self.user_api_client.left_group(chat_id, bot_id, user.id)

        new_users = update.message.new_chat_members
        if new_users:
            for new_user in new_users:
                # 加群
                reply_text = self.user_api_client.join_group(chat_id, bot_id, new_user.id, new_user.username,
                                                             new_user.first_name)
                await context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)
