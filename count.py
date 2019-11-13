import csv

f = open("output.txt",'w')
dataSource = "./src/test-data.csv"

def elimCandidate(round, winner=None):
    f.write("Determining the winner of Round " + str(round) + ":\n")
    ballotList = []

    with open(dataSource, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            ballotList.append(row)

    if round == 2 and winner:
        for ballot in ballotList:
            ballot.remove(winner)

    candidatesDict = {}

    for candidate in ballotList[0]:
        candidatesDict[candidate] = [0] * (7 - round)

    def elimCandidate(candidatesLeft):
        for candidate in candidatesDict:
            candidatesDict[candidate] = [0] * candidatesLeft

        for ballot in ballotList:
            for pref, candidate in enumerate(ballot):
                candidatesDict[candidate][pref] += 1

        f.write("Round " + str(7 - candidatesLeft) + "\n")
        for candidate in candidatesDict:
            f.write(candidate + ": " + str(candidatesDict[candidate]) + "\n")
        
        candToElim = min(candidatesDict, key=candidatesDict.get)
        f.write(candToElim + " is eliminated\n\n")

        for ballot in ballotList:
            ballot.remove(candToElim) 

        candidatesDict.pop(candToElim, None)

    for x in range(0, (6 - round)):
        elimCandidate(len(candidatesDict))

    return(str(list(candidatesDict.keys())[0]))

firstWinner = elimCandidate(1)
f.write("First Winner is " + firstWinner + "\n\n\n\n\n")
secondWinner = elimCandidate(2, firstWinner)
f.write("Second Winner is " + secondWinner)

