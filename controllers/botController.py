from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

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
    return bot_name

def training_bot(intent, bot):
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