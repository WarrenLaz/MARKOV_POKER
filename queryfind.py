from Game import Poker
from Cards import Card
from Cards import Deck
import random
from itertools import combinations 
import matplotlib.pyplot as plt

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

a = random.randint(1,14)
b = random.randint(1,14)

deck = [ str(x) for x in Deck().deck]
permd = list(combinations(deck, 2))
wins = {}

def hashcard(card):
   hashcode = 0
   pair = str(card[0]) + str(card[1])

   r = 1
   for alpha in pair:
      hashcode+=int(ord(alpha))*r
      r*=100
   return hashcode

f = open("Record1.txt", 'r')
cp = {}
next(f)
for x in f:
   r = x.split()
   cp[int(r[1])] = int(r[-1])

allowance = 100
#all cards
gameslist = []
gamenum = [i for i in range(1000)]
#for x in range (100):
for i in range(10):
    games = []
    for i in range(1000):
              bet = allowance/2
              pot = bet*8
              x = random.choice(permd)
              xhash = hashcard(x)
              print(x, hashcard(x))
              if(cp[xhash] > 20):
                bet = bet * (cp[xhash] * 0.01)
                game = Poker (8, Card( convert(x[0][:-1]), x[0][-1]) , Card( convert(x[1][:-1]) , x[1][-1]))
                game.play()

                if(game.Winner() == 1):
                    allowance += bet
                else: 
                    allowance -= bet
              games.append(allowance)
        #games.append(allowance)
    gameslist.append(games)
    allowance = 100

print('yourallowance: ' + str(allowance))

for g in gameslist:
    plt.plot(gamenum,g)

plt.xlabel('game')
plt.ylabel('allowance')
plt.title('graph')
plt.show()