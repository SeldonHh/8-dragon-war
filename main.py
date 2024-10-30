import json
import sys
import time

start = True

with open('weapon.json',"r") as json_files:
    weapons_file = json_files.read()
    weapons_list_json = json.loads(weapons_file)
    weapons_list = weapons_list_json["weapons"]


with open('armor.json',"r") as json_files:
    armor_file = json_files.read()
    armors_list_json = json.loads(armor_file)
    armors_list = armors_list_json["armors"]


with open('utilities.json',"r") as json_files:
    utilities_files = json_files.read()
    utilities_list_json = json.loads(utilities_files)
    utilities_list = utilities_list_json["utilities"]


with open ("characters.json","r") as json_files:
    character_file = json_files.read()
    character_list_json = json.loads(character_file)
    character_list = character_list_json["characters"]


#USEFUL FUNC
def update_character(category,data):
    character_list_json["characters"][selection][category]= data
    write_json("characters.json",character_list_json)


def write(text):
    for char in text:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()


def write_json(file,data,sort=False):
    with open(file,"w") as json_files:
        json_files.write(json.dumps(data,indent=2,sort_keys=sort))
        

class Player:

    def __init__(self,name,race,gold,inventory,level,game_stage):
        self.name = name
        self.race = race
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.game_stage = game_stage


def select_character():
    try:
        global player,selection
        for character in character_list:
            for item,value in character_list[character].items():
                print(item,": ",value)
            print("-------------------------------")
        selection = input("which one do you choose(enter his name)")
        character = character_list[selection]
        player = Player(
            character["name"],
            character["race"],
            character["gold"],
            character["inventory"],
            character["level"],
            character["gamestage"]
            )
    except:
        select_character()



# GAME STAGES
def welcome(): 
    print("-------------------------------")
    write("Welcome to Seven dragon's war\n(Thanks to GentleEgo for the help)\n")
    print("-------------------------------")
    time.sleep(1)


def menu():
    menu_choice = int(input("Type 1 to select an existing character and Type 2 to create a new character "))
    if menu_choice == 1:
        select_character()
    elif menu_choice == 2:
        print("Not available")
        menu()
    else :
        print("enter an available number")
        menu()


def intro():
    write(f'CHARACTER SELECTED:\nname: {player.name}\nrace: {player.race}\ngold: {player.gold}\ninventory: {player.inventory}\n')
    write("A long time ago there were 8 dragon siblings, sons of Amaralia the being above all\nThey decided together to live in a temperate planet called Earth. They all claimed a territory and stayed there for a while. The power emanating from these godly being bringed life to the lands. A large variety of intelligent and non intelligent beings came to life. At this point, the godess came to visit her children. Sadly her power was too great for the creatures that the dragons were raising. The brothers discussed for a long time and concluded that their mother needed to go. Zul'Sahar, the oldest sister ,drakaina of darkness, managed to create a powerful artifact that drained Amaralia's power. With this ,she managed to kill the godess and a period of peace came. However, everything must come to an end. Blinded by the artficat's power, Zul'Sahar attacked her 7 siblings one by one. Fortunately they managed to mortally injure her and peace came once again. The dragon's influence changed the world once again by manifesting 'mana' a new energy form. This stopped military advancement,letting people fight with mainly sword, spear and bows. Unfortunately , Zul'Sahar made her return many centuries later by making a new race entirely by herself. The corruption's adept, this new race had the power to shapeshift and spread a mental illness called corruption that enslaved people to the darkness drakaina. After infiltrating each country's governement. Zul'Sahar invaded all nations, forcing the other dragons to retreat. Before having to leave their physical body, each dragon manifested a part of their soul in being resistant to the corruption. Furthermore, Athul, the dragon of light, manage to create Light's Altar that could repulse the corruption once activated. He didn't have the time to activate them however . The dragons teleported their incarnations in Runar, the farthest mountain from Zul'Sahar's Kingdom where a group of resistant had taken place.\n")
    print("------------------------------------------")
    write("The biting wind of Runar whipped at your face, a stark contrast to the warmth of your dragon form. You were no longer the mighty Shar'Gezan, the dragon of sand, but a fragile human, a mere echo of your former power. A flicker of fear, a sensation you hadn't felt in millennia, pricked at your soul. This was a world you'd helped shape, yet now it felt alien, a battlefield you could barely comprehend. A guttural growl ripped through the silence. You turned to see a humanoid wolf, its fur the color of midnight, its eyes burning with an intensity that belied its animalistic form. It was a warrior, you sensed, honed by hardship and battle. You're one of them, the wolf spoke, its voice rough and gravelly. One of the dragon's echoes. You nodded, your voice a mere whisper. I am Shar'Gezan, but I am no longer what I once was. The wolf, Axit, you learned, was the incarnation of Az'nin, the dragon of wind. He had been fighting the corruption for years, his form a testament to the wind's untamed spirit. He regarded you with suspicion, but there was a glimmer of hope in his eyes. A woman, her face etched with the harshness of the mountains, stepped out from behind Axit. She wore fine silks, a stark contrast to her hardened features. Zorael, the incarnation of the dragon of ice, her power a chilling presence. She held a staff that pulsed with a cold, ethereal light. You have the mark, Zorael said, her voice smooth and melodic. The mark of the dragons. You showed her the faint, shimmering tattoo on your wrist, the mark of your dragon soul. We've been expecting you, Axit said, his gaze fierce. The whispers say you are the key to defeating Zul'Sahar. You felt a surge of hope, a flicker of the power you'd lost. Perhaps, even in this weakened form, you could help. We need to reach the Light's Altar, Zorael said, her eyes fixed on you. It is our only hope.Axit nodded, his gaze fierce. The corruption is spreading, but we must fight. We must activate the Altar before it's too late. But first, we must gather equipement and train before attacking Al'Banhera, the capital of Shar'Gezan's desert. Come, some people have establisted a market nearby")
    update_character("gamestage",1)
    player.game_stage = 1
    main()
        

def shop():
    write("Which shop do you want to go to ?\n1: Kan'Eran's weapon shop\n2: The Runarians Armors\n3: Valen's charms and potions\n4: Leave the market\n")
    choice = input("put the number of the shop ")
    if choice == "1":
        for weapon in weapons_list:
            if weapons_list[weapon]["level_required"] <= player.level:
                print("")
                print(weapons_list[weapon])
                for item,value in weapons_list[weapon].items():
                    print(item,": ",value)
                print("-------------------------------")
        item_choice = input("Enter the name of the object you want (put nothing to pass)")
        try:
            if weapons_list[item_choice]["price"] <= player.gold:
                update_character("gold",player.gold-weapons_list[item_choice]["price"])
                player.gold -= weapons_list[item_choice]["price"]
                update_character("inventory",(character_list[selection]["inventory"],weapons_list[item_choice]),True)
                player.inventory = (character_list[selection]["inventory"],weapons_list[item_choice])
                time.sleep(1)
                shop()
            else:
                print("You don't have enough gold")
                shop()
        except:
            shop()

    elif choice == "2":
        for armor in armors_list:
            if armors_list[armor]["level_required"]<= player.level:
                print("")
                print(armors_list[armor])
                for item,value in armors_list[armor].items():
                    print(item,': ',value)
                print("-------------------------------")
        item_choice = input("Enter the name of the object you want (put nothing to pass)")
        try:
            if armors_list[item_choice]["price"] <= player.gold:
                update_character("gold",player.gold-armors_list[item_choice]["price"])
                player.gold -= armors_list[item_choice]["price"]
                update_character("inventory",(character_list[selection]["inventory"],armors_list[item_choice]),True)
                player.inventory = ((character_list[selection]["inventory"],armors_list[item_choice]))
                time.sleep(1)
                shop()
            else:
                print("You don't have enough gold")
                shop()
        except:
            shop()

    elif choice == "3":
        for utilities in utilities_list:
            if utilities_list[utilities]["level_required"]<= player.level:
                print("")
                print(utilities_list[utilities])
                for item,value in utilities_list[utilities].items():
                    print(item,': ',value)
                print("-------------------------------")
        item_choice = input("Enter the name of the object you want ")
        try:
            if utilities_list[item_choice]["price"] <= player.gold:
                update_character("gold",player.gold-utilities_list[item_choice]["price"])
                player.gold -= utilities_list[item_choice]["price"]
                update_character("inventory",(character_list[selection]["inventory"],utilities_list[item_choice]),True)
                player.inventory = (character_list[selection]["inventory"],utilities_list[item_choice])
                time.sleep(1)
                shop()
            else:
                print("You don't have enough gold")
                shop()
        except:
            shop()

    elif choice == "4":
        print(f"inventory : {player.inventory} \ngold : {player.gold}")
        confirm = input("Are you sure you wanna go ? y/n")
        if confirm == "y":
            time.sleep(1)
            update_character("gamestage",2)
            player.game_stage = 2
            main()
        else:
            shop()

    else:
        print("Put an available number")
        shop()


def main():
    global start
    if start == True:
        welcome()
        menu()
        start = False
    if player.game_stage == 0:
        intro()
    if player.game_stage == 1:
        shop()
    if player.game_stage == 2:
        print("hola")
main()