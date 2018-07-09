import random
import json

numRowers = 4

rowers = ['a','b','c','d','e','f','g','h']


with open("rowers.csv", "w") as rowFile, open("pairScore.csv", "w") as pairFile:
    allRowers= []
    for rwr in rowers:
        i = rowers.index(rwr)
        friendList = random.sample(rowers[:i] + rowers[i+1:], 3)
        friendList.insert(0, rwr)
        #rowFile.write(str(friendList) + "\n")
        allRowers.append(friendList)
    json.dump(allRowers, rowFile)

    allscores = []
    for rwr1 in rowers:
        for rwr2 in rowers[:(rowers.index(rwr1))]:
            allscores.append( (rwr1,rwr2,random.randint(0,10)) )

    json.dump(allscores, pairFile);




