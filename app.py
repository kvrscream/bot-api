from flask import Flask
from flask import request
import json
from controllers.botController import training_bot, get_response

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"

@app.route('/training', methods=['POST'])
def training():
    body = request.get_json(force=True)
    intent = body['intent']
    #Intent sempre vai vir um name com o nome da inteção e um content com exemplos
    training_bot(intent['content'])
    return json.dumps({
        "message": "Treinamento concluído",
        "intencao": intent["name"]
    })

@app.route('/send', methods=['POST'])
def send_message():
    body = request.get_json(force=True)
    answer = get_response(body['message'])
    print(answer)
    return json.dumps({"answer": str(answer)}, ensure_ascii=False).encode('utf8')

#app.run()