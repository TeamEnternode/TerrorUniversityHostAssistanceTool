from role import Role
from role import AllRoles


class Campus:
    def __init__(self, name: str, roles: list=None):
        if roles is None:
            roles = []
        self.name = name
        self.roles = roles

    def addRole(self, r: Role):
        self.roles.append(r)

    def addRoleList(self, rl: list):
        for role in rl:
            self.roles.append(role)

    def __str__(self):
        return self.name


CampusDict = {
    "Law Enforcement": Campus("Law Enforcement", [
        AllRoles["Detective"],
        AllRoles["Forensic Scientist"],
        AllRoles["Undercover Cop"],
        AllRoles["Interrogator"]
    ]),

    "Athletic": Campus("Athletic", [
        AllRoles["Coach"],
        AllRoles["Quarterback"],
        AllRoles["Cheerleader"],
        AllRoles["Tennis Player"]
    ]),

    "Law Studies": Campus("Law Studies", [
        AllRoles["Defense Attorney"],
        AllRoles["Prosecutor"],
        AllRoles["Judge"]
    ]),

    "Business Studies": Campus("Business Studies", [
        AllRoles["Statistician"],
        AllRoles["Marketing Agent"],
        AllRoles["Banker"],
        AllRoles["Manager"]
    ]),

    "SPPS": Campus("SPPS", [
        AllRoles["Psychiatrist"],
        AllRoles["Social Justice Advocate"],
        AllRoles["Political Scientist"],
        AllRoles["Philosopher"]
    ]),

    "General Education": Campus("General Education", [
        AllRoles["Professor"],
        AllRoles["Dropout"],
        AllRoles["Yandere"],
        AllRoles["Special Needs Student"],
        AllRoles["Undecided Major"],
        AllRoles["Drunk"]
    ]),

    "Terrorists": Campus("Terrorists", [
        AllRoles["The Mastermind"],
        AllRoles["Lucifer"],
        AllRoles["Suicide Bomber"]
    ])
}