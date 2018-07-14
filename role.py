class Role:
    def __init__(self, name: str, gender: str="Random", alignment: str="Unknown"):
        self.name = name
        self.gender = gender
        self.alignment = alignment

    def __str__(self):
        return self.name


AllRoles = {
    # Law Enforcement
    "Detective": Role("Detective", "Female"),
    "Forensic Scientist": Role("Forensic Scientist", "Male"),
    "Undercover Cop": Role("Undercover Cop", "Female"),
    "Interrogator": Role("Interrogator", "Male"),

    # Athletic
    "Coach": Role("Coach", "Male"),
    "Quarterback": Role("Quarterback", "Male"),
    "Cheerleader": Role("Cheerleader", "Female"),
    "Tennis Player": Role("Tennis Player", "Female"),

    # Law Studies
    "Defense Attorney": Role("Defense Attorney", "Female"),
    "Prosecutor": Role("Prosecutor", "Male"),
    "Judge": Role("Judge", "Male", "Innocent"),

    # Business Studies
    "Statistician": Role("Statistician", "Male"),
    "Marketing Agent": Role("Marketing Agent", "Female"),
    "Banker": Role("Banker", "Male"),
    "Manager": Role("Manager", "Male"),

    # School of Philosophy, Psychology, and Sociology
    "Psychiatrist": Role("Psychiatrist", "Male"),
    "Social Justice Advocate": Role("Social Justice Advocate", "Female"),
    "Political Scientist": Role("Political Scientist", "Male"),
    "Philosopher": Role("Philosopher", "Male"),

    # General Education
    "Special Needs Student": Role("Special Needs Student", "Female", "Innocent"),
    "Undecided Major": Role("Undecided Major", "Male"),
    "Drunk": Role("Drunk", "Male"),
    "Professor": Role("Professor", "Female"),
    "Dropout": Role("Dropout", "Male", "Neutral"),
    "Yandere": Role("Yandere", alignment="Neutral"),

    # Terrorists
    "The Mastermind": Role("The Mastermind", "Male", "Terrorist"),
    "Lucifer": Role("Lucifer", "Male", "Terrorists"),
    "Suicide Bomber": Role("Suicide Bomber", "Male", "Terrorist")
}
