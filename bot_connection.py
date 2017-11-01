from direct_line_API_v3_connector.connector import DirectLineAPI
from config import config
from config.config import *


class BotTestSession(object):
    def ask_bot_for(self, message):
        bot = DirectLineAPI(DIRECT_LINE_API_SECRET)
        bot.send_message(message)
        botresponse = bot.get_message()
        return botresponse


# session = BotTestSession()
# resp = session.ask_bot_for('Outlook problem')
# print(resp)
