import random


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
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.attackHigh = attack + 10
        self.attackLow = attack - 10
        self.defence = defence
        self.magic = magic
        self.actions = ["attack", "magic"]

    def generate_damage(self):
        return random.randrange(self.attackLow, self.attackHigh)

    def generate_spell_damage(self, i):
        magic_low = self.magic[i]["damage"] - 5
        magic_high = self.magic[i]["damage"] + 5

        return random.randrange(magic_low, magic_high)

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        for item in self.actions:
            print(str(i) + '  ' + item)
            i += 1
    def choose_magic(self):
        i = 1

        for spell in self.magic:
            print(str(i) + ' ' + spell["name"], "(Cost: ", str(spell["mp"] + ")" )
            i += 1