from player import Player
from setup import setupDict
from random import choice
from roleslot import RoleSlotDict


def getVerifiedInput(prompt: str, options: list, listOptions: bool=True) -> str:
    if prompt != "":
        print(prompt)
    if listOptions:
        for i in options:
            print(i)
    r = input()
    while r not in options:
        print("Invalid response {}".format(r))
        r = input()
    return r


def getVerifiedClass(prompt: str, options: list, listOptions: bool=True):
    if prompt != "":
        print(prompt)
    if listOptions:
        for i in options:
            print(i)
    r = None
    while r is None:
        s = input()
        r = None
        for option in options:
            if s == str(option):
                r = option
        if r is None:
            print("Invalid response {}".format(s))
    return r


numPlayers = int(input("Welcome to the TUHAT! How many players are playing? \n"))
players = []


print("Please list the names of the players:")
for i in range(0, numPlayers):
    players.append(Player(input()))

validsetups = ["Custom"]
for k, v in setupDict.items():
    if v.minplayers <= numPlayers <= v.maxplayers:
        validsetups.append(v.name)

currentSetup = setupDict[getVerifiedInput("The following setups are valid. Which would you like to play?", validsetups)]
if currentSetup.name == "Custom":
    print("Which role slots would you like to use? List {} slots, including the Terrorist.".format(numPlayers))
    for i in range(0, numPlayers):
        currentSetup.slots.append(getVerifiedClass("", list(RoleSlotDict.values()), False))
    numCorrupt = int(input("How many corrupt members should there be?\n"))
    for i in range(0, numCorrupt):
        currentSetup.corrupts.append(i)
    currentSetup.maxplayers = len(currentSetup.slots)

currentSetup.assignAllPlayers(players)

for p in players:
    print(p)

print("The Terrorist must target the {} campus".format(currentSetup.choosetarget().name))

for p in players:
    if p.role.name == "Yandere":
        men, women = [], []
        for q in players:
            if q.role.name != "Dropout":
                if q.gender == "Male" and q is not p:
                    men.append(q)
                elif q.gender == "Female" and q is not p:
                    women.append(q)
        if p.gender == "Male":
            print("The Yandere's Senpai is {} and their rival is {}.".format(choice(women).name, choice(men).name))
        else:
            print("The Yandere's Senpai is {} and their rival is {}.".format(choice(men).name, choice(women).name))
pass
