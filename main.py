import json
import sys
import time
import os
import random

start = True
zone = "Desert"

# Function to check file existence and initialize with default data if missing
def load_json(file_path, default_data):
    """Loads JSON data from a file, creating the file with default data if it does not exist."""
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump(default_data, f, indent=2)
        print(f"{file_path} not found. Creating with default data.")
    
    with open(file_path, 'r') as f:
        return json.load(f)

# Loading JSON data with defaults if files do not exist
default_characters = {
    "characters": {
        "noob": {
            "name": "noob",
            "race": "orc",
            "level": 1,
            "gold": 10,
            "health":30,
            "damage":5,
            "mana_regen":5,
            "ultimate_damage":15,
            "gamestage": 0,
            "inventory": {}
        }
    }
}
default_weapons = {"weapons": {}}
default_armors = {"armors": {}}
default_utilities = {"utilities": {}}

characters = load_json('characters.json', default_characters)
weapons = load_json('weapon.json', default_weapons)
armors = load_json('armor.json', default_armors)
utilities = load_json('utilities.json', default_utilities)

# Utility functions for writing text and JSON
def write(text):
    """Prints text character by character for a typewriter effect."""
    for char in text:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

def write_json(file, data, sort=False):
    """Writes data to JSON file with optional sorting."""
    with open(file, "w") as json_files:
        json.dump(data, json_files, indent=2, sort_keys=sort)

def choose_monster() :
    global monster
    if zone == "Desert":
        monster = random.choice(["Giant Scorpio","Bandit","Sand Elemental","Sand Golem"])
        if monster == "Giant Scorpio":
            monster = Monster("Giant Scorpio",25,12,10,125)
        if monster == "Bandit":
            monster = Monster("Bandit",20,28,5,70)
        if monster == "Sand Elemental":
            monster = Monster("Sand Elemental",30,10,30,60)
        if monster == "Sand Golem":
            monster = Monster("Sand Golem",70,20,0,0)
    else:
        print("Sorry, the mounsters went on vacation, there's not any in the code")
    return monster

def display_fight():
        print(f'\r{monster.name}', end='', flush=True)
        print("{:>12}".format(player.name))
        print(f'\rHp: {monster.hp}', end='', flush=True)
        print("{:>19}".format(f'Hp:{player.health}'))
        print(f'\rDmg: {monster.damage}', end='', flush=True)
        print("{:>19}".format(f"Dmg: {player.damage}"))
        print(f'\rMr: {monster.mana_regen}', end='', flush=True)
        print("{:>19}".format(f"Mr: {player.mana_regen}")) 
        print(f'\rUlt: {monster.ultimate_damage}', end='', flush=True)
        print("{:>19}".format(f"Ult: {player.ultimate_damage}"))
# Character management functions
def update_character(category, data):
    """Updates character attributes and writes them to the JSON file."""
    characters["characters"][selection][category] = data
    write_json("characters.json", characters)

# Player class to represent the selected character
class Player:
    def __init__(self, name, race, gold, inventory, level, health, damage, mana_regen, ultimate_damage, game_stage):
        self.name = name
        self.race = race
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.health = health
        self.damage = damage
        self.mana_regen = mana_regen
        self.ultimate_damage = ultimate_damage
        self.game_stage = game_stage


    def update_game_stage(self, new_stage):
        """Updates the player's game stage and writes to character data."""
        self.game_stage = new_stage
        update_character("gamestage", new_stage)
#Monster class

class Monster:
    
    def __init__(self,name,hp,damage,mana_regen,ultimate_damage,loot=None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.mana_regen = mana_regen
        self.ultimate_damage = ultimate_damage
        self.loot = loot

# Function to select a character from the JSON file
def select_character():
    """Allows user to select a character, loading data into a Player instance."""
    global player, selection
    try:
        print("Available Characters:")
        for name, character in characters["characters"].items():
            for attr, value in character.items():
                if attr == "inventory":
                    print(f'{attr}: {value.keys()}')
                else:
                    print(f"{attr}: {value}")
            print("-------------------------------")

        selection = input("Choose a character by name: ")
        character = characters["characters"][selection]
        player = Player(
            character["name"],
            character["race"],
            character["gold"],
            character["inventory"],
            character["level"],
            character["health"],
            character["damage"],
            character["mana_regen"],
            character["ultimate_damage"],
            character["gamestage"]
        )
    except KeyError:
        print("Character not found. Please try again.")
        select_character()

def fight_action():
    action = input("1: Strike,      2: Ultimate      3: Use Items     4: Run        5:Cry")
    if action == "1":
        print("")
    if action == "2":
        print("")
    if action == "3":
        print("")
    if action == "4":
        print("")
    if action == "5":
        print("You are effectively useless\n----------------------------")
        fight_action()

# Game stages and functions
def combat():
    monster = choose_monster()
    write(f"You got ambushed by a {monster.name}, fight it\n"+" ")
    display_fight()
    print("-----------------------")
    fight_action()

def welcome():
    """Displays welcome message."""
    print("-------------------------------")
    write("Welcome to Seven Dragon's War\n(Thanks to GentleEgo for the help, he's a real goat)\n")
    print("-------------------------------")
    time.sleep(1)

def menu():
    """Displays menu for character selection or creation."""
    while True:
        menu_choice = input("Type 1 to select an existing character or 2 to create a new character: ")
        if menu_choice == '1':
            select_character()
            break
        elif menu_choice == '2':
            print("Character creation not available yet.")
        else:
            print("Please enter a valid option.")

def intro():
    """Displays character information and storyline intro."""
    write(f'CHARACTER SELECTED:\nname: {player.name}\nrace: {player.race}\ngold: {player.gold}\ninventory: {player.inventory}\n')
    write("A long time ago there were 8 dragon siblings, sons of Amaralia the being above all\nThey decided together to live in a temperate planet called Earth. They all claimed a territory and stayed there for a while. The power emanating from these godly being bringed life to the lands. A large variety of intelligent and non intelligent beings came to life. At this point, the godess came to visit her children. Sadly her power was too great for the creatures that the dragons were raising. The brothers discussed for a long time and concluded that their mother needed to go. Zul'Sahar, the oldest sister ,drakaina of darkness, managed to create a powerful artifact that drained Amaralia's power. With this ,she managed to kill the godess and a period of peace came. However, everything must come to an end. Blinded by the artficat's power, Zul'Sahar attacked her 7 siblings one by one. Fortunately they managed to mortally injure her and peace came once again. The dragon's influence changed the world once again by manifesting 'mana' a new energy form. This stopped military advancement,letting people fight with mainly sword, spear and bows. Unfortunately , Zul'Sahar made her return many centuries later by making a new race entirely by herself. The corruption's adept, this new race had the power to shapeshift and spread a mental illness called corruption that enslaved people to the darkness drakaina. After infiltrating each country's governement. Zul'Sahar invaded all nations, forcing the other dragons to retreat. Before having to leave their physical body, each dragon manifested a part of their soul in being resistant to the corruption. Furthermore, Athul, the dragon of light, manage to create Light's Altar that could repulse the corruption once activated. He didn't have the time to activate them however . The dragons teleported their incarnations in Runar, the farthest mountain from Zul'Sahar's Kingdom where a group of resistant had taken place.\n")
    print("-----------------------------------------------")
    write("The biting wind of Runar whipped at your face, a stark contrast to the warmth of your dragon form. You were no longer the mighty Shar'Gezan, the dragon of sand, but a fragile human, a mere echo of your former power. A flicker of fear, a sensation you hadn't felt in millennia, pricked at your soul. This was a world you'd helped shape, yet now it felt alien, a battlefield you could barely comprehend. A guttural growl ripped through the silence. You turned to see a humanoid wolf, its fur the color of midnight, its eyes burning with an intensity that belied its animalistic form. It was a warrior, you sensed, honed by hardship and battle. You're one of them, the wolf spoke, its voice rough and gravelly. One of the dragon's echoes. You nodded, your voice a mere whisper. I am Shar'Gezan, but I am no longer what I once was. The wolf, Axit, you learned, was the incarnation of Az'nin, the dragon of wind. He had been fighting the corruption for years, his form a testament to the wind's untamed spirit. He regarded you with suspicion, but there was a glimmer of hope in his eyes. A woman, her face etched with the harshness of the mountains, stepped out from behind Axit. She wore fine silks, a stark contrast to her hardened features. Zorael, the incarnation of the dragon of ice, her power a chilling presence. She held a staff that pulsed with a cold, ethereal light. You have the mark, Zorael said, her voice smooth and melodic. The mark of the dragons. You showed her the faint, shimmering tattoo on your wrist, the mark of your dragon soul. We've been expecting you, Axit said, his gaze fierce. The whispers say you are the key to defeating Zul'Sahar. You felt a surge of hope, a flicker of the power you'd lost. Perhaps, even in this weakened form, you could help. We need to reach the Light's Altar, Zorael said, her eyes fixed on you. It is our only hope.Axit nodded, his gaze fierce. The corruption is spreading, but we must fight. We must activate the Altar before it's too late. But first, we must gather equipement and train before attacking Al'Banhera, the capital of Shar'Gezan's desert. Come, some people have establisted a market nearby")
    player.update_game_stage(1)
    main()

def display_shop(items, item_type):
    """Displays items available in a shop and manages item purchases."""
    for item, details in items.items():
        if details["level_required"] <= player.level:
            print(f"{item}:")
            for attr, value in details.items():
                print(f"  {attr}: {value}")
            print("-------------------------------")

    item_choice = input("Enter the name of the item you want (or leave blank to pass): ").strip()
    if item_choice in items and items[item_choice]["price"] <= player.gold:
        # Deduct gold and update inventory
        player.gold -= items[item_choice]["price"]
        update_character("gold", player.gold)
        player.inventory[item_choice] = items[item_choice]
        update_character("inventory", player.inventory)
        print(f"{item_choice} purchased!")
    else:
        print("You don't have enough gold or the item was not found.")
        
def shop():
    """Manages the shop menu for purchasing items."""
    while True:
        write("Which shop would you like to visit?\n1: Weapon Shop\n2: Armor Shop\n3: Utilities Shop\n4: Leave Market")
        choice = input("Enter the number of your choice: ").strip()
        if choice == '1':
            display_shop(weapons["weapons"], "Weapon")
        elif choice == '2':
            display_shop(armors["armors"], "Armor")
        elif choice == '3':
            display_shop(utilities["utilities"], "Utility")
        elif choice == '4':
            print(f"Inventory: {player.inventory.keys}\nGold: {player.gold}")
            if input("Are you sure you want to leave? (y/n): ").lower() == 'y':
                player.update_game_stage(2)
                main()
        else:
            print("Please enter a valid option.")

def journey_to_Albanhera():
    if (not player.inventory) == True:
        write("Why did you choose to leave the market naked you weirdo")
        player.update_game_stage(1)
        exit()
    combat()

def main():
    """Main function to control game flow based on player's game stage."""
    global start
    if start:
        welcome()
        menu()
        start = False

    if player.game_stage == 0:
        intro()
    elif player.game_stage == 1:
        shop()
    elif player.game_stage == 2:
        if not player.inventory == False:
            write("With your new found equipement you go on a journey with Axit and Zorael your two acolytes. Unfortunately it is hard to approach Al'Banhera because Zul'Sahar's guards are killing everyone that isn't corrupted. Some merchants told you that the bandit's chief might know a way to get in.")
            print("-------------------------------------")
        journey_to_Albanhera()

main()