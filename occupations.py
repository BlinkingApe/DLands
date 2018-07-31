import items


class Occupation:

    # Initialize
    def __init__(self, name, dattributes, dskills, epskills, items):
        self.name = name
        self.dattributes = dattributes
        self.dskills = dskills
        self.items = items


class Recruit(Occupation):

    def __init__(self):
        super().__init__(name='Recruit',
                         dattributes={'End': 1, 'Str': 1, 'Agl': 0,
                                      'Per': 0, 'Int': 0, 'Chr': 0,
                                      'DF': 0, 'EP': 18},
                         dskills={'wEdg': 6, 'wImp': 6, 'wFll': 1,
                                  'wPol': 6, 'wThr': 1, 'wBow': 1,
                                  'wMsD': 6, 'Alch': 0, 'Relg': 0,
                                  'Virt': 0, 'SpkC': 1, 'SpkL': 0,
                                  'R&W': 0, 'Heal': 1, 'Artf': 0,
                                  'Stlh': 1, 'StrW': 1, 'Ride': 1, 'WdWs': 1},
                         epskills={'wEdg': 4, 'wImp': 4, 'wFll': 7,
                                   'wPol': 4, 'wThr': 6, 'wBow': 7,
                                   'wMsD': 4, 'Alch': 0, 'Relg': 2,
                                   'Virt': 2, 'SpkC': 2, 'SpkL': 0,
                                   'R&W': 0, 'Heal': 2, 'Artf': 2,
                                   'Stlh': 5, 'StrW': 5, 'Ride': 4, 'WdWs': 4},
                         items=[items.VCuirbouilli(), items.LLeather()])


class Soldier(Occupation):
    def __init__(self):
        super().__init__(name='Soldier',
                         dattributes={'End': 0, 'Str': 0, 'Agl': 0,
                                      'Per': 0, 'Int': 0, 'Chr': 0,
                                      'DF': 0, 'EP': 18},
                         dskills={'wEdg': 4, 'wImp': 2, 'wFll': 1,
                                  'wPol': 3, 'wThr': 1, 'wBow': 1,
                                  'wMsD': 3, 'Alch': 0, 'Relg': 1,
                                  'Virt': 1, 'SpkC': 1, 'SpkL': 0,
                                  'R&W': 0, 'Heal': 2, 'Artf': 1,
                                  'Stlh': 2, 'StrW': 1, 'Ride': 1, 'WdWs': 3},
                         epskills={'wEdg': 6, 'wImp': 6, 'wFll': 1,
                                   'wPol': 6, 'wThr': 1, 'wBow': 1,
                                   'wMsD': 6, 'Alch': 0, 'Relg': 0,
                                   'Virt': 0, 'SpkC': 1, 'SpkL': 0,
                                   'R&W': 0, 'Heal': 1, 'Artf': 0,
                                   'Stlh': 1, 'StrW': 1, 'Ride': 1, 'WdWs': 1},
                         items=[items.VChainmail(), items.LSLeather()])


class Veteran(Occupation):
    def __init__(self):
        super().__init__(name='Veteran',
                         dattributes={'End': 1, 'Str': 1, 'Agl': 0,
                                      'Per': 0, 'Int': 0, 'Chr': -1,
                                      'DF': 0, 'EP': 21},
                         dskills={'wEdg': 3, 'wImp': 2, 'wFll': 1,
                                  'wPol': 2, 'wThr': 1, 'wBow': 1,
                                  'wMsD': 2, 'Alch': 0, 'Relg': 1,
                                  'Virt': 1, 'SpkC': 2, 'SpkL': 0,
                                  'R&W': 1, 'Heal': 2, 'Artf': 1,
                                  'Stlh': 2, 'StrW': 2, 'Ride': 2, 'WdWs': 2},
                         epskills={'wEdg': 6, 'wImp': 6, 'wFll': 1,
                                   'wPol': 6, 'wThr': 1, 'wBow': 1,
                                   'wMsD': 6, 'Alch': 0, 'Relg': 0,
                                   'Virt': 0, 'SpkC': 1, 'SpkL': 0,
                                   'R&W': 0, 'Heal': 1, 'Artf': 0,
                                   'Stlh': 1, 'StrW': 1, 'Ride': 1, 'WdWs': 1},
                         items=[items.VBrigandine(), items.LCuirbouilli()])
