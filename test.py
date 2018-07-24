from character import Character
import occupations

tony = Character('Tony', 'male', 'noble')
print(tony.describe())
tony.print_attributes()
tony.add_occupation(occupations.Recruit())
tony.add_occupation(occupations.Veteran())

tony.print_attributes()
