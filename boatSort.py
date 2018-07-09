import json

rowers = []
friendList = []

with open("rowers.csv", "r") as rowFile:
    friends  = json.load(rowFile)
    
    for r in friends:
        rowers.append(r[0])
        friendList.append(r[1:])
    #should do data verification here

    print friendList

