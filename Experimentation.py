import random 


def PlayerDmgCalc(CurrentPlayerHealth, EnemyPower):
    CurrentPlayerHealth -= 





CurrentPlayerHealth = 100
MaxPlayerHealth = 100
GoblinHealth = 30
DragonHealth = 200
HasGoblinSword = False
Inventory = ["Standard Health Potion (heal 20 HP)", "Super Health Potion (heal 50 HP)"]



TurnNumber = 1
print ("A goblin has attacked you!")
for i in range (0,19):
    if GoblinHealth > 0:
        print("\n\nTurn Number: ", TurnNumber, "\nPress 1 to Attack \nPress 2 to use an item \nPress 3 to exit the game")
        Action = input()
        if Action == "1":
            print ("You attacked the Goblin!")
            GoblinHealth -= 5 
            if GoblinHealth <= 0:
                   print ("Goblin defeated! You have gained the goblin sword.")
                   HasGoblinSword = True
            else:
                MissRate = random.randint(1,10)
                if MissRate > 8:
                    print ("You missed your attack!")
                else:
                    print ("Goblin has lost 5 HP! Goblin has ", GoblinHealth, "remaining.")

        elif Action == "2":
            print ("What item would you like to use?")
            itemID = 0
            #if len(Inventory) == 0:
            #    print ("You have no items!")
            for item in Inventory:
                print ("Press ", itemID + 1, " to use ",Inventory[itemID])
                itemID += 1
            print ("Press ", itemID + 1, "to go back")
            Action = int(input())
            if Action == 1:
                if (CurrentPlayerHealth + 20) > MaxPlayerHealth:
                    CurrentPlayerHealth = MaxPlayerHealth
                else:
                    CurrentPlayerHealth += 20
                print ("You used a potion and regenerated 20 health! You now have ", CurrentPlayerHealth)
            elif Action == 2:
                if (CurrentPlayerHealth + 50) > MaxPlayerHealth:
                    CurrentPlayerHealth = MaxPlayerHealth
                else:
                    CurrentPlayerHealth += 50
                print ("You used a super potion and regenerated 50 health! You now have ", CurrentPlayerHealth)

        elif Action == "3":
            print("you have left the game")
            quit()
        else: 
            print("Why on earth would you not press what i told you")


    #GoblinTurn
    print ("\nThe goblin attacked you for 8 damage!")
    CurrentPlayerHealth -= 8
    if CurrentPlayerHealth <= 0:
        print ("You died!")
        quit()
    else:
        print ("Player health: ", CurrentPlayerHealth, "/", MaxPlayerHealth)

    TurnNumber += 1
   
