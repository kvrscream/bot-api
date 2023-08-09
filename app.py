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
    return json.dumps(body)


#app.run()