from sys import exit

current_room = [50]
killed = ["Cthulhu"]
race = ["human"]
prof = ["farmer"]
strength = [20]
spellpower = [20]
agility = [20]
health = [200]
potions = [0]
armour = [1]
weapon = [1]
gold = [1000]

rooms = {
    "50" : [["north"],"    The Gates are closed behind you. Your only option is to head into the town, to the (north)"],
    "51" : [["north", "south", "east", "west"],"""    You are walking along the main street of the town.
    There is no way off this street, as there are guards blocking all the side streets.
    This seems to be a security precaution in case anything gets loose from the Arena.\n
    The road continues to the (north) and (south). There are also some shops here.
    To the (west) you see 'Potent Potions', and to the (east) is 'Artificers Armour Shoppe'"""],
    "52" : [["north", "south", "east", "west"],"""    You are standing right in front of the Arena. You can hear the cheers from the crowds spectating
    To enter the Arenas ground, go (north). There is an abandoned building to the {west).
    To the east you see a crowd of people gathered around a window, peering at the wares in 'Wicked Weapons'"""],
    "53" : [["south", "combat"],"""    The roars of the crowds here is near deafening. You can barely make out the
    screams of pain coming from the pit over the crowd.
    You can head back to town for supplies to the (south) or step into the (combat) waiting area"""],
    "41" : [["east", "potion"],"""    As you step into the shop, you spend a few seconds coughing from the heavy fumes.
    A small shop owner in long flowing robes becons you over.
    \"Here for the Arena? You need some potions! Finest in the land!\"
    He pulls a small rack of red potions out and puts them on the counter.
    \"100 gold each. Guranteed to work! Fix your wounds instantly!\"
    \nYou can purchase a (potion) or leave the shop, going back (east)"""],
    "61" : [["west", "armour"],"61 -> BUY SOME ARMOUR OR DIE!"],
    "42" : [["east"],"42 - Nobody knows what this room is for"],
    "62" : [["west", "weapon"],"62 - The weapon shop!"]
}

def creation():
    print "    Welcome adventurer! Tell us about yourself."
    print "    Are you a (halfling), (elf), or an (orc)?"

    x = 1
    while x != 0:
        x = 0
        race_choice = raw_input("\nAvailable Actions: ['elf', 'halfling', 'orc']\n> ")
        if race_choice == "halfling":
            race[0] = "Halfling"
            agility[0] += 10
            armor[0] += 1
        elif race_choice == "elf":
            race[0] = "Elf"
            agility[0] += 10
            spellpower[0] += 10
        elif race_choice == "orc":
            race[0] = "Orc"
            strength[0] += 10
            health[0] += 25
        else:
            print "That is no race I have ever heard of! Try again."
            x = 1
    
    print "\n\n    Haha! Of course you are! I should have known by looking at you."
    print "\n    This next one is a little less obvious. Where do your talents lie?"
    print "    Are you are mighty (warrior), a sneaky (thief) or an arcane (mage)?"
    
    x = 1
    while x != 0:
        x = 0
        prof_choice = raw_input("\nAvailable Actions: ['mage', 'thief', 'warrior']\n> ")
        if prof_choice == "warrior":
            prof[0] = "Warrior" 
            strength[0] += 10
        elif prof_choice == "thief":
            prof[0] = "Thief"
            agility[0] += 20
        elif prof_choice == "mage":
            prof[0] = "Mage"
            spellpower[0] += 20
        else:
            print "Are you sure? Try again."
            x = 1
        
    print "\n\n    Lets just take your vitals and sign you up to the Arena before we continue."
    print "\nRace: %s\nClass: %s\nHealth: %i\nStrength: %i" % (race[0], prof[0], health[0], strength[0])
    print "Agility: %i\nSpell Power: %i" % (agility[0], spellpower[0])
    return()

def start():
    print "\n\n ARENA CHALLENGE v0.7\n\n"
    print "    Before you is the Hall of Creation. If you are ever unsure of your options,"
    print "    they will always be highlighted in brackets. To continue, enter the {hall) of creation."
    x = 1
    while x != 0:
        x = 0
        command = raw_input("\nAvailable Action: ['hall']\n> ")
        if command == "hall":
            print "\n\nYou set off into the Hall of Creation."
            creation()
        else:
            print "I do not understand the command. Try again."
            x = 1
    print "\n    Vitals taken and registration done, you are shown to the small town entrance. The gates close behind you"
    print "    There are banners hanging out of windows and lots of cheering for the local champions."
    print "    Some even seem to been cheering for the monsterous creatures pitted against the champions!"
    print "\n    There seems to be only one way down this street, and you can see the Arena in the distance" 
    available()
    
def available():
    print "\nYou have %i health, %i gold and %i potions\nAvailable actions: %s" % (health[0], gold[0], potions[0], rooms[str(current_room[0])][0])
    command(raw_input("> "))
    
def command(action):
    """Takes a command and checks if it is valid for the room. If it is, goes through if/else chain
to get to correct action."""
    x = 1
    while x != 0:
        x = 0
        if action in rooms[str(current_room[0])][0]:
            if action == "north" or action == "south" or action == "east" or action == "west":
                current_room[0] = movement(action, current_room[0])
                available()
            elif action == "potion":
                if gold[0] >= 100:
                    gold[0] -= 100
                    potions[0] += 1
                else:
                    print "You do not have enough gold."
                available()
            elif action == "combat":
                combat()            
            elif action == "armour":
                if gold[0] >= 450:
                    gold[0] -= 450
                    armour[0] += 1
                    print "Your armour value increases! You will take less damage in the Arena!"
                else:
                    print "You do not have enough gold."
                available()
            elif action == "weapon":
                if gold[0] >= 450:
                    gold[0] -= 450
                    weapon[0] += 1
                    print "You equip a better weapon! You will deal more damage in the Arena!"
                else:
                    print "You do not have enough gold."
                available()
            else:
                available()
        else:
            print "I do not understand the command. Try again."
            print "\nYou have %i health, %i gold and %i potions\nAvailable actions: %s" % (health[0], gold[0], potions[0], rooms[str(current_room[0])][0])
            action = raw_input("> ")
            x = 1
def movement(direction, attempt):
    if direction == "north":
        attempt += 1
    elif direction == "south":
        attempt -= 1
    elif direction == "east":
        attempt += 10
    elif direction == "west":
        attempt -= 10
    else:
        print "DEBUG ERROR - No valid direction fed to movement function"
    if str(attempt) in rooms:
        print "\nYou head %s\n" % direction
        print rooms[str(attempt)][1]
        return attempt

def dead(opponent):
    print "    Oh no. Sadly our favorite %s has been taken down by %s" % (race[0], opponent)
    print "    I guess they weren't quite as skilled as they thought. Your deeds shall be remembered!"
    exit(0)

def retire():
    print "    Our interpid adventurer, one of the most brave %s and definitely the most skilled %s has retired." % (race[0], prof[0])
    print "    Creatures defeated before retirement:"
    print killed
    exit(0)
    
start()
#commands available
#print rooms["51"][0]
#room descriptions
#print rooms["51"][1]
#if "65" in rooms: