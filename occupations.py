class Occupation:

    # Initialize
    def __init__(self, name, dattributes, dskills):
        self.name = name
        self.dattributes = dattributes
        self.dskills = dskills


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
                                  'Stlh': 1, 'StrW': 1, 'Ride': 1, 'WdWs': 1})


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
                                  'Stlh': 2, 'StrW': 1, 'Ride': 1, 'WdWs': 3})


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
                                  'Stlh': 2, 'StrW': 2, 'Ride': 2, 'WdWs': 2})
