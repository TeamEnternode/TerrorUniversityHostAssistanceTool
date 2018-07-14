import role
from campus import CampusDict
from random import choice


class RoleSlot:
    def __init__(self, name: str, possibilities: list):
        self.name = name
        self.possibilities = possibilities

    def decide(self, campuses: list) -> tuple:
        if self.name == "Random":
            cmp = choice(campuses)
            r = choice(cmp.roles)
            while r.alignment == "Neutral":
                r = choice(cmp.roles)
            return r, cmp
        else:
            r = choice(self.possibilities)
            for name, camp in CampusDict.items():
                for ro in camp.roles:
                    if ro == r:
                        return r, camp
            print("ERROR: ROLE SLOT {} CANNOT BE RESOLVED (MISSING FROM CAMPUS LIST)".format(r))

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if len(other.possibilities) == 1:
            if other.possibilities[0].alignment == "Terrorist":
                return False
        if len(self.possibilities) == 1:
            if self.possibilities[0].alignment == "Terrorist":
                return True
        if len(other.possibilities) == 1:
            if other.possibilities[0].alignment == "Neutral":
                return False
        if len(self.possibilities) == 1:
            if self.possibilities[0].alignment == "Neutral":
                return True
        if len(other.possibilities) == 1 and len(self.possibilities) != 1:
            return False
        if len(self.possibilities) == 1 and len(other.possibilities) != 1:
            return True
        if len(other.possibilities) > 1 and len(self.possibilities) == 0:
            return False
        if len(self.possibilities) > 1 and len(other.possibilities) == 0:
            return True
        return False


RoleSlotDict = {
    "Random Law Enforcement": RoleSlot("Random Law Enforcement", CampusDict["Law Enforcement"].roles),
    "Random Athletic": RoleSlot("Random Athletic", CampusDict["Athletic"].roles),
    "Random Law Studies": RoleSlot("Random Athletic", CampusDict["Law Studies"].roles),
    "Random Business Studies": RoleSlot("Random Business Studies", CampusDict["Business Studies"].roles),
    "Random General Education": RoleSlot("Random General Education", CampusDict["General Education"].roles),
    "Random SPPS": RoleSlot("Random SPPS", CampusDict["SPPS"].roles),
    "Random": RoleSlot("Random", []),
    "Random Neutral": RoleSlot("Random Neutral", [role.AllRoles["Dropout"], role.AllRoles["Yandere"]]),
    "Random Terrorist": RoleSlot("Random Terrorist", CampusDict["Terrorists"].roles),
    "Any Law Enforcement": RoleSlot("Any Law Enforcement", CampusDict["Law Enforcement"].roles),
    "Any Athletic": RoleSlot("Any Athletic", CampusDict["Athletic"].roles),
    "Any Law Studies": RoleSlot("Any Athletic", CampusDict["Law Studies"].roles),
    "Any Business Studies": RoleSlot("Any Business Studies", CampusDict["Business Studies"].roles),
    "Any General Education": RoleSlot("Any General Education", CampusDict["General Education"].roles),
    "Any SPPS": RoleSlot("Any SPPS", CampusDict["SPPS"].roles),
    "Any Neutral": RoleSlot("Any Neutral", [role.AllRoles["Dropout"], role.AllRoles["Yandere"]]),
    "Any Terrorist": RoleSlot("Any Terrorist", CampusDict["Terrorists"].roles),
    "Any": RoleSlot("Any", list(role.AllRoles.values()))
}

for k, ROLE in role.AllRoles.items():
    RoleSlotDict[ROLE.name] = RoleSlot(ROLE.name, [ROLE])
