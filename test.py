import character
import occupations

def test_create_character():  # tests character creation
    tony = character.Character('Tony', 'male', 'noble')
    assert tony.attributes == {'End': 13, 'Str': 16, 'Agl': 12,
                               'Per': 13, 'Int': 12, 'Chr': 12,
                               'DF': 0, 'EP': 89}

    assert tony.skills == {'wEdg': 5, 'wImp': 4, 'wFll': 1, 'wPol': 4,
                           'wThr': 0, 'wBow': 4, 'wMsD': 0, 'Alch': 2,
                           'Relg': 5, 'Virt': 2, 'SpkC': 4, 'SpkL': 2,
                           'R&W': 2, 'Heal': 0, 'Artf': 0, 'Stlh': 1,
                           'StrW': 0, 'Ride': 3, 'WdWs': 1}

    return tony


def test_occupation(occupation):  # tests veteran occupation
    tony = character.Character('Tony', 'male', 'noble')

    tony.add_occupation(occupation)
    tony.print_occupations()
    print('***********')
    tony.print_attributes()
    print('***********')
    tony.print_skills()
    print('***********')
    tony.print_inv()





#def test_create_interaction():  # tests interaction creation
    #ia0_koln_gate = Interaction(name)

test_create_character()         # test suite
test_occupation(occupations.Veteran())
test_occupation(occupations.Soldier())
#test_create_interaction()