# ________________________________________________________________________ #
# Written by: Vy Hoang                                                     #
# Program: Boat Sales Recording - using functions                          #
# This program records sales for sales reps that the user enters.          #
# For each sales rep that the user enters, record sales for                #
# Thursday, Friday, and Saturday for Week One and Week Two.                #
# This program is similar as program 06 but it is written with modularity  #
# that uses multiple functions to process data.                            #
# ________________________________________________________________________ #

# Create two lists to hold sales rep data
sales_rep_names = []
sales_rep_locations = []

# Create three lists to hold boats sold data
boats_sold_thursday = []
boats_sold_friday = []
boats_sold_saturday = []

# ______________________________main()__________________________________#
def main():
    # Get weeks
    weeks = get_weeks()

    # Get name and location for each sales rep
    accept_sales_reps()
    # Get boats sold per day in each week by each sales rep
    accept_boats_sold(weeks)

    # Display sales results in each week
    print_sales_results(weeks)

    # Get url for each location
    URLs = get_URLs()

    # Display email address for each sales rep based on their location url
    print_email(URLs)

# ______________________get_weeks()____________________________________#
# This function defines two tuples: one for two weeks and              #
# the other for three days in a week. It then returns the weeks tuple  #
# _____________________________________________________________________#
def get_weeks():
    weeks = ('Week One', 'Week Two')
    days = ('Thursday', 'Friday', 'Saturday')
    return weeks

# ______________________accept_sales_reps()_____________________________#
# This function accepts data input for each sales rep, then populate    #
# data to two lists: sales_rep_names and sales_rep_locations.           #
# ______________________________________________________________________#
def accept_sales_reps():
    sales_rep_data = 'y'
    while sales_rep_data == 'y':
        sales_rep = input("\nEnter sales rep's first name: ").capitalize() + " " \
                    + input("\nEnter sales rep's last name: ").capitalize()

        location = input('\nEnter a location for the sale rep: ').capitalize()

        sales_rep_names.append(sales_rep)
        sales_rep_locations.append(location)

        sales_rep_data = input('\nDo you have more sale rep data to enter? (enter "y" or "n"): ').lower()

# ______________________accept_boats_sold()_____________________________#
# This function accepts data input for each week that includes          #
# boats sold for each day in the week by each sales rep.                #
# ______________________________________________________________________#
def accept_boats_sold(weeks):
    print('\n############ Enter Sales Results ############')
    for week in weeks:
        print('\n-----Entering boats sold for {} -----'.format(week))
        for sales_rep in sales_rep_names:
            boats_sold_thursday.append(int(input('\nThursday boats sold by {}: '
                                                 .format(sales_rep))))
            boats_sold_friday.append(int(input('\nFriday boats sold by {}: '
                                               .format(sales_rep))))
            boats_sold_saturday.append(int(input('\nSaturday boats sold by {}: '
                                                 .format(sales_rep))))

# ____________________print_sales_results()_____________________________#
# This function displays sales results for each week that includes      #
# boats sold for each day in the week by each sales rep.                #
# ______________________________________________________________________#
def print_sales_results(weeks):
    print('############  Print Sales Results ############')
    j = 0
    for week in weeks:
        print('\n------ {}  Results -----'.format(week))
        for sales_rep in sales_rep_names:
            print('\n{} sold {} on Thursday'.format(sales_rep, boats_sold_thursday[j]))
            print('\n{} sold {} on Friday'.format(sales_rep, boats_sold_friday[j]))
            print('\n{} sold {} on Saturday'.format(sales_rep, boats_sold_saturday[j]))
            j += 1

# ___________________________get_URLs()_________________________________#
# This function gets urls for each sales location and populate          #
# sales location and its URL values to the url dict.                    #
# It then returns the url dict.                                         #
# ______________________________________________________________________#
def get_URLs():
    dealer_URLs = {}
    print('############ Enter Dealership URLs ############')
    for sales_location in sales_rep_locations:
        URL = input('\nEnter the URL for {}: '.format(sales_location))
        dealer_URLs[sales_location] = URL

    return dealer_URLs

# ______________________print_email()___________________________________#
# This function displays each email address of each sales rep combined  #
# from data in the sales rep names  list and the urls list.             #
# ______________________________________________________________________#
def print_email(URLs):
    for sales_rep in sales_rep_names:
        location = sales_rep_locations[sales_rep_names.index(sales_rep)]
        print('\n {}@{}'.format(sales_rep.replace(' ', '_'), URLs[location]).lower())



if __name__ == '__main__':
    main()
else:
    pass