from orderedcounter import OrderedCounter
from character import Character
import occupations
import items

def test_create_character():  # tests character creation
    tony = Character('Tony', 'male', 'noble')
    assert tony.attributes == {'End': 13, 'Str': 16, 'Agl': 12,
                               'Per': 13, 'Int': 12, 'Chr': 12,
                               'DF': 0, 'EP': 89}

    assert tony.skills == {'wEdg': 5, 'wImp': 4, 'wFll': 1, 'wPol': 4,
                           'wThr': 0, 'wBow': 4, 'wMsD': 0, 'Alch': 2,
                           'Relg': 5, 'Virt': 2, 'SpkC': 4, 'SpkL': 2,
                           'R&W': 2, 'Heal': 0, 'Artf': 0, 'Stlh': 1,
                           'StrW': 0, 'Ride': 3, 'WdWs': 1}

    return tony


def test_veteran_occupation():  # tests veteran occupation
    tony = Character('Tony', 'male', 'noble')
    tony.add_occupation(occupations.Veteran())
    assert tony.attributes == {'End': 14, 'Str': 17, 'Agl': 12,
                               'Per': 13, 'Int': 12, 'Chr': 11,
                               'DF': 0, 'EP': 110}
    assert tony.skills == {'wEdg': 8, 'wImp': 6, 'wFll': 2, 'wPol': 6,
                           'wThr': 1, 'wBow': 5, 'wMsD': 2, 'Alch': 2,
                           'Relg': 6, 'Virt': 3, 'SpkC': 6, 'SpkL': 2,
                           'R&W': 3, 'Heal': 2, 'Artf': 1, 'Stlh': 3,
                           'StrW': 2, 'Ride': 5, 'WdWs': 3}
    tony.print_inv()
#def test_inventory():  # tests player inventory
    

#def test_create_interaction():  # tests interaction creation
    #ia0_koln_gate = Interaction(name)

test_create_character()         # test suite
test_veteran_occupation()
#test_create_interaction()