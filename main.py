from json import dumps
from flask import Flask, request, Response
from flask_restful import Resource, Api, reqparse
from bot_connection import BotTestSession

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('message')

class QnABotConversation(Resource):
    def post(self):
        args = parser.parse_args()
        original_message = args['message']
        bot_session = BotTestSession()
        res = bot_session.ask_bot_for(original_message)
        json_res = {"original_message": original_message, "messages": res, "length": str(len(res)) }
        return Response(dumps(json_res), mimetype='application/json')

api.add_resource(QnABotConversation, '/ask_bot')

if __name__ == '__main__':
    app.run()