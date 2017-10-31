from direct_line_API_v3_connector.connector import DirectLineAPI
from config import config

bot = DirectLineAPI(config.DIRECT_LINE_API_SECRET)
bot.send_message("I have Outlook problem")
botresponse = bot.get_message()
for message in botresponse:
    print(message)