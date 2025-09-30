#TODO 
#1 - fix item inventory buttons so order is always correct regardless of item value being 0
#2 - add mana and spells into the main code
#3 - translate mana/spells into classes
#4 - add second party member
#5 - add grid and movement options
#6 - add exp leveling up system
#7 - probability for enemies to drop items
#8 - add brave/defaulting
#9 - explain brave'defualting in a ui pop up
#10 - add burning ailment to enemies, -2 health at the end of their turn




import random


from Classes import *


is_in_combat = True
Action = 0
MissRate = 0

character1 = PartyMember() 
character1.set_name("Felix")
character1.max_health = 100
character1.stats["health"] = 100
character1.stats["strength"] = 10
character1.stats["mana"] = 25
character1.print_stats()
print("\n")

current_character = character1

character2 = PartyMember() 
character2.set_name("Cyrus")
character2.stats["health"] = 80
character2.max_health = 80
character1.stats["strength"] = 8
character2.stats["mana"] = 40
character2.print_stats()
print("\n")




def PickEnemy():
    if random.randint(0,2) == 1:
        current_enemy = Enemy()
        current_enemy.max_health = 30
        current_enemy.stats["name"] = "Goblin"
        current_enemy.stats["health"] = 30
        current_enemy.stats["strength"] = 8
    else:

        current_enemy = Enemy()
        current_enemy.max_health = 100
        current_enemy.stats["name"] = "Dragon"
        current_enemy.stats["health"] = 100
        current_enemy.stats["strength"] = 15
    return (current_enemy, current_enemy.max_health, current_enemy.stats)

current_enemy, current_enemy.max_health, current_enemy.stats = PickEnemy()



potion = Item(name = "Health Potion", quantity = 3, effect = heal_user(character1, 20), description= "Heal self for 30 HP")
super_potion = Item(name = "Super Potion", quantity = 3, effect = heal_user(character1, 30), description= "Heal self for 30 HP")
fire_potion = Item(name= "Fire Potion", quantity = 1, effect = harm_enemy(current_enemy, 20), description= "Deal 20 dmg to the enemy")
#TODO define fire potion and heart carrot





InventoryItems = []


Inventory = {
    potion.name: potion.quantity,
    super_potion.name: super_potion.quantity,
    fire_potion.name: fire_potion.quantity,
    "Hearty Carrot" : 1,
}

InventoryTest = {}
    

def DamageCalc(attacked, attackerStregnth):
    return (attacked - attackerStregnth)


def ChooseEnemy():
    pass

def BeginEncounter():
    pass

def EnemyTurn():
    pass

def SortInventory(Inventory):
    InventoryItems = []
    if potion.quantity > 0:
       InventoryItems.append((f"{potion.name} - {potion.description} - {potion.quantity} remaining"))
    if Inventory["Super Potion"] > 0:
       InventoryItems.append((f"{super_potion.name} - {super_potion.description} - {super_potion.quantity} remaining"))
    if Inventory["Fire Potion"] > 0:
        InventoryItems.append((f"{fire_potion.name} -{fire_potion.description} - {fire_potion.quantity} remaining"))
    if Inventory["Hearty Carrot"] > 0:
        InventoryItems.append(("Hearty Carrot - increase max mana by 5 - "+ str(Inventory["Hearty Carrot"]) + " remaining"))
    return InventoryItems

def MainMenuDecision():
    print("\n\nTurn Number: ", TurnNumber, "\nPress 1 to Attack \nPress 2 to use an item \nPress 3 to exit the game")
    Action = input()
    return Action

def TurnResponse():
    if Action == "1":
        print ("You attacked the ", current_enemy.stats["name"], "!")
        current_enemy.stats["health"] = DamageCalc(current_enemy.stats["health"],current_character.stats["strength"])
        if current_enemy.stats["health"] <= 0:
            print (current_enemy.stats["name"], " has been defeated!")
            is_in_combat = False
            quit()

        MissRate = random.randint(1,10)
        if MissRate > 8:
                print ("You missed your attack!")
        else:
            print (f"{current_enemy.stats["name"]} has lost {current_character.stats["strength"]} HP!  has ", current_enemy.stats["health"], "remaining.")

    elif Action == "2":
        character1.stats, current_item, current_item.quantity = ItemMenu()

    elif Action == "3":
        print("GAME OVER")
        quit()
    else:
        pass
        #return to main menu
    current_item = potion
    current_item.quantity = potion.quantity
    return (current_character.stats, current_enemy.stats, current_item, current_item.quantity)

def ItemMenu():
    print ("What item would you like to use?")
    InventoryItems = SortInventory(Inventory)
    itemID = 0
    if len(Inventory) == 0:
        print ("You have no items!")
    for item in InventoryItems:
        print ("Press ", itemID + 1, " to use ",InventoryItems[itemID])
        itemID += 1
    print ("Press ", itemID + 1, "to go back")
    Action = (input())
    if Action == "1":
        current_item = potion
        if current_character.stats["health"] == current_character.max_health:
            print ("You already have full health!")
            MainMenuDecision()
        elif (current_character.stats["health"] + 20) > current_character.max_health:
            potion.use_item()
            current_character.stats["health"] = current_character.max_health
            print ("You used a potion and regenerated 20 health! You now have ", current_character.stats["health"])
        else:
            potion.use_item()
            print ("You used a potion and regenerated 20 health! You now have ", current_character.stats["health"])
        return (current_character.stats, current_item,current_item.quantity)


    elif Action == "2":
        current_item = super_potion
        if current_character.stats["health"] == current_character.max_health:
            print ("You already have full health!")
        elif (current_character.stats["health"] + 30) > current_character.max_health:
            super_potion.use_item()
            current_character.stats["health"] = current_character.max_health
            print ("You used a super potion and regenerated 30 health! You now have ", current_character.stats['health'])
        else:
            super_potion.use_item()
            print ("You used a super potion and regenerated 30 health! You now have ", current_character.stats['health'])
        return (current_character.stats, current_item,current_item.quantity)


    elif Action == "3":
        current_item = fire_potion
        print (f"You used a fire potion and dealt 20 health! The {current_enemy.stats["name"]} now has {current_enemy.stats["health"]}")
        fire_potion.use_item()
        if current_enemy.stats["health"] <= 0:
            print (f"You defeated the {current_enemy.stats["name"]}!")
        return (current_character.stats, current_item,current_item.quantity)

    elif Action == "4":
        current_character.stats["mana"] += 5
        current_character.max_mana += 5
        Inventory["Hearty Carrot"] -= 1
        print(f"You increased your max mana to {current_character.max_mana}. You have {current_character.stats['mana']} mana remaining.")
        #TODO
        #return (character1.stats, current_item,current_item.quantity)

    elif Action == "5":
        MainMenuDecision()
   

print (f"You have encountered a {current_enemy.stats['name']}! \nThe {current_enemy.stats['name']} has engaged you in combat")
TurnNumber = 1
print ("A ", current_enemy.stats['name'], " has attacked you!")
while is_in_combat == True:
    #character 1 turn
    print(f"\nIt is {current_character.stats['name']}'s turn")
    current_character = character1
    current_character.stats = character1.stats
    current_character.max_health = character1.max_health
    Action = MainMenuDecision()
        #return (character1.stats, current_enemy.stats, HasGoblinSword, current_item, current_item.quantity)
    current_character.stats, current_enemy.stats, current_item, current_item.quantity = TurnResponse()

    print(f"\nIt is {current_character.stats['name']}'s turn")

    current_character = character2
    current_character.stats = character2.stats
    current_character.max_health = character2.max_health
    Action = MainMenuDecision()
    character2.stats, current_enemy.stats, current_item, current_item.quantity = TurnResponse()


#CHANGE FROM 8 TO VERSTAILE CHANGE CHANGE CHANGE CHANGE
#Enemy Turn
    if random.randint(0,2):
        target_character = character1
        target_character.stats = character1.stats
        target_character.max_health = character1.max_health
    else: 
        target_character = character2
        target_character.stats = character2.stats
        target_character.max_health = character2.max_health

    print (f"\nThe {current_enemy.stats["name"]} attacked {target_character.stats["name"]} for {current_enemy.stats["strength"]} damage!")
    target_character.stats["health"] = DamageCalc(target_character.stats["health"], current_enemy.stats["strength"])

    if character1.stats["health"] <= 0:
        print ("You died!")
        quit()
    else:
        print (f"{target_character.stats["name"]} health: {target_character.stats["health"]}/{ target_character.max_health}")


    TurnNumber += 1
    
