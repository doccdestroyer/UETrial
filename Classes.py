

class PartyMember():
    def __init__(self):
        self.max_health = 100
        self.max_mana = 30
        self.exp_to_level_up = 100
        self.health_potion_strength = 20


        self.stats = {
            "name" : "hero",
            "strength": 5,
            "health": 100,
            "mana": 30,
            "exp": 0,
            "level": 0,
        }
        self.inventory = ["health potion","super potion","fire potion", "hearty carrot"]

    def print_stats(self):
        print("Current Stats: ")
        for key, value in self.stats.items():
            print(f"{key}:{value}")

    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    def move(self):
        pass

    def attack(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"Your health has decreased to {self.stats['health']}")
    
    def heal(self,item_name):
        if (self.inventory.count("health potion") <= 0):
            print (f"You don't have any {item_name}")
            return
        # make item name check for a/an depedning on the letter, if first letter is vowel use an not a
        print (f"You've used a {item_name} you've restored {self.health_potion_strength} health")
        self.stats["health"] += self.health_potion_strength

        if (self.stats["health"] >= self.max_health):
            print(f"You've fully restored your health to {self.max_health}")
            self.stats["health"] = self.max_health
        else:
            print (f"Your health is now {self.stats['health']}")
        self.inventory.remove("health potion")

    def use_item(self):
        pass

class Enemy():
    def __init__(self):
        self.max_health = 30
        
        self.stats = {
            "name": "enemy",
            "health": 30,
            "strength": 10,
            "level": 1,
            "status_ailment": "null"
        }

        def attack(self):
            pass
        def take_damage():
            pass
        def heal_self():
            pass


     
#def heal_user(item):
        
    #    print ("player has been healed")
   #     user = user +  heal_potency
   #     return effect

def heal_user(user, heal_potency):
    def effect():
        user.stats["health"] += heal_potency
        print(f"{user.stats['name']} healed by {heal_potency} HP.")
    return effect

def harm_enemy(target, damage):
    def effect():
        target.stats["health"] -= damage
        print (f"You dealt {damage} damage to the enemy. The enemy has {target.stats['health']} HP remaining")
    return effect
def increase_max_stat():
    
    pass

class Item():
    def __init__(self, name, quantity, effect, description):
        self.name = name
        self.quantity = quantity
        self.effect = effect
        self.description = description

    def use_item(self):
        if self.quantity > 0:
            self.effect()
            self.quantity -= 1
        else:
            print ("somehow you have access this code i genuienly dont know how")

character1 = PartyMember() 
character1.set_name("Felix")
character1.stats["health"] = 100
character1.stats["mana"] = 25
character1.print_stats()
print("\n")
    
potion = Item(name = "Health Potion", quantity = 3, effect = heal_user(character1, 10), description= "Heal self for 10 HP")
potion.use_item()
print(potion.quantity)
print (character1.stats["health"])

Goblin = Enemy()
Goblin.stats["name"] = "Goblin"
Goblin.stats["health"] = 30
Goblin.stats["strength"] = 8
fire_potion = Item(name = "Fire Potion", quantity = 1, effect = harm_enemy(Goblin, 20), description= "Deal 20 dmg to the enemy")

fire_potion.use_item()
print (Goblin.stats["health"])


        
