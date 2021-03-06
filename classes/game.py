import random


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # hp = hit_point


class Person:
    def __init__(self, hp, magic_points, attack, defence, magic, items):
        self.maxHp = hp
        self.hp = hp
        self.maxMagic_points = magic_points
        self.magic_points = magic_points
        self.attackHigh = attack + 10
        self.attackLow = attack - 10
        self.defence = defence
        self.magic = magic
        self.items = items
        self.actions = ["attack", "magic", "items"]

    def generate_damage(self):
        return random.randrange(self.attackLow, self.attackHigh)

    # def generate_spell_damage(self, i):
    #     magic_low = self.magic[i]["damage"] - 5
    #     magic_high = self.magic[i]["damage"] + 5
    #
    #     return random.randrange(magic_low, magic_high)

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, damage):
        self.hp += damage
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_magic_points(self):
        return self.magic_points

    def get_max_magic_points(self):
        return self.maxMagic_points

    def reduce_magic_points(self, cost):
        self.magic_points -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]["name"]
    #
    # def get_spell_magic_points_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("Action")

        for item in self.actions:
            print("    ", str(i) + '  ' + item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")

        for spell in self.magic:
            print("    ", str(i), ' ', spell.name, "(Cost: ", spell.damage, ")")
            i += 1

    def choose_item(self):
        i = 1
        print(BColors.OKGREEN, BColors.BOLD, "ITEMS", BColors.ENDC)

        for item in self.items:
            print("    ", str(i), ".", item["item"].name, ": ",
                  item["item"].description, "(x"+str(item["quantity"])+")")
            i += 1
