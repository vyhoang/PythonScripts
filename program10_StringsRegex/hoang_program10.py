# ________________________________________________________________________  #
# Written by: Vy Hoang                                                      #
# Program: Practice with strings stuff                                      #
# This program works with strings, uses regular expressions,                #
# and performs input validation tasks.                                      #
# This program requires the use of pyperclip, a module to work              #
# with the clipboard.                                                       #
# ________________________________________________________________________  #

import pyinputplus as pyip
import pyperclip
import re

print("\n######   A String that includes the five Python escape characters ######")
print("My favorite\'s movies:\n\"2012\" by Roland Emmerich\\\t\"Taken\" by Olivier Megaton\\\t"
      "\"Captain Phillips\" by Paul Greengrass")

print("\n######   A raw string that includes the five Python escape characters ######")
print(r"My favorite\'s movies:\n\"2012\" by Roland Emmerich\\\t\"Taken\" by Olivier Megaton\\"
      r"\t\"Captain Phillips\" by Paul Greengrass")

print("\n######   Triple quotes using single and double quote ######")
print('''My favorite\'s movies:
2012
Taken
Captain \"Phillips\"''')

print("\n######   An example of multiline comments in code ######")
"""Vy Hoang are practicing Python script.
This is example of multiline comments.
"""

print("\n\nAssign a string to a list and print characters in string")
my_string = 'Beautiful life!'
print("\nMy string: ", my_string)
print("\nA single indexed character at 0:", my_string[0])
print("\nThe character 5 index places from the end:", my_string[-5])
print("\nThe characters starting at 3 until the end:", my_string[3:])
print("\nThe characters from the beginning up to but not including character 7:", my_string[0:7])


print("\n\nDemonstrate the in and not in operators.")
print("\n\'Beautiful\' in my string:", 'Beautiful' in my_string)
print("\n\'Beautiful\' not in my string:", 'Beautiful' not in my_string)


print("\n\nDemonstrate including two strings inside another string")
first_name = 'Vy'
last_name = 'Hoang'
print("\nMy full name using \'+\' operator:", first_name + ' ' + last_name)
print("\nMy full name using string interpolation: {} {}".format(first_name, last_name))
print(f"\nMy full name using f-strings: {first_name} {last_name}")


print("\n\nDemonstrate: isalpha(), isalnum(), isdecimal(), isspace(), and istitle()")
print("\n\'life\' with string method isalpha():\t", 'life'.isalpha())
print("\n\'life123\' with string method isalpha():\t", 'life123'.isalpha())
print("\n\'life123\' with string method isalnum():\t", 'life123'.isalnum())
print("\n\'life\' with string method isalnum():\t", 'life'.isalnum())
print("\n\'123\' with string method isdecimal():\t", '123'.isdecimal())
print("\n\'     \' with string method isspace():\t", '     '.isspace())
print("\n\'Life Is Beautiful!\' with string method istitle():\t\t",
      'Life Is Beautiful!'.istitle())
print("\n\'Life 123 Is Beautiful!\' with string method istitle():\t",
      'Life 123 Is Beautiful!'.istitle())
print("\n\'Life is  NOT Beautiful!\' with string method istitle():\t",
      'Life is  NOT Beautiful!'.istitle())


print("\n\nUse two isX() methods in two loops (one per loop) for input validation")
while True:
    user_name = input("\nEnter username: ")
    if not user_name.isalnum():
        print("\nUsername can only have letters (a-z), numbers (0-9) and no spaces")
    else:
        break

while True:
    phone_num = input("\nEnter phone number: ")
    if not phone_num.isdecimal():
        print("\nPlease input only numbers (0-9) and no spaces")
    else:
        break


print("\n\nConvert a list of strings into one string using join()")
list_fruits = ['orange', 'lemon', 'apple']
string_fruits = 'Juice, '.join(list_fruits)
print("\nConvert a list of strings into one string:", string_fruits)


print("\n\nConvert one string into a list of strings using split()")
print("\nConvert one string into a list of strings", string_fruits.split('Juice, '))


print("\n\nDemonstrate the following string methods")
print("\n\'Life is so beautiful\' with string method partition():",
      'Life is so beautiful'.partition('is'))
print("\n\' Life \' with string method center(25):", ' Life '.center(25))
print("\n\'BadLife\' with string method strip('adB'):", 'BadLife'.strip('adB'))
print("\nReturn an integer \'65\' with string method ord('A'):", ord('A'))
print("\nReturn a character \'A\' with string method chr(65):", chr(65))


print("\n\nDemonstrate the following using pyperclip copy() and paste()")

my_text = 'The days are long but the years are short!'
pyperclip.copy(my_text.upper().join('""'))
print("\nNew replacement pasted from clipboard:", pyperclip.paste())


print("\n\nUse regular expressions to verify the user id "
      "supplied by the user meets format")
ID = input("\nEnter user ID in format AAAA-####: ")

idRegex = re.compile(r'^[a-zA-Z]{4}([-][0-9]{4})')
while True:
    matchID = idRegex.search(ID)
    if not matchID:
        print("\nIncorrect user ID.")
        ID = input("\nRe-Enter user ID in format AAAA-####: ")
    else:
        break


print("\n\nVerify that one of the user ids in the list has been entered.")
accepted_IDs = ["gdrt-8493", "DBTF-6253", "UyHt-8326", "YYrv-5329", "qzrb-8264"]
print("The id list: ", accepted_IDs)
# Display a message the id match in the list
if matchID.group() in accepted_IDs:
    print("\nThank you for entering your user ID.")


print("\n\nUse regular expressions to verify the phone number"
      " supplied by the user meets format")
phoneNum = input("Enter your phone number in format ###-###-###-####: ")

phoneRegex = re.compile(r'(\d{3})-(\d{3})-(\d{3})-(\d{4})')
while True:
    matchPhone = phoneRegex.search(phoneNum)
    if not matchPhone:
        print("\nIncorrect phone number.")
        phoneNum = input("\nRe-Enter phone number in format ###-###-###-####: ")
    else:
        break


print("\n\nVerifying the phone number meets the format,"
      " verify the call is being placed to one of the countries below")
accepted_calls = {"Andorra": "376", "Bolivia": "591", "Djibouti": "253",
                  "Georgia": "995", "Lithuania": "370"}
print("The placed call list: ", accepted_calls)
# Display a message after successful entry
for index in accepted_calls:
    if matchPhone.group(1) == accepted_calls[index]:
        print("\nYour call has been placed. Thank you for calling", index.join(' .'), sep="")

# Demonstrate five PyInputPlus functions to validate input
print("\n######### Validate inputNum() ########")
print(pyip.inputNum("\nEnter a number: "))

print("\n######### Validate inputDate() ########")
print(pyip.inputDate("\nEnter a date : "))

print("\n######### Validate inputYesNo() ########")
print(pyip.inputYesNo("\nDo you like Python? (y/n): "))

print("\n######### Validate inputChoice() ########")
fruits = ['apple', 'banana', 'orange']
print("\nYour choice:", pyip.inputChoice(fruits))

print("\n######### Validate inputMenu() ########")
print("\nYour fruit:", pyip.inputMenu(fruits, numbered=True))

# Demonstrate the following PyInputPlus keyword arguments
print("\n######### Keyword arguments min, max ########")
print(pyip.inputInt("\nEnter a number (min=70, max=100): ", min=70, max=100))

print("\n######### Keyword arguments greaterThan, lessThan ########")
print(pyip.inputNum("\nEnter a number (3<num<5):  ", lessThan=5, greaterThan=3))

print("\n######### Keyword arguments limit, timeout, default ########")
print(pyip.inputEmail("\nEnter your email1(limit=3): ", limit=3, default='\nFailed Input!'))
print(pyip.inputEmail("\nEnter your email2(timeout=10): ", timeout=10, default='\nTime Out!'))

print("\n######### Keyword arguments allowRegexes and block Regexes ########")
print(pyip.inputNum("\nEnter a positive number: ", blockRegexes=[r'-[\d]']))
print(pyip.inputNum("\nEnter a number with spaces: ", allowRegexes=[r'\s']))
