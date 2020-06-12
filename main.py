from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# black magic
fire = Spell('Fire', 18, 160, "black")
thunder = Spell('Thunder', 10, 120, "black")
blizzard = Spell('Blizzard', 20, 200, "black")
meteor = Spell('Meteor', 8, 50, "black")
quake = Spell('Quake', 25, 300, "black")

# white magic
cure = Spell('Cure', 20, 80, 'white')
cura = Spell('Cura', 60, 180, 'white')

# creating items
potion = Item('potion', 'potion', 'Heals 50 hp', 50)
hipotion = Item('hipotion', 'potion', 'Heals 100 hp', 100)
supotion = Item('supotion', 'potion', 'Heals 200', 200)
elixer = Item('Elixer', 'elixer', 'Fully restores MP/HP of one', 9999)
hixer = Item('High-elixer', 'elixer', "Fully restore party's MP/HP", 99999)


grenade = Item('Grenade', 'attack', 'Deals 500 dmg', 500)


player_spell = [fire, thunder, cure, cura]
player_items = [{"item": potion, "quantity": 2}, {"item": grenade, "quantity": 5}, ]

# making People :)
player = Person(460, 65, 60, 34, player_spell, player_items)
enemy = Person(1200, 65, 100, 80, [meteor, quake, cure], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "Enemy attacks" + bcolors.ENDC)



while running:
    print("=======================================")
    player.choose_action()
    choice = input("Choose action")
    index = int(choice) - 1


    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for: ", dmg, "Enemy health is ", enemy.get_hp())



    elif  index == 1:
        player.choose_spell()
        magic_choice = int(input("Choose spell"))-1

        if magic_choice == -1:  # back menu
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        cost = spell.cost
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough mp\n" + bcolors.ENDC)
            continue

        if spell.type == 'white':
            player.heal(magic_dmg)
            print(bcolors.WARNING + spell.name + " Heals for ", magic_dmg, bcolors.ENDC )

        elif spell.type == 'black':
            player.reduce_mp(cost)
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", magic_dmg, "points of damage" + bcolors.ENDC)
            print("You attacked for: ", magic_dmg, "Enemy health is ", enemy.get_hp())



    elif index == 2:
        player.choose_item()  # shows players items
        item_choice = int(input("Choose item"))-1 # gets players choice

        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"] #choosing item from players_item next taking name and choosing item with class to get type

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL+"You haven't got enough items"+bcolors.ENDC+"\n")
            player.items[item_choice]["quantity"] =0
            continue

        player.reduce_quantity(item_choice)

        if item.type == 'potion':
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + "heals for ", str(item.prop), "HP" + bcolors.ENDC)

        elif item.type == 'elixer':
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + "fully restores HP/MP" + bcolors.ENDC)

        elif item.type == 'attack':
            enemy.take_damage(item.prop)
            print(bcolors.OKGREEN + "\n" + "you've attack for ",str(item.prop) + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("==================================")
    print("Enemy hp:", bcolors.FAIL + str(enemy.get_hp()), "/", str(enemy.get_max_hp()) + bcolors.ENDC)

    print("Your hp:", bcolors.OKGREEN + str(player.get_hp()), "/", str(player.get_max_hp()) + bcolors.ENDC)
    print("Your mp ", bcolors.OKBLUE + str(player.get_mp()), "/", str(player.get_max_mp()) + bcolors.ENDC)


    if enemy.get_hp() == 0:
        running = False
        print(bcolors.OKGREEN + "YOU WON" + bcolors.ENDC)

    if player.get_hp() == 0:
        running = False
        print(bcolors.BOLD + bcolors.FAIL + "You lost" + bcolors.ENDC)

