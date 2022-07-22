import logging

from tgbot.models.user import User


class UserService:
    def __init__(self):
        pass

    def get_all(self):
        user = User.select().get()
        logging.info(user.__data__)
