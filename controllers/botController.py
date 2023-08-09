from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('thor',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Desculpe não consegui entender. Tente reformular sua pergunta.',
            'maximum_similarity_threshold': 0.60
        }
    ]
)

def training_bot(intent):
    trainer = ListTrainer(chatbot)
    trainer.train(intent)
    return True

def get_response(client_message):
    response = chatbot.get_response(client_message)
    return response