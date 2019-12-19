from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "damage": 100},
         {"name": "Thunder", "cost": 10, "damage": 124},
         {"name": "Blizzard", "cost": 10, "damage": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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

    elif damage == 1:
        player.choose_magic()
        choice = int(input("Select Spell: ")) - 1
        magic_damage = player.generate_spell_damage(choice)
        spell = player.get_spell_name(choice)
        cost = player.get_spell_magic_points_cost(choice)

        current_magic_point = player.get_magic_points()

        if cost > current_magic_point:
            print(BColors.FAIL, "\nYou Don't Have Enough Life", BColors.ENDC)

        print("You Attacked For: ", damage, "Points of Damage", "Enemy Hit Points: ", enemy.get_hp())

    # running = False

    enemy_choice = 1
    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy Attacks For", enemy_damage, "Player Hit Point: ", player.get_hp())

    if enemy.get_hp() == 0:
        print(BColors.OKGREEN, "You Fucking Win......#@!#@!#@!@##$$^$&%^&", BColors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print(BColors.FAIL, "You Fucking Lost Loser......#@!#@!#@!@##$$^$&%^&", BColors.ENDC)
        running = False
