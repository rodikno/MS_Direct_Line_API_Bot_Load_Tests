# python-botframework-directline
Example Python for calling Bot Framework via the DirectLine API (v3)

For further details refer to the API documentation here: 
[http://dev.botframework.com](https://docs.microsoft.com/en-us/bot-framework/rest-api/bot-framework-rest-direct-line-3-0-concepts
)
1. Register your bot on the dev.botframework.com portal
2. Enable the DirectLine Channel and copy the secret key
3. Put the secret key to `/config/config.py` as `DIRECT_LINE_API_SECRET` value
4. Run the `bot_connection.py`

Usage example

```
bot = DirectLineAPI(config.DIRECT_LINE_API_SECRET)
bot.send_message("I have Outlook problem")
botresponse = bot.get_message()
for message in botresponse:
    print(message)
```

# Running Locust.io Load testing framework
To run the service: 
`locust --host=http://127.0.0.1:5002`
Additional docs for Locust.io are placed here https://docs.locust.io/en/latest/api.html

Locust will run locally after it's started, to reach a Web-interface go to: 
`http://127.0.0.1:8089/`
