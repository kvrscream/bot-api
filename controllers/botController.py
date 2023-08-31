from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from lib.db import connect
from datetime import datetime
from bson.objectid import ObjectId



def create_bot(bot_name):
    chatbot = ChatBot(bot_name,
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb+srv://botelho:QaTOAWPJpPn48L8Z@cluster0.sbo5kcd.mongodb.net/%s?retryWrites=true&w=majority' % bot_name,
    logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe não consegui entender. Tente reformular sua mensagem.',
            'maximum_similarity_threshold': 0.60
        }]
    )

    db = connect()
    db["homolog"].clients.insert_one({
        "name": bot_name,
        "created": datetime.now()
    })
    db.close()


    return bot_name

def training_bot(name, intent, bot):
    chatbot = ChatBot(bot,
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb+srv://botelho:QaTOAWPJpPn48L8Z@cluster0.sbo5kcd.mongodb.net/%s?retryWrites=true&w=majority' % bot,
    logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe não consegui entender. Tente reformular sua mensagem.',
            'maximum_similarity_threshold': 0.60
        }]
    )
    trainer = ListTrainer(chatbot)
    trainer.train(intent)

    db = connect()
    client = db['homolog'].clients.find_one({"name": bot})
    data = db['homolog'].intents.insert_one({
        "name": name,
        "intents": intent,
        "clientId": client['_id']
    })
    print(data)
    db.close()

    return True

def get_response(client_message, bot):
    chatbot = ChatBot(bot,
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database_uri='mongodb+srv://botelho:QaTOAWPJpPn48L8Z@cluster0.sbo5kcd.mongodb.net/%s?retryWrites=true&w=majority' % bot,
    logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe não consegui entender. Tente reformular sua mensagem.',
            'maximum_similarity_threshold': 0.60
        }]
    )
    response = chatbot.get_response(client_message)
    return response


def list_bots():
    db = connect()
    bots = db['homolog']['clients'].find()
    #db.close()
    return list(bots)

def list_intents(client_id):
    db = connect()
    object_id_to_find = ObjectId(str(client_id))
    intents = db['homolog'].intents.find({"clientId":object_id_to_find })
    #db.close()
    return list(intents)