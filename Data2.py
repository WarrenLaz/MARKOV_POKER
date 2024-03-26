import pandas
from Cards import Deck

f = open("Record2.txt", 'r')
ma = open("RecordMatrix2.txt", "w")
data = []

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

for line in f:
    t = []
    vector = line.split(" ")
    t.append(int(vector[0]))
    t.append(vector[1])
    t.append(vector[2])
    t.append(int(vector[3]))
    t.append(int(vector[4]))
    data.append(t)

d = Deck().deck
m = []
t = ['[\]']

for x in ranks:
    t.append(str(x))
m.append(t)

t = [' ' for _ in range(14)]

for x in ranks:
    t = [' ' for _ in range(14)]
    t[0] = str(x)
    m.append(t)

for x in data:
    m[m[0].index(x[1])][m[0].index(x[2])] = str(x[-1])

for x in m:
    for y in x:
        ma.write(str(y) + "\t")
    ma.write("\n")

ma.close()
f.close()


