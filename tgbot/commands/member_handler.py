import logging

from telegram import Update
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf


class MemberJoinOrLeftGroupHandler:
    def __init__(self):
        self.sys_conf = SysConf()

    async def handle(self, update: Update, context: CallbackContext):
        logging.info("ChatJoinRequestHandler:%s", update.effective_user.id)
        logging.info("ChatJoinRequestHandler:%s", update.effective_user.username)

        user = update.message.left_chat_member
        if user:
            self.user_left_group(user)

        new_users = update.message.new_chat_members
        if new_users:
            for new_user in new_users:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=self.new_user_join_group(new_user),
                )

    def new_user_join_group(self, user) -> str:
        logging.info("ChatJoinRequestHandler 加入群:-%s -%s -%s -%s", user.username, user.id, user.first_name,
                     user.language_code)

        reply_text = """
        欢迎 @{at} 加入
        快速开始教程
1. 每2分钟开奖一次, 开奖前20秒封盘，停止投注
2. 开奖号取币安的BTC/USDT价格双数分钟的开盘价，取值到小数点后一位，例如币安BTC/USDT的价格是49617.8，则开奖号码的算法：4+9+6+1+7+8=35，取个位数5为开奖号码
3. 本系统专业为博彩双方服务，不参与任何形式博彩，无需担心庄家输了赖帐，请放心存款
4. 操作命令：
/start 开启彩票
/stop 关闭彩票
/mini H5小程序 
/help 查看帮助
/doc 操作指南
                """
        return reply_text.format(at=user.username)

    def user_left_group(self, user):
        logging.info("ChatJoinRequestHandler 离开群：-%s -%s", user.username, user.id)
