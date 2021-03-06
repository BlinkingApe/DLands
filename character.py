from orderedcounter import OrderedCounter

import occupations

import items


class Character:
    """ to do"""

    # Initializer
    def __init__(self, name, gender, family):

        self.is_alive = True

        self.name = name
        self.age = 15
        self.gender = gender
        self.family = family
        self.occupations = []  # list of held occupations
        self.saints = []  # list of known saints
        self.recipes = []  # list of known recipes
        self.attributes = {}  # dict of attributes
        self.skills = {}  # dict of skills
        self.inv = OrderedCounter()  # inventory of items

        if self.gender == 'male':  # give default male attributes
            self.attributes = {'End': 13, 'Str': 16, 'Agl': 12,
                               'Per': 13, 'Int': 12, 'Chr': 12,
                               'DF': 0, 'EP': 0}
        else:  # give default female attributes
            self.attributes = {'End': 15, 'Str': 13, 'Agl': 12,
                               'Per': 13, 'Int': 12, 'Chr': 13,
                               'DF': 0, 'EP': 0}

        if self.family == 'noble':  # give family attributes and skills
            self.mod_attribute('EP', 89)

            self.skills = {'wEdg': 5, 'wImp': 4, 'wFll': 1, 'wPol': 4,
                           'wThr': 0, 'wBow': 4, 'wMsD': 0, 'Alch': 2,
                           'Relg': 5, 'Virt': 2, 'SpkC': 4, 'SpkL': 2,
                           'R&W': 2, 'Heal': 0, 'Artf': 0, 'Stlh': 1,
                           'StrW': 0, 'Ride': 3, 'WdWs': 1}

        elif self.family == 'wealthy urban':
            self.mod_attribute('End', -1)
            self.mod_attribute('Per', 1)
            self.mod_attribute('Int', 1)
            self.mod_attribute('EP', 90)

            self.skills = {'wEdg': 4, 'wImp': 3, 'wFll': 0, 'wPol': 3,
                           'wThr': 0, 'wBow': 0, 'wMsD': 3, 'Alch': 2,
                           'Relg': 5, 'Virt': 1, 'SpkC': 5, 'SpkL': 1,
                           'R&W': 5, 'Heal': 1, 'Artf': 1, 'Stlh': 1,
                           'StrW': 2, 'Ride': 2, 'WdWs': 0}

        elif self.family == 'town trades':
            self.mod_attribute('End', -1)
            self.mod_attribute('Str', -1)
            self.mod_attribute('Per', 1)
            self.mod_attribute('Int', 2)
            self.mod_attribute('EP', 93)

            self.skills = {'wEdg': 4, 'wImp': 5, 'wFll': 0, 'wPol': 3,
                           'wThr': 0, 'wBow': 0, 'wMsD': 4, 'Alch': 1,
                           'Relg': 4, 'Virt': 1, 'SpkC': 4, 'SpkL': 0,
                           'R&W': 1, 'Heal': 1, 'Artf': 5, 'Stlh': 1,
                           'StrW': 3, 'Ride': 0, 'WdWs': 0}

        elif self.family == 'country crafts':
            self.mod_attribute('Agl', 1)
            self.mod_attribute('Int', 1)
            self.mod_attribute('EP', 94)

            self.skills = {'wEdg': 4, 'wImp': 3, 'wFll': 0, 'wPol': 4,
                           'wThr': 1, 'wBow': 4, 'wMsD': 1, 'Alch': 0,
                           'Relg': 2, 'Virt': 1, 'SpkC': 3, 'SpkL': 0,
                           'R&W': 1, 'Heal': 1, 'Artf': 4, 'Stlh': 1,
                           'StrW': 0, 'Ride': 0, 'WdWs': 3}

        elif self.family == 'common urban':
            self.mod_attribute('Str', 1)
            self.mod_attribute('Agl', 1)
            self.mod_attribute('Int', -1)
            self.mod_attribute('Chr', -1)
            self.mod_attribute('EP', 96)

            self.skills = {'wEdg': 4, 'wImp': 4, 'wFll': 0, 'wPol': 3,
                           'wThr': 3, 'wBow': 0, 'wMsD': 2, 'Alch': 0,
                           'Relg': 2, 'Virt': 1, 'SpkC': 2, 'SpkL': 0,
                           'R&W': 0, 'Heal': 1, 'Artf': 1, 'Stlh': 4,
                           'StrW': 4, 'Ride': 0, 'WdWs': 0}

        else:
            self.mod_attribute('End', 1)
            self.mod_attribute('Str', 1)
            self.mod_attribute('Agl', 1)
            self.mod_attribute('Chr', -1)
            self.mod_attribute('EP', 97)

            self.skills = {'wEdg': 3, 'wImp': 3, 'wFll': 4, 'wPol': 3,
                           'wThr': 3, 'wBow': 1, 'wMsD': 0, 'Alch': 0,
                           'Relg': 1, 'Virt': 1, 'SpkC': 1, 'SpkL': 0,
                           'R&W': 0, 'Heal': 1, 'Artf': 1, 'Stlh': 3,
                           'StrW': 0, 'Ride': 1, 'WdWs': 4}

    # Character description
    def describe(self):
        print("{} is a {} year old {} from a {} family.".format(self.name,
                                                                self.age,
                                                                self.gender,
                                                                self.family))

    # prints list of occupations
    def print_occupations(self):
        for occupation in self.occupations:
            print(occupation)

    # adds new occupation
    def add_occupation(self, occupation):

        self.mod_age(5)  # advance age by 5 years
        self.occupations.append(occupation.name)  # add occupation to list
        self.inv.clear()  # clear any previous inventory

        for item in occupation.items:  # give occupation items
            self.inv[item] += 1

        for k, v in self.attributes.items():  # apply occupation attributes
            self.attributes[k] += occupation.dattributes[k]

        for k, v in self.skills.items():  # apply occupation skills
            self.skills[k] += occupation.dskills[k]

        if len(self.occupations) == 1:  # add bonus if first occupation
            self.mod_attribute('EP', 20)
            for k, v in self.skills.items():
                self.mod_skill(k, 2)

        if len(self.occupations) == 2:  # add bonus if second occupation
            self.mod_attribute('EP', 5)

        self.add_weapon()  # add weapon from highest weapon skill class

    # prints all attribute values
    def print_attributes(self):
        for k, v in self.attributes.items():
            print(k, v)

    # returns value of attribute
    def get_attribute(self, attribute):
        return self.attributes.get(attribute)

    # change attribute value
    def set_attribute(self, attribute, value):
        self.attributes[attribute] = value

    # modrement attribute value
    def mod_attribute(self, attribute, value):
        self.attributes[attribute] += value

    # prints all skill values
    def print_skills(self):
        for k, v in self.skills.items():
            print(k, v)

    # return value of skill
    def get_skill(self, skill):
        return self.skills.get(skill)

    # change skill value
    def set_skill(self, skill, value):
        self.skills[skill] = value

    # mod skill value
    def mod_skill(self, skill, value):
        self.skills[skill] += value

    # change name
    def change_name(self, name):
        self.name = name

    # change age
    def change_age(self, age):
        self.age = age

    # mod age
    def mod_age(self, dage):
        self.age += dage

        if self.age == 30:
            self.mod_attribute('End', -1)
            self.mod_attribute('Str', -1)
            self.mod_attribute('Agl', -1)

        if self.age == 35:
            self.mod_attribute('End', -2)
            self.mod_attribute('Str', -1)
            self.mod_attribute('Agl', -2)

        if self.age == 40:
            self.mod_attribute('End', -2)
            self.mod_attribute('Str', -2)
            self.mod_attribute('Agl', -2)

        if self.age == 45:
            self.mod_attribute('End', -3)
            self.mod_attribute('Str', -2)
            self.mod_attribute('Agl', -2)
            self.mod_attribute('Per', -1)
            self.mod_attribute('Int', 0)
            self.mod_attribute('Chr', -1)

        if self.age == 50:
            self.mod_attribute('End', -3)
            self.mod_attribute('Str', -2)
            self.mod_attribute('Agl', -3)
            self.mod_attribute('Per', -1)
            self.mod_attribute('Int', 0)
            self.mod_attribute('Chr', -1)

        if self.age == 55:
            self.mod_attribute('End', -3)
            self.mod_attribute('Str', -3)
            self.mod_attribute('Agl', -3)
            self.mod_attribute('Per', -2)
            self.mod_attribute('Int', -1)
            self.mod_attribute('Chr', -2)

        if self.age == 60:
            self.mod_attribute('End', -5)
            self.mod_attribute('Str', -4)
            self.mod_attribute('Agl', -4)
            self.mod_attribute('Per', -3)
            self.mod_attribute('Int', -2)
            self.mod_attribute('Chr', -3)

        if self.age == 65:
            self.mod_attribute('End', -6)
            self.mod_attribute('Str', -6)
            self.mod_attribute('Agl', -4)
            self.mod_attribute('Per', -3)
            self.mod_attribute('Int', -2)
            self.mod_attribute('Chr', -3)

    # change gender
    def change_gender(self, gender):
        self.gender = gender

    # add item to inv
    def add_item(self, item, amount):
        if item not in self.inv:
            self.inv[item] = amount
            return

        self.inv[item] += amount

    # returns best weapon skill

    def add_weapon(self):
        weapon_skills = {'wEdg': 0, 'wImp': 0, 'wFll': 0, 'wPol': 0,
                         'wThr': 0, 'wBow': 0, 'wMsD': 0}

        for k, v in weapon_skills.items():
            weapon_skills[k] = self.skills[k]

        max_skill = max(weapon_skills.keys(), key=lambda k: weapon_skills[k])

        if max_skill == 'wEdg':
            self.add_item(items.Shortsword(), 1)

        if max_skill == 'wImp':
            self.add_item(items.Club(), 1)

        if max_skill == 'wFll':
            self.add_item(items.MFlail(), 1)

        if max_skill == 'wPol':
            self.add_item(items.TKnife(), 1)

        if max_skill == 'wBow':
            self.add_item(items.SBow(), 1)

        if max_skill == 'wMsD':
            self.add_item(items.Crossbow(), 1)

    # remove item from inv
    def remove_item(self, item, amount):
        if item not in self.inv:
            return
        if amount >= self.inv.get(item):
            del self.inv[item]
            return
        self.inv[item] -= amount

    # prints all items in inv
    def print_inv(self):
        for k, v in self.inv.items():
            print(k.name, v)

    # add saint to character
    def add_saint(self, saint):
        self.saints.append(saint)
        self.saints.sort()

    # print saints
    def print_saints(self):
        for saint in self.saints:
            print(saint)

    # add recipe to character
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.recipes.sort()

    # print recipes
    def print_recipes(self):
        for recipe in self.recipes:
            print(recipe)
