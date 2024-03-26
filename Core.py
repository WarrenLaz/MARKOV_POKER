from Game import Poker
from Cards import Deck
from Cards import Card
import math
from itertools import combinations 

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

def main ():
  
  deck = [ str(x) for x in Deck().deck]
  permd = combinations(deck, 2)

  wins = {}
  
  for x in permd:
    wins[str(x)] = 0
    for i in range(100):
        game = Poker (8, Card( convert(x[0][:-1]), x[0][-1]) , Card( convert(x[1][:-1]) , x[1][-1]))
        game.play()
        if(game.Winner() == 1):
           wins[str(x)] += 1

  f = open("Record1.txt", 'w') 
  i = 1
  for x in wins:
     print(x, wins[x], math.ceil((wins[x]/100)*100))
     f.write( str(i) + " " + str(x).replace('(', '').replace(')','').replace(',','').replace('\'','') + " " + str(wins[x]) + " " 
             + str(math.ceil((wins[x]/100)*100)) 
             + "\n")
     i += 1
  f.close()


  

main()
print('exit process')