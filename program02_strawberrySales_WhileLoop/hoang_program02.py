# Written by: Vy Hoang
# Program: Strawberry sales calculation - using while loop
# This program calculates strawberry sales for the month.

# Validate sales data input & calculate total sales
more_sales_data = input('Do you have strawberry sales '
                        'data to enter? (y/n): ')
total_sales_data = 0
while more_sales_data == "y":
    new_sales_data = int(input('\nEnter the quantity of '
                               'sales in pints: '))
    # Calculate total sales
    total_sales_data += new_sales_data
    more_sales_data = input('Do you have more strawberry '
                            'sales data to enter? (y/n): ')

# Display total sales
print('Total strawberry sales in pints: {}'. format(total_sales_data))

