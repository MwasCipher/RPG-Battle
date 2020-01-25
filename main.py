from classes.game import Person, BColors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic

fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 124, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Meteor", 12, 120, "black")

# Create Whit Magic

cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Items

potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "super potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Restores HP/MP one Party Member", 999)
megaelixer = Item("Mega Elixer", "mega elixer", "Restores HP/MP one Party Member", 9999)

grenade = Item("Grenade", "attack", "Deals damage of 500 HP", 500)

player_spells = [fire, thunder, blizzard, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, megaelixer]

player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(BColors.FAIL + BColors.BOLD + "An Enemy Attacks", BColors.ENDC)

while running:
    print('============================================================')
    player.choose_action()

    choice = input("Choose Action:  ")

    index = int(choice) - 1

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Select Magic Spell: ")) - 1
        # magic_damage = player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.generate_damage(magic_choice)

        spell = player.magic[magic_choice]
        magic_damage = spell.generate_spell_damage()

        current_magic_point = player.get_magic_points()

        if spell.cost > current_magic_point:
            print(BColors.FAIL, "\nYou Don't Have Enough Life", BColors.ENDC)
            continue

        player.reduce_magic_points(spell.cost)

        if spell.type == "white":
            player.heal(magic_damage)
            print(BColors.OKBLUE, "\n", spell.name, "Heals For", str(magic_damage), "HP", BColors.ENDC)

        elif spell.type == "black":
            enemy.take_damage(magic_damage)
            print(BColors.OKBLUE, "\n", spell.name, "deals", str(magic_damage), "Points of Damage", BColors.ENDC)

    if index == 2:
        player.choose_item()
        item_choice = int(input("Select Item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]
        if item.item_type == "potion":
            player.heal(item.prop)
            print(BColors.OKGREEN, "\n", item.name, "Heals For", str(item.prop), "HP", BColors.ENDC)

        # print("You Attacked For: ", damage, "Points of Damage")

    # running = False

    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy Attacks For", enemy_damage)
    print("====================================")
    print("Enemy Hit Points: ", BColors.FAIL,
          str(enemy.get_hp()), "/", str(enemy.get_max_hp()), BColors.ENDC, "\n")
    print("Your Hit Points: ", BColors.OKGREEN,
          str(player.get_hp()), "/", str(player.get_max_hp()), "\n")
    print("Your Magic Points: ", BColors.OKBLUE,
          str(player.get_magic_points()), "/", str(player.get_max_magic_points()))

    if enemy.get_hp() == 0:
        print(BColors.OKGREEN, "You Fucking Win......#@!#@!#@!@#$$#&&!!!", BColors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(BColors.FAIL, "You Fucking Lost You Dumb Loser......#@!#@!#@!@##$$^$&%^&", BColors.ENDC)
        running = False
