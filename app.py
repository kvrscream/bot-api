from flask import Flask
from flask import request
import json
from controllers.botController import training_bot, get_response, create_bot, list_bots, list_intents

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"

@app.route('/create', methods=['POST'])
def create():
    body = request.get_json(force=True)
    bot_name = body['name']
    chatbot = create_bot(bot_name)

    return json.dumps({
        'message': 'Chatbot cadastrado com sucesso',
        'name': bot_name,
        "chatbot": chatbot
    }, ensure_ascii=False).encode('utf8')

@app.route('/training', methods=['POST'])
def training():
    body = request.get_json(force=True)
    intent = body['intent']
    bot = body['bot']
    training_bot(intent['name'], intent['content'], bot)
    return json.dumps({
        "message": "Treinamento concluído",
        "intencao": intent["name"]
    })

@app.route('/send', methods=['POST'])
def send_message():
    body = request.get_json(force=True)
    answer = get_response(body['message'], body['bot'])
    return json.dumps({"answer": str(answer)}, ensure_ascii=False).encode('utf8')

@app.route('/bots', methods=['GET'])
def bots():
    bots = list_bots()
    return json.dumps({"clients": str(bots)}, ensure_ascii=False).encode('utf8')


@app.route('/intents/<clientId>', methods=["GET"])
def intents(clientId):
    intents = list_intents(clientId)
    print(intents)
    return json.dumps({"intents": str(intents)}, ensure_ascii=False).encode('utf8')

