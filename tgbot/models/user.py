# coding=utf-8
from peewee import PrimaryKeyField, IntegerField, CharField, DateTimeField, DoubleField

from tgbot.models.base_model import BaseModel


class User(BaseModel):
    """
      `id` varchar(64) NOT NULL COMMENT 'id',
      `group_id` varchar(64) DEFAULT NULL COMMENT '群id',
      `tg_user_id` varchar(64) NOT NULL COMMENT 'tg用户id，来自tg',
      `tg_username` varchar(64) NOT NULL COMMENT 'tg下用户名',
      `username` varchar(32) NOT NULL COMMENT '本系统生成的用户名，默认和tg保持一致',
      `password` varchar(32) DEFAULT NULL COMMENT '密码，默认和用户名一致',
      `google_code` varchar(32) DEFAULT NULL COMMENT '谷歌口令',
      `percent` int(10) DEFAULT NULL COMMENT '占成比例，如:10% 存储为10',
      `status` varchar(16) DEFAULT NULL COMMENT '状态:可投注 Enable,禁止投注 Disable，庄审核 Verify_Banker',
      `type` varchar(16) DEFAULT NULL COMMENT '类型:试玩 Demo,玩家 Player,庄家 Banker',
      `is_owner` varchar(4) DEFAULT NULL COMMENT '是否群主：是 Y,否 N',
      `is_admin` varchar(4) DEFAULT NULL COMMENT '是否管理员：是 Y，否 N',
      `usdt_balance` double DEFAULT NULL COMMENT 'usdt 余额',
      `usdt_address` varchar(255) DEFAULT NULL COMMENT 'usdt 地址',
      `bet_total_money` bigint(19) DEFAULT NULL COMMENT '投注总额',
      `bet_win_money` bigint(19) DEFAULT NULL COMMENT '投注盈利',
      `bet_lost_money` bigint(19) DEFAULT NULL COMMENT '投注亏损总额',
      `summary` varchar(128) DEFAULT NULL COMMENT '说明',
      `create_time` datetime DEFAULT NULL COMMENT '创建时间',
      `update_time` datetime DEFAULT NULL COMMENT '更新时间',
    """
    id = PrimaryKeyField()
    group_id = CharField()
    tg_user_id = CharField()
    tg_username = CharField()
    username = CharField()
    password = CharField()
    google_code = CharField()
    percent = IntegerField()
    status = CharField()
    type = CharField()
    is_owner = CharField()
    is_admin = CharField()
    usdt_balance = DoubleField()
    usdt_address = CharField()
    bet_total_money = IntegerField()
    bet_win_money = IntegerField()
    bet_lost_money = IntegerField()
    summary = CharField()
    create_time = DateTimeField()
    update_time = DateTimeField()
