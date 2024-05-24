import pandas
from Cards import Deck

f = open("Record1.txt", 'r')
ma = open("RecordMatrix.txt", "w")
data = []

f.readline()
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

for x in d:
    t.append(str(x))
m.append(t)

t = [' ' for _ in range(53)]

for x in d:
    t = [' ' for _ in range(53)]
    t[0] = str(x)
    m.append(t)


for x in data:
    m[m[0].index(x[1])][m[0].index(x[2])] = str(x[-1])

for x in m:
    for y in x:
            print(y)
            ma.write(str(y) + "\t")
    ma.write("\n")

ma.close()
f.close()


