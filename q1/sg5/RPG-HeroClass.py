class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def damage_taken(self, amount):
        self.hp = self.hp - amount

arthur =  Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.damage_taken(10)

print("Arthur HP:", arthur.hp)
print("Morgana HP:", morgana.hp)
