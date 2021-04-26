# ________________________________________________________________________  #
# Written by: Vy Hoang                                                      #
# Program: Pokemon Keep Track - using class, functions                      #
# This program keeps track of data of Pokémon characters you have captured. #
# ________________________________________________________________________  #


# Define class Pokemon
class Pokemon:
    def __init__(self, name, ability):
        self.__name = name
        self.__ability = ability

    def get_name(self):
        return self.__name

    def get_ability(self):
        return self.__ability

# ______________________________main()__________________________________#
def main():

    print('\n##############  In main()  ##############')
    pokemon_list = add_pokemon()
    display_pokemon(pokemon_list)


# ___________________________add_pokemon()______________________________#
# This function gets Pokemon data and populate to pokemon list.         #
# It then returns the pokemon lilst.                                    #
# ______________________________________________________________________#
def add_pokemon():
    print('\nIn add_pokemon()')
    pokemon_list = []
    pokemon_number = 1
    more_pokemon = input('\nDo you have a pokemon to enter? (y/n) ').lower()
    while more_pokemon == "y":
        pokemon_name = input('\nEnter name for Pokemon #{}: '
                             .format(pokemon_number))
        pokemon_ability = input('\nEnter ability for Pokemon #{}: '
                                .format(pokemon_number))
        new_pokemon = Pokemon(pokemon_name, pokemon_ability)
        pokemon_list.append(new_pokemon)
        pokemon_number += 1
        more_pokemon = input('\nAnother pokemon to enter? (y/n) ').lower()

    return pokemon_list

# ___________________________display_pokemon()__________________________#
# This function displays data for each Pokemon                          #
# ______________________________________________________________________#
def display_pokemon(pokemon_list):
    num = 0
    for p in pokemon_list:
        num += 1
        print('\nName of Pokemon #{}: {}'
              .format(num, Pokemon.get_name(p)))
        print('\nAbility of Pokemon #{}: {}'
              .format(num, Pokemon.get_ability(p)))


if __name__ == '__main__':
    main()
else:
    pass