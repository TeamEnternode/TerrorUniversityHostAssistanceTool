from campus import Campus
from role import Role
from random import choice


class Player:
    def __init__(self, name: str):
        self.name = name
        self.campus = None
        self.role = None
        self.alignment = "Innocent"
        self.gender = "Random"

    def assign(self, role: Role, cmp: Campus, campusList: list):
        self.role = role
        if cmp.name not in ["Terrorists", "General Education"]:
            self.campus = cmp
        else:
            self.campus = choice(campusList)
            while self.campus.name in ["Terrorists", "General Education"]:
                self.campus = choice(campusList)
        if cmp.name == "Terrorists":
            self.alignment = "Corrupt"
        if role.alignment != "Unknown":
            self.alignment = role.alignment
        if role.gender != "Random":
            self.gender = role.gender
        else:
            self.gender = choice(["Male", "Female"])

    def __str__(self):
        return "Player {} is the {} {} {} at the {} campus".format(self.name, self.alignment, self.gender, self.role, self.campus)
