# ________________________________________________________________________  #
# Written by: Vy Hoang                                                      #
# Program: Pratice with file operations                                     #
# This program demonstrates reading, writing, and organizing files.         #                                       #
# ________________________________________________________________________  #


from pathlib import Path
import pyperclip, shutil, zipfile, pyinputplus as pypip

# Display the current working directory
print("\nCurrent working directory: ", Path.cwd())

# Get directory to save file from user
subDir1 = Path(input("\nEnter the directory you want to save files: "))
Path(subDir1).mkdir()

# Write three lines to file_one.txt
fileOne = open(Path(subDir1) / 'file_one.txt', 'w')
fileOneOut = fileOne.write('Line 1 from file_one wrong_text\n'
                           'Line 2 from file_one wrong_text\nLine 3 from file_one wrong_text')
fileOne.close()


# Read and display the contents of the file_one.txt
fileOne = open(Path(subDir1) / 'file_one.txt').read()
print("\nThe content of file_one.txt:\n\n", fileOne, sep='')


# Read file_one.txt, replace text in each line and write to file_two.txt
fileOne = open(Path(subDir1) / 'file_one.txt', 'r')
fileTwo = open(Path(subDir1) / 'file_two.txt', 'w')
for line in fileOne:
    fileTwo.write(line.replace('file_one wrong_text', 'file_two correct_text'))
fileOne.close()
fileTwo.close()


# Demonstrate pyperclip
print("""\nPlease type the following lines into a text editor 
and copy the lines to the clipboard (using Ctrl-c):\n
Line 1 from the clipboard
Line 2 from the clipboard
Line 3 from the clipboard""")
confirm = pypip.inputYesNo("\nEnter 'y' when you are done typing and copying to clipboard: ")

# Display the contents from clipboard
print("\nThe contents from the clipboard:")
pyperclip.copy('''Line 1 from the clipboard
Line 2 from the clipboard
Line 3 from the clipboard''')
print(pyperclip.paste())

# Read the contents of file_two.txt
fileTwo = open(Path(subDir1) / 'file_two.txt', 'r')
# Read the contents of the clipboard
clipBoardText = str(pyperclip.paste()).split('\n')

# Append the contents of clipboard onto file_two.txt and write lines out to file_three.txt
fileThree = open(Path(subDir1) / 'file_three.txt', 'w')
i = 0
for line in fileTwo:
    fileThree.write(line.rstrip('\n') + ' followed by ' + clipBoardText[i] + '\n')
    i += 1
fileTwo.close()
fileThree.close()


# Display the contents of file_three.txt
fileThree = open(Path(subDir1) / 'file_three.txt').read()
print("\nThe contents of the file_three.txt:\n", fileThree, sep='')


# Get new directory from user
subDir2 = Path(input("\nEnter a new directory name: "))
# Copy files to new directory
shutil.copytree(Path(subDir1), Path(subDir2))
# Compress files in new directory
newZip = zipfile.ZipFile(Path(subDir2) / 'new.zip', 'w')
newZip.write(Path(subDir2) / 'file_one.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write(Path(subDir2) / 'file_two.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.write(Path(subDir2) / 'file_three.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

