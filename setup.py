import campus
import roleslot
from random import shuffle
from random import choice


class Setup:
    def __init__(self, name: str, slots: list=None, corrupts: list=None, minplayers: int=5):
        self.name = name
        if slots is None:
            slots = []
        self.slots = slots
        if corrupts is None:
            corrupts = []
        self.corrupts = corrupts
        self.maxplayers = len(slots)
        self.minplayers = minplayers
        self.campuses = []

    def assignAllPlayers(self, players: list):
        alreadyAssigned = []
        self.slots = self.slots[:len(players)]
        self.slots.sort()
        for s in self.slots:
            if s.name == "Random Law Enforcement" and campus.CampusDict["Law Enforcement"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Law Enforcement"])
            if s.name == "Random Athletic" and campus.CampusDict["Athletic"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Athletic"])
            if s.name == "Random Law Studies" and campus.CampusDict["Law Studies"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Law Studies"])
            if s.name == "Random Business Studies" and campus.CampusDict["Business Studies"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Business Studies"])
            if s.name == "Random SPPS" and campus.CampusDict["SPPS"] not in self.campuses:
                self.campuses.append(campus.CampusDict["SPPS"])
            if s.name == "Random General Education" and campus.CampusDict["General Education"] not in self.campuses:
                self.campuses.append(campus.CampusDict["General Education"])
            if s.name == "Any Law Enforcement" and campus.CampusDict["Law Enforcement"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Law Enforcement"])
            if s.name == "Any Athletic" and campus.CampusDict["Athletic"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Athletic"])
            if s.name == "Any Law Studies" and campus.CampusDict["Law Studies"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Law Studies"])
            if s.name == "Any Business Studies" and campus.CampusDict["Business Studies"] not in self.campuses:
                self.campuses.append(campus.CampusDict["Business Studies"])
            if s.name == "Any SPPS" and campus.CampusDict["SPPS"] not in self.campuses:
                self.campuses.append(campus.CampusDict["SPPS"])
            if s.name == "Any General Education" and campus.CampusDict["General Education"] not in self.campuses:
                self.campuses.append(campus.CampusDict["General Education"])

        shuffle(players)
        for i in range(0, len(players)):
            res = self.slots[i].decide(self.campuses)
            while res[0].name in alreadyAssigned and "Any" not in self.slots[i].name:
                res = self.slots[i].decide(self.campuses)
            if res[1] not in self.campuses:
                self.campuses.append(res[1])
            players[i].assign(res[0], res[1], self.campuses)
            alreadyAssigned.append(res[0].name)

        corruptCount = 0
        for i in self.corrupts:
            if len(players) >= i:
                corruptCount += 1

        if corruptCount != 0:
            for i in range(0, corruptCount):
                p = choice(players)
                while p.alignment != "Innocent":
                    p = choice(players)
                p.alignment = "Corrupt"

    def choosetarget(self) -> campus.Campus:
        r = choice(self.campuses)
        while r.name in ["General Education"]:
            r = choice(self.campuses)
        return r

    def __str__(self):
        return self.name


rs = roleslot.RoleSlotDict

setupDict = {
    "Custom": Setup("Custom"),
    "Beginner (Small)": Setup("Beginner (Small)", [
        rs["The Mastermind"],
        rs["Random Law Enforcement"],
        rs["Random Law Enforcement"],
        rs["Random Athletic"],
        rs["Random"],
        rs["Random"],
        rs["Professor"],
    ], [4]),

    "Beginner": Setup("Beginner", [
        rs["The Mastermind"],
        rs["Random Law Enforcement"],
        rs["Random Law Enforcement"],
        rs["Random Athletic"],
        rs["Random Business Studies"],
        rs["Professor"],
        rs["Random"],
        rs["Random"],
        rs["Random"],
        rs["Random Business Studies"],
        rs["Random Athletic"],
        rs["Dropout"],
        rs["Random"],
        rs["Random"]
    ], [6, 8, 13], 7),

    "Court of Justice (Small)": Setup("Court of Justice (Small)", [
        rs["Lucifer"],
        rs["Judge"],
        rs["Random Law Enforcement"],
        rs["Random Law Studies"],
        rs["Random"],
        rs["Random"],
        rs["Random Neutral"]
    ]),

    "Court of Justice": Setup("Court of Justice", [
        rs["Lucifer"],
        rs["Judge"],
        rs["Random Law Enforcement"],
        rs["Random Business Studies"],
        rs["Random"],
        rs["Random"],
        rs["Random Neutral"],
        rs["Random Business Studies"],
        rs["Random Law Studies"],
        rs["Random"],
        rs["Professor"],
        rs["Undecided Major"],
        rs["Random"],
        rs["Random Neutral"],
    ], [9], 7),

    "Advanced (Small)": Setup("Advanced (Small)", [
        rs["Lucifer"],
        rs["Random SPPS"],
        rs["Random Athletic"],
        rs["Random"],
        rs["Random"],
        rs["Random"],
        rs["Yandere"],
    ]),

    "Advanced": Setup("Advanced", [
        rs["Lucifer"],
        rs["Random SPPS"],
        rs["Random Business Studies"],
        rs["Random Law Studies"],
        rs["Random SPPS"],
        rs["Random"],
        rs["Yandere"],
        rs["Random"],
        rs["Random"],
        rs["Random General Education"],
        rs["Random Law Enforcement"],
        rs["Random"],
        rs["Random Business Studies"],
        rs["Random Neutral"],
    ], [9], 7),
}
