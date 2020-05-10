""" Module-example of using Situation ADT """
from read_save_input import UsersSituation

USER_SITUATION = UsersSituation()
USER_SITUATION.read_users_situation("result.xlsx")
USER_SITUATION.history_user_write()
print(USER_SITUATION.translate_situation())
