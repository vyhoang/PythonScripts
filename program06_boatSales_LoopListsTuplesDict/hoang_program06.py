# Written by: Vy Hoang
# Program: Boat Sales Recording - using nested loops, lists, strings, tuples, and dictionaries
# This program records sales for sales reps that the user enters.
# For each sales rep that the user enters, record sales for
# Thursday, Friday, and Saturday for Week One and Week Two.

# Define two tuples - one to hold two weeks and the other to hold three days of each week
weeks = ('Week One', 'Week Two')
days = ('Thursday', 'Friday', 'Saturday')

# Create two lists to hold sales rep data
sales_rep_names = []
sales_rep_locations = []

# Get sales rep data and populate sales rep data to each list
sales_rep_data = 'y'
while sales_rep_data == 'y':
    name = {'first_name': input('\nEnter first name for the sale rep: ').capitalize(),
            'last_name': input('\nEnter last name for the sale rep: ').capitalize()}
    location = input('\nEnter a location for the sale rep: ').capitalize()

    sales_rep_names.append(name)
    sales_rep_locations.append(location)

    sales_rep_data = input('\nDo you have more sale rep data to enter? (enter "y" or "n"): ').lower()

# Create three lists to hold boats sold data
boats_sold_thursday = []
boats_sold_friday = []
boats_sold_saturday = []

# Get boats sold data for each day per each week by each sales rep
# and populate data for each week
print('\n########## Enter Sales Results ##########')
for week in weeks:
    print('\n-----Entering boats sold for {} -----'.format(week))
    for index in range(len(sales_rep_names)):
        name = sales_rep_names[index]
        boats_sold_thursday.append(int(input('\nThursday boats sold by {} {}: '
                                             .format(name['first_name'], name['last_name']))))
        boats_sold_friday.append(int(input('\nFriday boats sold by {} {}: '
                                           .format(name['first_name'], name['last_name']))))
        boats_sold_saturday.append(int(input('\nSaturday boats sold by {} {}: '
                                             .format(name['first_name'], name['last_name']))))

# Display boat sold data for each day per each week by each sales rep
print('##########  Print Sales Results ##########')
j = 0
length = len(sales_rep_names)
for week in weeks:
    print('\n------ {}  Results -----'.format(week))
    for i in range(length):
        name = sales_rep_names[i]
        print('\n{} {} sold {} on Thursday'.format(name['first_name'], name['last_name'],
                                                   boats_sold_thursday[(j * length) + i]))
        print('\n{} {} sold {} on Friday'.format(name['first_name'], name['last_name'],
                                                 boats_sold_friday[j * length + i]))
        print('\n{} {} sold {} on Saturday'.format(name['first_name'], name['last_name'],
                                                   boats_sold_saturday[j * length + i]))
    j += 1


# Process dealership URLS information and display contact info. for each sales rep
# Create URL dictionary
dealer_URLs = {}

# Get urls for each location and populate location keys and URL values to the dict.
print('########## Enter Dealership URLs ##########')
for location in sales_rep_locations:
    URL = input('\nEnter the URL for {}: '.format(location))
    dealer_URLs[location] = URL

# Display email address for each sales rep based on location and url data
for index in range(len(sales_rep_locations)):
    location = sales_rep_locations[index]
    url = dealer_URLs[location]
    name = sales_rep_names[index]
    print('\n {}_{}@{}'.format(name['first_name'], name['last_name'], url, ).lower())

