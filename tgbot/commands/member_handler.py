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
                await update.message.reply_text(self.new_user_join_group(new_user))


    def new_user_join_group(self, user) -> str:
        logging.info("ChatJoinRequestHandler 加入群:-%s -%s", user.username, user.id)

        reply_text = """
        欢迎 @{at} 加入
        彩票规则
        1. 每2分钟开奖一次, 开奖前20秒封盘，停止投注

        2. 开奖号取币安的BTC/USDT价格双数分钟的开盘价，取值到小数点后一位， 例如币安BTC/USDT的价格是49617.8，则开奖号码的算法：4+9+6+1+7+8=35，取个位数5为开奖号码。
        核对开奖结果：https://www.binance.com/zh-CN/trade/BTC_USDT

        3. 0,1,2,3,4为小，5,6,7,8,9为大；0,2,4,6,8为双，1,3,5,7,9为单

        4. 押大小单双赔率 1.96, 押号码赔率 9.8

        5. 庄家盈利需要扣除0.5%的服务费

        初级群：群累计投注额小于100万的按0.5%算系统佣金
        中级群：群累计投注额100万——1000万的按0.4%算系统佣金
        高级群：群累计投注额1000万——1个亿的按0.3%算系统佣金
        黄金群：群累计投注额1个亿——10个亿的按0.2%算系统佣金
        钻石群：群累计投注额10个亿以上的按0.1%算系统佣金

        6. 大小限红 10 ~ 1000

        7. 单双限红10 ~ 1000

        8. 号码限红10 ~ 500

        9. 单场最大赔付金额10000
                """
        return reply_text.format(at=user.username)

    def user_left_group(self, user):
        logging.info("ChatJoinRequestHandler 离开群：-%s -%s", user.username, user.id)
