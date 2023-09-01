from flask import Flask, request, Response, jsonify
import json
from controllers.botController import training_bot, get_response, create_bot, list_bots, list_intents
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Index"

@app.route('/create', methods=['POST'])
def create():
    body = request.get_json(force=True)
    bot_name = body['name']
    chatbot = create_bot(bot_name)

    return Response(json.dumps({
        'message': 'Chatbot cadastrado com sucesso',
        'name': bot_name,
        "chatbot": chatbot
    }, ensure_ascii=False).encode('utf8'), mimetype='application/json')

@app.route('/training', methods=['POST'])
def training():
    body = request.get_json(force=True)
    intent = body['intent']
    bot = body['bot']
    training_bot(intent['name'], intent['content'], bot)
    return Response(json.dumps({
        "message": "Treinamento concluído",
        "intencao": intent["name"]
    }), mimetype='application/json')

@app.route('/send', methods=['POST'])
def send_message():
    body = request.get_json(force=True)
    answer = get_response(body['message'], body['bot'])
    return Response(json.dumps({"answer": str(answer)}, ensure_ascii=False).encode('utf8'), mimetype='application/json')

@app.route('/bots', methods=['GET'])
def bots():
    bots = list_bots()
    for bot in bots:
        bot['_id'] = str(bot['_id'])
        bot['created'] = str(bot['created'])
    return Response(json.dumps(bots), mimetype='application/json')

@app.route('/intents/<clientId>', methods=["GET"])
def intents(clientId):
    intents = list_intents(clientId)
    for intent in intents:
        intent['_id'] = str(intent['_id'])
        intent['clientId'] = str(intent['clientId'])
    return Response(json.dumps(intents, ensure_ascii=False).encode('utf8'), mimetype='application/json')

