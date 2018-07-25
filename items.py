class Item:

    def __init__(self, name, quality, rarity, price):
        self.name = name
        self.quality = quality
        self.rarity = rarity
        self.price = price


class Weapon(Item):

    def __init__(self, name, speed, pen, dmg, skill, strength, wgt,
                 quality, rarity, price):
        super().__init__(name, quality, rarity, price)

        self.speed = speed
        self.pen = pen
        self.dmg = dmg
        self.skill = skill
        self.strength = strength
        self.wgt = wgt

class Armor(Item):

    def __init(self, thick, wgt):
        super().init__()

class Shortsword25(Weapon):

    def __init__(self):
        super().__init__(name='Shortsword', quality=25, rarity=5, price=170,
                         speed=40, pen=4, dmg=8, skill=16, strength=13,
                         wgt=3)
