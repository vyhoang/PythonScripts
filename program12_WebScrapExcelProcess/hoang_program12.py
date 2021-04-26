# ________________________________________________________________________  #
# Written by: Vy Hoang                                                      #
# Program: Web Scraping - using bs4, request.. and work on Exel process     #
# This program demonstrates using Python to perform web scraping            #
# and working with Excel spreadsheets.                                      #
# ________________________________________________________________________  #


import bs4
import openpyxl
import pyinputplus as pypip
import pyperclip
import requests
import webbrowser

# Get the addres from clipboard and navigate to open it on Google map
print("\nPlease copy a U.S. street address to the clipboard.")
pypip.inputYesNo("\nEnter 'y' after copying the address to clipboard: ")
pyperclip.copy('8601 Research Blvd, Austin, TX 78758')
readAddress = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + readAddress)


# Display the text of the <p> elements selected from a web page
URL = input("\nPlease enter an URL of a web page: ")
res = requests.get(URL)
res.raise_for_status()
pElemsSoup = bs4.BeautifulSoup(res.text, 'html.parser')
pElems = pElemsSoup.select('p')
j = 0
for index in range(len(pElems)):
    j += 1
    print("\nThe text of the <p> #{}: ".format(j), pElems[index].getText(''.strip()))


# Work on class ExcelProcessing and
# define member functions to process the excel file
class ExcelProcessing:
    # Initialize workbook object
    def __init__(self, workbook_name):
        self.workbook = openpyxl.load_workbook(workbook_name)

    # Return the list of sheets of the workbook
    def sheetNames(self):
        return self.workbook.sheetnames

    # Return the sheet name
    def sheet(self, sheetName):
        sheet = self.workbook[sheetName]
        return sheet

    # Return cell values of the sheet name
    def cellValue(self, sheetName, cellNum):
        sheet = self.sheet(sheetName)
        return sheet[cellNum].value

    # Display cell values of rectangular section
    def rectangularSection(self, sheetName, rectSection):
        section = self.sheet(sheetName)[rectSection]
        for row in section:
            for cell in row:
                print(cell.coordinate, cell.value)
            print("--- END OF ROW ---\n")


def main():
    # Pass the excel file
    processor = ExcelProcessing('example.xlsx')

    # Display the list of sheets in the file
    listSheets = processor.sheetNames()
    print("\nThe list of sheets:", listSheets)

    # Display cell values user input
    cellNum = input("\nEnter a cell number in range A1-C7: ").upper()
    cellValue = processor.cellValue('Sheet1', cellNum)
    print("\nThe value in the cell {}:".format(cellNum), cellValue)

    # Display cel values in rectangular section as user input
    rectSection = input("\nEnter a rectangular section from example.xlsx (e.g. A3:C7): ").upper()
    print("\nThe values in the cells of the rectangular section [{}]:\n".format(rectSection))
    processor.rectangularSection('Sheet1', rectSection)


if __name__ == '__main__':
    main()
else:
    pass

