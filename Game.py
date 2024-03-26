from Cards import Deck

class Poker (object):

  def __init__ (self, numHands, card1, card2):
    self.deck = Deck()
    self.deck.shuffle()
    self.hands = []
    self.tlist=[]       #create a list to store total_point
    numCards_in_Hand = 5

    #River
    River = []
    for j in range (numCards_in_Hand):
        River.append(self.deck.deal())

    #You 
    hand = []
    hand.extend(River)
    hand.extend([card1, card2])
    self.deck.removecard(card1)
    self.deck.removecard(card2)
    self.hands.append (hand)

    #adversary 
    for i in range (numHands):
      hand = []
      hand.extend(River)
      hand.extend([self.deck.deal(),self.deck.deal()])
      self.hands.append (hand)
  
  def play (self):
    for i in range (len (self.hands) ):
      sortedHand = sorted (self.hands[i], reverse = True)
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '
      print (str(i + 1) + ': ' + hand)
      self.isRoyal(sortedHand)
    print('W: ' + str(self.Winner()))

  def Winner(self):
    return self.tlist.index(max(self.tlist))+1

  def point(self,hand):                         #point()function to calculate partial score
    sortedHand=sorted(hand,reverse=True)
    c_sum=0
    ranklist=[]
    for card in sortedHand:
      ranklist.append(card.rank)
    c_sum=ranklist[0]*13**4+ranklist[1]*13**3+ranklist[2]*13**2+ranklist[3]*13+ranklist[4]
    return c_sum
      
  def isRoyal (self, hand):               #returns the total_point and prints out 'Royal Flush' if true, if false, pass down to isStraightFlush(hand)
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=10
    Cursuit=sortedHand[0].suit
    Currank=14
    total_point=h*13**5+self.point(sortedHand)
    for card in sortedHand:
      if card.suit!=Cursuit or card.rank!=Currank:
        flag=False
        break
      else:
        Currank-=1
    if flag:
        self.tlist.append(total_point)    
    else:
      self.isStraightFlush(sortedHand)
    

  def isStraightFlush (self, hand):       #returns the total_point and prints out 'Straight Flush' if true, if false, pass down to isFour(hand)
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=9
    Cursuit=sortedHand[0].suit
    Currank=sortedHand[0].rank
    total_point=h*13**5+self.point(sortedHand)
    for card in sortedHand:
      if card.suit!=Cursuit or card.rank!=Currank:
        flag=False
        break
      else:
        Currank-=1
    if flag:
      self.tlist.append(total_point)
    else:
      self.isFour(sortedHand)

  def isFour (self, hand):                  #returns the total_point and prints out 'Four of a Kind' if true, if false, pass down to isFull()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=8
    Currank=sortedHand[1].rank               #since it has 4 identical ranks,the 2nd one in the sorted listmust be the identical rank
    count=0
    total_point=h*13**5+self.point(sortedHand)
    for card in sortedHand:
      if card.rank==Currank:
        count+=1
    if not count<4:
      flag=True
      self.tlist.append(total_point)

    else:
      self.isFull(sortedHand)
    
  def isFull (self, hand):                     #returns the total_point and prints out 'Full House' if true, if false, pass down to isFlush()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=7
    total_point=h*13**5+self.point(sortedHand)
    mylist=[]                                 #create a list to store ranks
    for card in sortedHand:
      mylist.append(card.rank)
    rank1=sortedHand[0].rank                  #The 1st rank and the last rank should be different in a sorted list
    rank2=sortedHand[-1].rank
    num_rank1=mylist.count(rank1)
    num_rank2=mylist.count(rank2)
    if (num_rank1==2 and num_rank2==3)or (num_rank1==3 and num_rank2==2):
      flag=True
      self.tlist.append(total_point)
      
    else:
      flag=False
      self.isFlush(sortedHand)

  def isFlush (self, hand):                         #returns the total_point and prints out 'Flush' if true, if false, pass down to isStraight()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=6
    total_point=h*13**5+self.point(sortedHand)
    Cursuit=sortedHand[0].suit
    for card in sortedHand:
      if not(card.suit==Cursuit):
        flag=False
        break
    if flag:
      self.tlist.append(total_point)
    else:
      self.isStraight(sortedHand)

  def isStraight (self, hand):
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=5
    total_point=h*13**5+self.point(sortedHand)
    Currank=sortedHand[0].rank                        #this should be the highest rank
    for card in sortedHand:
      if card.rank!=Currank:
        flag=False
        break
      else:
        Currank-=1
    if flag:
      self.tlist.append(total_point)
      
    else:
      self.isThree(sortedHand)
        
  def isThree (self, hand):
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=4
    total_point=h*13**5+self.point(sortedHand)
    Currank=sortedHand[2].rank                    #In a sorted rank, the middle one should have 3 counts if flag=True
    mylist=[]
    for card in sortedHand:
      mylist.append(card.rank)
    if mylist.count(Currank)==3:
      flag=True
      self.tlist.append(total_point)
      
    else:
      flag=False
      self.isTwo(sortedHand)
        
  def isTwo (self, hand):                           #returns the total_point and prints out 'Two Pair' if true, if false, pass down to isOne()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=3
    total_point=h*13**5+self.point(sortedHand)
    rank1=sortedHand[1].rank                        #in a five cards sorted group, if isTwo(), the 2nd and 4th card should have another identical rank
    rank2=sortedHand[3].rank
    mylist=[]
    for card in sortedHand:
      mylist.append(card.rank)
    if mylist.count(rank1)==2 and mylist.count(rank2)==2:
      flag=True
      self.tlist.append(total_point)
      
    else:
      flag=False
      self.isOne(sortedHand)
  
  def isOne (self, hand):                            #returns the total_point and prints out 'One Pair' if true, if false, pass down to isHigh()
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=2
    total_point=h*13**5+self.point(sortedHand)
    mylist=[]                                       #create an empty list to store ranks
    mycount=[]                                      #create an empty list to store number of count of each rank
    for card in sortedHand:
      mylist.append(card.rank)
    for each in mylist:
      count=mylist.count(each)
      mycount.append(count)
    if mycount.count(2)==2 and mycount.count(1)==3:  #There should be only 2 identical numbers and the rest are all different
      flag=True
      self.tlist.append(total_point)
      
    else:
      flag=False
      self.isHigh(sortedHand)

  def isHigh (self, hand):                          #returns the total_point and prints out 'High Card' 
    sortedHand=sorted(hand,reverse=True)
    flag=True
    h=1
    total_point=h*13**5+self.point(sortedHand)
    mylist=[]                                       #create a list to store ranks
    for card in sortedHand:
      mylist.append(card.rank)
    self.tlist.append(total_point)