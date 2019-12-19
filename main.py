from classes.game import Person, BColors


magic = [{"name": "Fire", "cost": 10, "damage": 60},
         {"name": "Thunder", "cost": 10, "damage": 60},
         {"name": "Blizzard", "cost": 10, "damage": 60}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(BColors.FAIL + BColors.BOLD + "An Enemy Attacks", BColors.ENDC)

print('I Love Pink Pussy................!!!!!!!!!!>>>>>>>>>>>>>>>!!!!!!!!!!!!!..............')

# while running:
#     print('Lets Flood This Stack.......... !!!!!', i)
#     i += 1

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))

