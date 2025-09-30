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

HasGoblinSword = False


import random


from Classes import *


is_in_combat = True
Action = 0

character1 = PartyMember() 
character1.set_name("Felix")
character1.max_health = 100
character1.stats["health"] = 100
character1.stats["mana"] = 25
character1.print_stats()
print("\n")



character2 = PartyMember() 
character2.set_name("Cyrus")
character2.stats["health"] = 80
character2.max_health = 80
character2.stats["mana"] = 40
character2.print_stats()
print("\n")


#CurrentPlayerHealth = 100
#MaxPlayerHealth = 100
#MaxGoblinHealth = 30
#MaxDragonHealth = 200
HasGoblinSword = False
#EnemyHealth = 100
#EnemyPower = 99
#EnemyName = "undefined"

if random.randint(0,2) == 1:
    #EnemyHealth = MaxGoblinHealth
    #EnemyName = "Goblin"
    #EnemyPower = 5
    current_enemy = Enemy()
    current_enemy.max_health = 30
    current_enemy.stats["name"] = "Goblin"
    current_enemy.stats["health"] = 30
    current_enemy.stats["strength"] = 8
else:
    #EnemyHealth = MaxDragonHealth
    #EnemyName = "Dragon"
    #EnemyPower = 10
    current_enemy = Enemy()
    current_enemy.max_health = 100
    current_enemy.stats["name"] = "Dragon"
    current_enemy.stats["health"] = 100
    current_enemy.stats["strength"] = 15



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
    
# def ChooseEnemy():
#     if random.randint(0,2) == 1:
#         EnemyHealth = MaxGoblinHealth
#         EnemyName = "Goblin"
#         EnemyPower = 5
#     else:
#         EnemyHealth = MaxDragonHealth
#         EnemyName = "Dragon"
#         EnemyPower = 10
#     return (EnemyName, EnemyHealth, EnemyPower)


def DamageCalc(attacked, attackerStregnth):
    return (attacked - attackerStregnth)


def ChooseEnemy():
    pass

def BeginEncounter():
    pass

def PlayerTurn():
    pass
def UseItem():
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

def UseItem():
    pass




def MainMenu():
    print("\n\nTurn Number: ", TurnNumber, "\nPress 1 to Attack \nPress 2 to use an item \nPress 3 to exit the game")
    Action = input()
    return Action

def PlayerAction():
    pass

print ("You have encountered a ", current_enemy.stats['name'], "! \nThe ", current_enemy.stats['name']," has engaged you in combat")
TurnNumber = 1
print ("A ", current_enemy.stats['name'], " has attacked you!")
while is_in_combat == True:
    if current_enemy.stats["health"] > 0:
        Action = MainMenu()
        if Action == "1":
            print ("You attacked the ", current_enemy.stats["name"], "!")
            current_enemy.stats["health"] = DamageCalc(current_enemy.stats["health"],current_enemy.stats["strength"])
            if current_enemy.stats["health"] <= 0:
                    print (current_enemy.stats["name"], " has been defeated!")
                    if current_enemy.stats["name"] == "Goblin":
                        HasGoblinSword = True
                        current_enemy.stats["strength"] = 15
                        print("You have gained the goblin sword! Your attack damage has increased to 10.")
                    is_in_combat = False
                    break
            else:
                MissRate = random.randint(1,10)
                if MissRate > 8:
                    print ("You missed your attack!")
                else:
                    print (current_enemy.stats["name"], " has lost 5 HP!  has ", current_enemy.stats["health"], "remaining.")

        elif Action == "2":
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
                if character1.stats["health"] == character1.max_health:
                    print ("You already have full health!")
                    MainMenu()
                elif (character1.stats["health"] + 20) > character1.max_health:
                    potion.use_item()
                    character1.stats["health"] = character1.max_health
                    #Inventory["Health Potion"] -= 1
                    print ("You used a potion and regenerated 20 health! You now have ", character1.stats["health"])
                else:
                    potion.use_item()
                    print ("You used a potion and regenerated 20 health! You now have ", character1.stats["health"])

            elif Action == "2":
                if character1.stats["health"] == character1.max_health:
                    print ("You already have full health!")
                elif (character1.stats["health"] + 50) > character1.max_health:
                    character1.stats["health"] = character1.max_health
                    Inventory["Super Potion"] -= 1
                    print ("You used a super potion and regenerated 50 health! You now have ", character1.stats['health'])
                else:
                    character1.stats["health"] += 50
                    Inventory["Super Potion"] -= 1
                    print ("You used a super potion and regenerated 50 health! You now have ", character1.stats['health'])
            elif Action == "3":
                print ("YOU USED FIRE")
                breakpoint
                fire_potion.use_item()

                print (f"You threw a fire potion! Enemy now has {current_enemy.stats['health']}")
            elif Action == "4":
                character1.stats["mana"] += 5
                character1.max_mana += 5
                Inventory["Hearty Carrot"] -= 1
                print(f"You increased your max mana to {character1.max_mana}. You have {character1.stats['mana']} mana remaining.")
            elif Action == "5":
                MainMenu()
            else: 
                print ("other input detected. try again")
                MainMenu()



        elif Action == "3":
            print("GAME OVER")
            quit()
        else:
            pass
            #return to main menu



    #Enemy Turn
    print ("\nThe ", current_enemy.stats["name"], " attacked you for 8 damage!")
    character1.stats["health"] = DamageCalc(character1.stats["health"], current_enemy.stats["strength"])

    if character1.stats["health"] <= 0:
        print ("You died!")
        quit()
    else:
        print ("Player health: ", character1.stats["health"], "/", character1.max_health)


    TurnNumber += 1
   


