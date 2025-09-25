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


from Classes import PartyMember
from Classes import Enemy
from Classes import Item
from Classes import heal_user


is_in_combat = True
Action = 0

character1 = PartyMember() 
character1.set_name("Felix")
character1.stats["health"] = 100
character1.stats["mana"] = 25
character1.print_stats()
print("\n")

potion = Item(name = "Health Potion", quantity = 3, effect = heal_user(character1, 20), description= "Heal self for 30 HP")
super_potion = Item(name = "Super Potion", quantity = 3, effect = heal_user(character1, 30), description= "Heal self for 30 HP")
#TODO define fire potion and heart carrot




InventoryItems = ["Standard Health Potion (heal 20 HP)", "Super Health Potion (heal 50 HP)"]

PlayerDamage = 5
CurrentPlayerHealth = 100
MaxPlayerHealth = 100
MaxGoblinHealth = 30
MaxDragonHealth = 200
HasGoblinSword = False
EnemyHealth = 0
EnemyPower = 99
EnemyName = "undefined"



Inventory = {
    potion.name: potion.quantity,
    super_potion.name: super_potion.quantity,
    "Fire Potion": 2,
    "Hearty Carrot" : 1,
}
    
def ChooseEnemy():
    if random.randint(0,2) == 1:
        EnemyHealth = MaxGoblinHealth
        EnemyName = "Goblin"
        EnemyPower = 5
    else:
        EnemyHealth = MaxDragonHealth
        EnemyName = "Dragon"
        EnemyPower = 10
    return (EnemyName, EnemyHealth, EnemyPower)


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
        InventoryItems.append(("Fire Potion - deals 10 damage, inflicts burn - " + str(Inventory["Fire Potion"]) + " remaining"))
    if Inventory["Hearty Carrot"] > 0:
        InventoryItems.append(("Hearty Carrot - increase max mana by 5 - "+ str(Inventory["Hearty Carrot"]) + " remaining"))
    return InventoryItems

def UseItem():
    pass


if random.randint(0,2) == 1:
    EnemyHealth = MaxGoblinHealth
    EnemyName = "Goblin"
    EnemyPower = 5
else:
    EnemyHealth = MaxDragonHealth
    EnemyName = "Dragon"
    EnemyPower = 10
#return (EnemyName, EnemyHealth, EnemyPower)

def MainMenu():
    print("\n\nTurn Number: ", TurnNumber, "\nPress 1 to Attack \nPress 2 to use an item \nPress 3 to exit the game")
    Action = input()
    return Action

def PlayerAction():
    pass

print ("You have encountered a ", EnemyName, "! \nThe ", EnemyName," has engaged you in combat")
TurnNumber = 1
print ("A ",EnemyName, " has attacked you!")
while is_in_combat == True:
    if EnemyHealth > 0:
        Action = MainMenu()
        if Action == "1":
            print ("You attacked the ", EnemyName, "!")
            EnemyHealth = DamageCalc(EnemyHealth,PlayerDamage)
            if EnemyHealth <= 0:
                    print (EnemyName, " has been defeated!")
                    if EnemyName == "Goblin":
                        HasGoblinSword = True
                        PlayerDamage = 10
                    is_in_combat = False
                    break
            else:
                MissRate = random.randint(1,10)
                if MissRate > 8:
                    print ("You missed your attack!")
                else:
                    print (EnemyName, " has lost 5 HP!  has ", EnemyHealth, "remaining.")

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
                if CurrentPlayerHealth == MaxPlayerHealth:
                    print ("You already have full health!")
                    MainMenu()
                elif (CurrentPlayerHealth + 20) > MaxPlayerHealth:
                    potion.use_item()
                    CurrentPlayerHealth = MaxPlayerHealth
                    #Inventory["Health Potion"] -= 1
                    print ("You used a potion and regenerated 20 health! You now have ", CurrentPlayerHealth)
                else:
                    potion.use_item()
                    print ("You used a potion and regenerated 20 health! You now have ", CurrentPlayerHealth)

            elif Action == 2:
                if CurrentPlayerHealth == MaxPlayerHealth:
                    print ("You already have full health!")
                elif (CurrentPlayerHealth + 50) > MaxPlayerHealth:
                    CurrentPlayerHealth = MaxPlayerHealth
                    Inventory["Super Potion"] -= 1
                    print ("You used a super potion and regenerated 50 health! You now have ", CurrentPlayerHealth)
                else:
                    CurrentPlayerHealth += 50
                    Inventory["Super Potion"] -= 1
                    print ("You used a super potion and regenerated 50 health! You now have ", CurrentPlayerHealth)
            elif Action == 3:
                EnemyHealth = DamageCalc(EnemyHealth,20)
                Inventory["Fire Potion"] -= 1

                print (f"You threw a fire potion! Enemy now has {EnemyHealth}")
            elif Action == 4:
                character1.stats["mana"] += 5
                character1.max_mana += 5
                Inventory["Hearty Carrot"] -= 1
                print(f"You increased your max mana to {character1.max_mana}. You have {character1.stats["mana"]} mana remaining.")
            elif Action == 5:
                MainMenu()


        elif Action == "3":
            print("GAME OVER")
            quit()
        else:
            pass
            #return to main menu



    #Enemy Turn
    print ("\nThe ", EnemyName, " attacked you for 8 damage!")
    CurrentPlayerHealth = DamageCalc(CurrentPlayerHealth, EnemyPower)

    if CurrentPlayerHealth <= 0:
        print ("You died!")
        quit()
    else:
        print ("Player health: ", CurrentPlayerHealth, "/", MaxPlayerHealth)


    TurnNumber += 1
   


