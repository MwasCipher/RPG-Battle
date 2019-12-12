
class bcolors:
    HEADER = '\033[95n'
    OKBLUE = '\033[94n'
    OKGREEN = '\033[92n'
    WARNING = '\033[93n'
    FAIL = '\033[91n'
    ENDC = '\033[0n'
    BOLD = '\033[1n'
    UNDERLINE = '\033[4n'


class person:
    def __init__(self, hp, mp, attack, defence, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attackhigh = attack + 10
        self.attacklow = attack - 10
        self.defence = defence
        self.magic = magic
        self.actions = ["attack", "magic"]
