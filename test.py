
current_health = 500
def healthAddition (baseHealth,HealthIncrememnt):
    return (baseHealth + HealthIncrememnt)


dictionary = {
    "potion" : (healthAddition(current_health,10), 10),
    "superPotion" : healthAddition (current_health,20)
}

current_health = dictionary["potion"][1]

print(current_health)


