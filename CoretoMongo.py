from Game import Poker
from Cards import Deck
from Cards import Card
from itertools import combinations
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb+srv://wjlaz:Josh2003@cardcluster.yskogdd.mongodb.net/'
client = MongoClient(uri, server_api = ServerApi('1'))

def pingM():
    try:
        client.admin.command('ping')
        print("You successfully connected!")
    except Exception as e:
        print(e)

def getCollection(dbname, collection):
   return client[dbname][collection]

def convert(rank):
    if rank == 'A':
      return 14
    elif rank == 'K':
      return 13
    elif rank == 'Q':
      return 12
    elif rank == 'J':
      return 11
    else:
      return int(rank)
    
def SimP():
  print('processing...')

  deck = [ str(x) for x in Deck().deck]
  permd = combinations(deck, 2)
  wins = {}
  #all cards
  for x in permd:
    wins[str(x)] = 0
    for i in range(100):
        game = Poker (8, Card(convert(x[0][:-1]), x[0][-1]) , Card(convert(x[1][:-1]) , x[1][-1]))
        game.play()
        if(game.Winner() == 1):
           wins[str(x)] += 1
  return wins

def main():
    pingM()
    wdict = SimP()
    collection = getCollection("PokerAI", "Win_rates")
    print("loading")
    for item in wdict:
        collection.insert_one({str(item): str(wdict[item])})

main()
print("End Process")