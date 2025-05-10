class Pokemon:
    def __init__(self, name, type, hp, attack, defense, special_attack, special_defense, speed):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def __str__(self):
        return self.name

pokemon = Pokemon("Sobble", "Water", 35, 55, 40, 50, 50, 90)

print(pokemon)