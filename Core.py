from Game import Poker
from Cards import Deck
from Cards import Card
import math
from itertools import combinations 
import os

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

def readrecord(record):
  data = []
  n = 0
  if(os.stat("Record1.txt").st_size == 0):
     return data, n
  
  n = int(record.readline())
  for line in record:
      t = []
      vector = line.split(" ")
      t.append(int(vector[0]))
      t.append(vector[1])
      t.append(vector[2])
      t.append(int(vector[3]))
      t.append(int(vector[4]))
      data.append(t)

  return data, n 

def hashcard(card):
   hashcode = 0
   pair = str(card[0]) + str(card[1])

   r = 1
   for alpha in pair:
      print(alpha)
      hashcode+=int(ord(alpha))*r
      r*=100
   return hashcode


def main ():
  
  deck = [ str(x) for x in Deck().deck]
  permd = combinations(deck, 2)

  wins = {}
  
  #all cards
  for x in permd:
    hashcard(x)
    wins[hashcard(x)] = 0
    for i in range(100):
        game = Poker (8, Card( convert(x[0][:-1]), x[0][-1]) , Card( convert(x[1][:-1]) , x[1][-1]))
        game.play()
        if(game.Winner() == 1):
           wins[hashcard(x)] += 1

  r = open("Record1.txt", 'r')
  datab, numruns = readrecord(r)
  numruns += 1

  f = open("Record1.txt", 'w') 
  f.write(str(numruns) + "\n")
  i = 1
  j = 0
  if(numruns==1):
     for x in wins:
        print(x, wins[x])
        f.write( str(i) + " " 
                + str(x).replace('(', '').replace(')','').replace(',','').replace('\'','') 
                + " " + str(wins[x]) + " " 
                + str(math.ceil(((wins[x])/100)*100)) 
                + "\n")
        i += 1
  else: 
    for x in wins:
       print(x, wins[x])
       f.write( str(i) + " " 
               + str(x).replace('(', '').replace(')','').replace(',','').replace('\'','') 
               + " " + str(wins[x]+datab[j][3]) + " " 
               + str(math.ceil(((wins[x]+datab[j][3])/(100*numruns))*100)) 
               + "\n")
       j += 1
       i += 1
  
  print(numruns)
  f.close()

main()
print('exit process')