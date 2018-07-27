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

    def __init__(self, name, quality, rarity, price,
                 area, armor, thick, wgt):
        super().__init__(name, quality, rarity, price)

        self.area = area
        self.armor = armor
        self.thick = thick
        self.wgt = wgt


class VPlate(Armor):

    def __init__(self):
        super().__init__(name='Plate', quality=25, rarity=7, price=2700,
                         area='Vitals', armor='Plate', thick=5, wgt=28)


class LPlate(Armor):

    def __init__(self):
        super().__init__(name='Plate', quality=25, rarity=7, price=2500,
                         area='Lower', armor='Plate', thick=5, wgt=31)


class VBrigandine(Armor):

    def __init__(self):
        super().__init__(name='Brigandine', quality=25, rarity=3, price=930,
                         area='Vitals', armor='Brigandine', thick=4, wgt=27)


class LBrigandine(Armor):

    def __init__(self):
        super().__init__(name='Brigandine', quality=25, rarity=4, price=930,
                         area='Lower', armor='Brigandine', thick=4, wgt=29)


class VChainmail(Armor):

    def __init__(self):
        super().__init__(name='Chainmail', quality=25, rarity=4, price=1200,
                         area='Vitals', armor='Chainmail', thick=4, wgt=23)


class LChainmail(Armor):

    def __init__(self):
        super().__init__(name='Chainmail', quality=25, rarity=4, price=1130,
                         area='Lower', armor='Chainmail', thick=4, wgt=26)


class VScale(Armor):

    def __init__(self):
        super().__init__(name='Scale', quality=25, rarity=5, price=900,
                         area='Vitals', armor='Scale', thick=3, wgt=21)


class LScale(Armor):

    def __init__(self):
        super().__init__(name='Scale', quality=25, rarity=6, price=1000,
                         area='Lower', armor='Scale', thick=3, wgt=24)


class VCuirbouilli(Armor):

    def __init__(self):
        super().__init__(name='Cuirbouilli', quality=25, rarity=3, price=450,
                         area='Vitals', armor='Cuirbouilli', thick=2, wgt=6)


class LCuirbouilli(Armor):

    def __init__(self):
        super().__init__(name='Cuirbouilli', quality=25, rarity=4, price=460,
                         area='Lower', armor='Cuirbouilli', thick=2, wgt=8)


class VSLeather(Armor):

    def __init__(self):
        super().__init__(name='Studded Leather', quality=25, rarity=3, price=330,
                         area='Vitals', armor='Nonmetal', thick=2, wgt=8)


class LSLeather(Armor):

    def __init__(self):
        super().__init__(name='Studded Leather', quality=25, rarity=4, price=370,
                         area='Lower', armor='Nonmetal', thick=2, wgt=10)


class VLeather(Armor):

    def __init__(self):
        super().__init__(name='Leather', quality=25, rarity=2, price=100,
                         area='Vitals', armor='Nonmetal', thick=1, wgt=4)


class LLeather(Armor):

    def __init__(self):
        super().__init__(name='Leather', quality=25, rarity=2, price=100,
                         area='Lower', armor='Nonmetal', thick=1, wgt=4)


class VPadded(Armor):

    def __init__(self):
        super().__init__(name='Padded', quality=25, rarity=2, price=70,
                         area='Vitals', armor='Nonmetal', thick=1, wgt=6)


class LPadded(Armor):

    def __init__(self):
        super().__init__(name='Padded', quality=25, rarity=2, price=70,
                         area='Lower', armor='Nonmetal', thick=1, wgt=6)


class Shortsword(Weapon):

    def __init__(self):
        super().__init__(name='Shortsword', quality=25, rarity=5, price=170,
                         speed=40, pen=4, dmg=8, skill=16, strength=13,
                         wgt=3, skill='WEdg')


class Club(Weapon):

    def __init__(self):
        super().__init__(name='Club', quality=25, rarity=1, price=20,
                         speed=45, pen=3, dmg=7, skill=4, strength=16,
                         wgt=5)


class MFlail(Weapon):

    def __init__(self):
        super().__init__(name='Military flail', quality=25, rarity=6, price=160,
                         speed=70, pen=4, dmg=10, skill=14, strength=17,
                         wgt=4)


class SSpear(Weapon):

    def __init__(self):
        super().__init__(name='Short spear', quality=25, rarity=3, price=100,
                         speed=70, pen=3, dmg=9, skill=17, strength=17,
                         wgt=3)


class TKnife(Weapon):

    def __init__(self):
        super().__init__(name='Throwing knife', quality=25, rarity=8, price=40,
                         speed=240, pen=2, dmg=5, skill=30, strength=13,
                         wgt=1)


class SBow(Weapon):

    def __init__(self):
        super().__init__(name='Short bow', quality=25, rarity=3, price=230,
                         speed=150, pen=4, dmg=5, skill=20, strength=16,
                         wgt=6)


class Crossbow(Weapon):

    def __init__(self):
        super().__init__(name='Crossbow', quality=25, rarity=2, price=270,
                         speed=540, pen=6, dmg=7, skill=14, strength=18,
                         wgt=9)