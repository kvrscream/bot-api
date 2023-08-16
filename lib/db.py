from pymongo import MongoClient

def connect():
  try:
    conn = MongoClient('mongodb+srv://botelho:QaTOAWPJpPn48L8Z@cluster0.sbo5kcd.mongodb.net/?retryWrites=true&w=majority')
    return conn
  except:
    print('erro ao tentar conectar no mongo')