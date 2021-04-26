# ________________________________________________________________________  #
# Written by: Vy Hoang                                                      #
# Program: Pokemon Keep Track - using class, functions                      #
# This program keeps track of Pokémon characters, saves the data to file,   #
# and displays the data from a file.                                        #
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

    print('\n\n##############  In main() ##############')
    pokemon_list = add_pokemon()
    display_pokemon(pokemon_list)

    print('\n\n####### Save Pokemon data to file #########')
    pokemon_file = input('\nEnter the name of the file? ')
    save_data(pokemon_list, pokemon_file)

    print('\n\n######## Read Pokemon data from the file ######')
    display_data(pokemon_file)


# ___________________________add_pokemon()______________________________#
# This function gets Pokemon data and populate to pokemon list.         #
# It then returns the pokemon lilst.                                    #
# ______________________________________________________________________#
def add_pokemon():
    print('\nIn add_pokemon() from program 08')
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
# This function displays data for each Pokemon.                         #
# ______________________________________________________________________#
def display_pokemon(pokemon_list):
    print('\nIn display_pokemon() from program 08')
    num = 0
    for p in pokemon_list:
        num += 1
        print('\nName of Pokemon #{}: {}'
              .format(num, Pokemon.get_name(p)))
        print('\nAbility of Pokemon #{}: {}'
              .format(num, Pokemon.get_ability(p)))

# ___________________________save_data()________________________________#
# This function saves Pokemon data to file.                             #
# ______________________________________________________________________#
def save_data(pokemon_list, pokemon_file):
    print('\nWrite Pokemon data to a file')
    p_file = open(pokemon_file, 'w')
    num = 0
    for p in pokemon_list:
        num += 1
        p_file.write('Name of Pokemon #{}: {}\n'.format(num, Pokemon.get_name(p)))
        p_file.write('Ability of Pokemon #{}: {}\n'.format(num, Pokemon.get_ability(p)))

    p_file.close()

# ___________________________display_data()_____________________________#
# This function displays Polemon data reading from the file.            #
# ______________________________________________________________________#
def display_data(pokemon_file):
    print('\nDisplay Pokemon data from the file\n')
    p_file = open(pokemon_file, 'r')
    lines = p_file.readlines()
    for line in lines:
        print(line)

    p_file.close()


if __name__ == '__main__':
    main()
else:
    pass
