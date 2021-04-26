# Written by: Vy Hoang
# Program: Book Order Recording - using nested while/for loops and lists
# This program records the book data per each author the buyers order in a book store.

# Get number of authors
num_authors = int(input('Enter the number of authors: '))

# Loop to get each author data and book order per author
for num in range(1, num_authors + 1):
    author_name = input('Enter author name {}: '.format(num))
    url = input('Enter author website URL {}: '.format(num))

    # Create lists to hold book data the user input
    books_title = []
    books_isbn = []
    books_order_amount = []

    # Nested loop to store book data for each author until user enters -1 to end
    book_count = 0
    again = int(input('\nTo input book data, enter any integer other than -1\n'
                      '(to end, enter -1): '))
    while again != -1:
        book_count += 1
        book_title = input('\nEnter book title: ')
        book_isbn = input('Enter book ISBN: ')
        book_order_amount = int(input('Enter amount to order: '))
        # Store data to the lists
        books_title.append(book_title)
        books_isbn.append(book_isbn)
        books_order_amount.append(book_order_amount)

        print()
        again = int(input('\nTo input book data, enter any integer other than -1\n'
                          '(to end, enter -1): '))

    # Display data for each author
    print(author_name)
    print(url)
    print()
    # Display data for each book order per author
    for i in range(book_count):
        print('Book Title', i+1, '-', books_title[i])
        print('Book ISBN', i+1, '-', books_isbn[i])
        print('Amount to Order', i+1, '-', books_order_amount[i])
        print()


# ____________________Sample Output_______________________ #
# ___________________for each author______________________ #
"""
    Michael Crichton
    michaelcrichton.com
    
    Book Title 1 – Jurassic Park
    Book ISBN 1 – 978-1613835050
    Amount to Order 1 – 33
    
    Book Title 2 – Disclosure
    Book ISBN 2 – 978-0679419457
    Amount to Order 2 – 50
    
    Book Title 3 – Dragon Teeth
    Book ISBN 3 – 978-0062473356
    Amount to Order 3 - 99
"""
# _________________________________________________________ #
