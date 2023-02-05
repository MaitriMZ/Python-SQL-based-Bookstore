"""
Bookstore program to implement the following functionalities:
MAIN MENU
    1. Enter book
    2. Update book
    3. Delete book
    4. Search book
    0. Exit

UPDATE MENU (Option 2)
    a. Search by book id
    b. Search by book name
    c. Search by book author
    d. Go to Main Menu

SEARCH MENU (Option 4)
    a. Search by book id
    b. Search by book name
    c. Search by book author
    d. Go to Main Menu

"""

# import required modules
# sqlite3 for SQL database queries
# tabulate to display it in table format
import sqlite3
# import traceback
# import sys
from tabulate import tabulate

book_ids = []
search_results = []


# Function to display all the records in the books table
def disp_func():
    # initilaize an empty list to store the results
    book_data = []
    # SQL statement to select all the records from the table
    disp_all_sql = "SELECT * FROM bookstore;"
    # Variable to store the result and iterate with for loop
    records = cursor.execute(disp_all_sql)
    print("Here is the current list of all books")
    # For loop to get all the data and store it in a list within list
    for id, title, author, qty in records:
        book_record = [id, title, author, qty]
        book_data.append(book_record)
    # Display the book table in a tabular format
    print(tabulate(book_data, headers=['BookID', 'Title', 'Author', 'Qty']))


# Function to check whether the queried book exists in the database or not
# This is to check the book exists before performing UPDATE on it
def book_exists(input_id):
    # SQL statement and query for the book id
    sql_getid = f"SELECT id FROM bookstore WHERE id = {input_id}"
    cursor.execute(sql_getid)
    # Reading the data in a variable
    retrieved_id = cursor.fetchone()
    # Exctracting the book id
    for i in retrieved_id:
        print(f"The ID retrieved from Database is {i}")

    # Validate if the Book id exists or not
    if i == input_id:
        print('Book Found')
        return True
    else:
        print("Sorry book not found, try again")
        return False


# Function to create a SEARCH result by the id/keywords
def search_exists(sql_stmt):
    # Execute the query and store the results in a variable
    cursor.execute(sql_stmt)
    retrieved_id = cursor.fetchall()
    # Iterate over the result and store it in a Search_result list
    # These variables are used Search operations
    for id, title, author, qty in retrieved_id:
        # Condition to avoid the duplicate search results
        if id not in book_ids:
            result_record = [id, title, author, qty]
            book_ids.append(id)
            search_results.append(result_record)


# Function to perform ENTER BOOK option
def enter_books():
    # Accept the inputs
    print("Please enter the book details, make sure Book IDs are unique")
    id = input("Enter the id of the book: ")
    name = input("Enter the name of the book: ")
    author = input("Enter the author of the book: ")
    qty = input("Enter the quantity of the book: ")
    # Check for the integers on id and qty can be converted to integers
    if not (id.isdigit() and qty.isdigit()):
        print("Id / quantity / both not interger, please retry...")
        return
    else:
        # If id and qty are integer then convert them to integers
        id = int(id)
        qty = int(qty)
    # Form SQL statement and execute, commit it
    sql_stmt = "INSERT INTO bookstore VALUES (?,?,?,?)"
    cursor.execute(sql_stmt, (id, name, author, qty))
    db.commit()
    print("Insert is successful")
    # Display the updated database
    disp_func()


# Function to handle the UPDATE BOOK operation
def update_books():
    # Users are given 5 options as shown below
    print("\t\t\tThis is Updatebook function")
    print("\t\t\t\t\tUPDATE MENU")
    update_option = (input('''Select the option - Key in the letter:
                     a. Update bookid
                     b. Update book name
                     c. Update book author
                     d. Update book name and author
                     e. Update book quantity
                     f. Go to Main Menu\n''')).lower()
    # This option accepts the book id and updates it
    if update_option == 'a':
        print("You have selected Update bookid")
        old_id = input("Enter the old id of the book that needs update: ")
        new_id = input("Enter the new id of this book: ")
        # Check the ids can be converted to inters
        if not (old_id.isdigit() and new_id.isdigit()):
            print("Old ID / New ID / both not interger, please retry...")
            return
        else:
            # Convert to integers
            old_id = int(old_id)
            new_id = int(new_id)
            # SQL stmt to update the book id
            if book_exists(old_id):
                sql_upd = f'''UPDATE bookstore SET id = {new_id}
                            WHERE id = {old_id};'''
            else:
                return
    # This option updates the book name
    elif update_option == 'b':
        # Accept the inputs
        print("You have selected Update book name")
        curr_id = input("Enter the book id that needs name update: ")
        new_name = input("Enter the new name of the book: ")
        # Check the ids can be converted to inters
        if not curr_id.isdigit():
            print("Book ID not an interger, please retry...")
            return
        else:
            # Convert to integers
            curr_id = int(curr_id)
            if book_exists(curr_id):
                # SQL stmt to update book name
                sql_upd = (f'''UPDATE bookstore SET Title = "{new_name}"
                           WHERE id = {curr_id};''')
            else:
                return
    # This option updates the book author
    elif update_option == 'c':
        # Accept inputs
        print("You have selected Update book author")
        curr_id = input("Enter the book id that needs author update: ")
        new_author = input("Enter the new author of the book: ")
        # Check the ids can be converted to inters
        if not curr_id.isdigit():
            print("Book ID not an interger, please retry...")
            return
        else:
            # integer conversion
            curr_id = int(curr_id)
            if book_exists(curr_id):
                # SQL logic to update book
                sql_upd = (f'''UPDATE bookstore SET Author = "{new_author}"
                           WHERE id = {curr_id};''')
            else:
                return
    # This option updates the book name and author
    elif update_option == 'd':
        # Accept the inputs
        print("You have selected Update book name and author")
        curr_id = input("Enter the book id that needs name & author update: ")
        new_name = input("Enter the new name of the book: ")
        new_author = input("Enter the new author of the book: ")
        # Check the ids can be converted to inters
        if not curr_id.isdigit():
            print("Book ID not an interger, please retry...")
            return
        else:
            # Convert it to integer
            curr_id = int(curr_id)
            if book_exists(curr_id):
                # SQL logic to update book
                sql_upd = (f'''UPDATE bookstore SET Author = "{new_author}",
                           Title = "{new_name}" WHERE id = {curr_id};''')
            else:
                return
    # This option updates the book qty
    elif update_option == 'e':
        # Accept the inputs
        print("You have selected Update book quantity")
        curr_id = input("Enter the book id that needs quantity update: ")
        new_qty = input("Enter the new qty of this book: ")
        # Check the id and qty can be converted to integers
        if not (curr_id.isdigit() and new_qty.isdigit()):
            print("Book ID / New Qty / both not interger, please retry...")
            return
        else:
            # Integer conversion
            curr_id = int(curr_id)
            new_qty = int(new_qty)
            if book_exists(curr_id):
                # SQL stmt to update the qty
                sql_upd = (f'''UPDATE bookstore SET Qty = {new_qty}
                           WHERE id = {curr_id};''')
            else:
                return
    # Option to go back to MAIN MENU
    elif update_option == 'f':
        print("You have selected Go to Main Menu!")
        return
    # INvalid choice
    else:
        print("You have made an incorrect choice, please try again")
        return

    # Once the SQL stmt is created, the below code execute and commit
    # to the database and also displays the updated records
    cursor.execute(sql_upd)
    db.commit()
    disp_func()
    print("Update Successful!")


# This function DELETEs the book using the book ID
def delete_books():
    # Accept the input
    print("This is Deletebook function")
    curr_id = input("Enter the book id which needs to be deleted: ")
    # Check the id can be converted to integer
    if not curr_id.isdigit():
        print("Book ID is not interger, please retry...")
        return
    else:
        # Integer conversion
        curr_id = int(curr_id)
        if book_exists(curr_id):
            # SQL statement to delete the book based on id
            sql_upd = f'DELETE from bookstore WHERE id = {curr_id};'
        else:
            return
    # Once the SQL stmt is created, the below code execute and commit
    # to the database and also displays the updated records
    print("about to execute the sql")
    cursor.execute(sql_upd)
    db.commit()
    disp_func()
    print("Delete Successful!")


# This function Searches for the book based on id and various keywords
def search_books():
    # Using the global variables and then initializing them
    global book_ids
    book_ids = []
    global search_results
    search_results = []
    # Search menu for the user
    print("\t\t\tThis is Search book function")
    print("\t\t\t\t\tSEARCH BOOK MENU")
    search_option = (input('''Select the option - Key in the letter:
                     a. Search by book id
                     b. Search by book name
                     c. Search by book author
                     d. Go to Main Menu\n''')).lower()
    # This option searches for the book based on id
    if search_option == 'a':
        # accept the inputs
        print("You have selected Search by book id")
        curr_id = input("Enter the book id that you want to search: ")
        # Valdate the id can be converted to integer
        if not curr_id.isdigit():
            print("Book id not interger, please retry...")
            return
        else:
            # Convert to integers
            curr_id = int(curr_id)
            # SQL stmt
            sql_search = f"SELECT * FROM bookstore WHERE id = {curr_id}"
            # Call the function to get all the search results
            search_exists(sql_search)
        # If the list is empty then book was not found
        if len(book_ids) == 0:
            print("Sorry book not found, try again")
            return
        # Display the search results
        print("\nHere are your search results:")
        print("------------------------------")
        print(tabulate(search_results,
                       headers=['BookID', 'Title', 'Author', 'Qty']))
    # Option to search based on book name using the keywords
    elif search_option == 'b':
        # Accept the keywords
        print("You have selected Search by book name")
        keywords = input("Enter the book name keywords "
                         "you want to search, separated by space: ")
        print("The keywords you entered are: ", keywords)
        # Split the words and append prefix and suffix by %
        # wild card % will be used in SQL query to do LIKE comparision
        sql_words = keywords.split()  # List of all keywords
        for index, i in enumerate(sql_words):
            sql_words[index] = '%' + i + '%'
        # for loop for each of the keyword search
        for j in sql_words:
            sql_search = f"SELECT * FROM bookstore WHERE Title like '{j}'"
            search_exists(sql_search)
            # Sort the search results
            search_results.sort()
        # No books found if the list is empty
        if len(book_ids) == 0:
            print("Sorry book not found, try again")
            return
        # Display the results
        print("\nHere are your search results:")
        print("------------------------------")
        print(tabulate(search_results,
                       headers=['BookID', 'Title', 'Author', 'Qty']))
    # OPtoin to search for the books based on Author keywords
    elif search_option == 'c':
        # Accept keywords from user for Author keyword search
        print("You have selected Search by book author")
        keywords = input("Enter the author name keywords "
                         "you want to search, separated by space: ")
        print("The keywords you entered are: ", keywords)
        # Split the words and append prefix and suffix by %
        # wild card % will be used in SQL query to do LIKE comparision
        sql_words = keywords.split()  # List of all keywords
        for index, i in enumerate(sql_words):
            sql_words[index] = '%' + i + '%'
        # for loop for each of the keyword search
        for j in sql_words:
            sql_search = f"SELECT * FROM bookstore WHERE Author like '{j}'"
            search_exists(sql_search)
            search_results.sort()
        # No books found if the list is empty
        if len(book_ids) == 0:
            print("Sorry book not found, try again")
            return
        # Display the results
        print("\nHere are your search results:")
        print("------------------------------")
        print(tabulate(search_results,
                       headers=['BookID', 'Title', 'Author', 'Qty']))
    # OPtion to go back to MAIN MENU
    elif search_option == 'd':
        print("You have selected Go to Main Menu!")
        return
    # Incorrect choice and go back
    else:
        print("You have made an incorrect choice, please try again")
        return


#########################
# Main Program
#########################
try:
    # Create a Database and get the cusrsor
    db = sqlite3.connect('book_store_db')
    cursor = db.cursor()

    # Created the bookstore table using this SQL code
    # I have left it in the code just so that you can see the SQL Stmts
    """
    sql_create_table = ("CREATE TABLE bookstore "
                        "(id INTEGER PRIMARY KEY UNIQUE, "
                        "Title VARCHAR(255), "
                        "Author VARCHAR(50), "
                        "Qty INTEGER);")
    cursor.execute(sql_create_table)

    # Insert al the rows required
    sql_stmt = ("INSERT INTO bookstore VALUES(3001, 'A Tale of Two Cities', "
               "'Charles Dickens', 31);")
    cursor.execute(sql_stmt)

    sql_stmt = ('''INSERT INTO bookstore VALUES(3002,
                "Harry Potter and the Philosopher's Stone",
                'J.K. Rowling', 40);''')
    cursor.execute(sql_stmt)
    sql_stmt = ('''INSERT INTO bookstore VALUES(3003,
                'The Lion, the Witch and the Wardrobe',
                'C. S. Lewis', 25);''')
    cursor.execute(sql_stmt)
    sql_stmt = ('''INSERT INTO bookstore VALUES(3004,
                'The Lord of the Rings',
                'J.R.R Tolkien', 37);''')
    cursor.execute(sql_stmt)
    sql_stmt = ('''INSERT INTO bookstore VALUES(3005,
                'Alice in Wonderland',
                'Lewis Carroll', 12);''')
    cursor.execute(sql_stmt)
    db.commit()
    """
    # Call to the display function which simply lists all the book records
    disp_func()

    # Starting a while loop to accept the user choice
    while True:
        print("\n\t\t\tInside the main program")
        print("\t\t\t\t\tMAIN MENU")
        option = input('''Enter number related to action to be performed:
                     1. Enter book
                     2. Update book
                     3. Delete book
                     4. Search book
                     0. Exit\n''')
        # Valdate the id can be converted to integer
        if not option.isdigit():
            print("Not an Interger, please retry...")
        else:
            # Convert to integer
            option = int(option)
            # Option to Enter a new book and call to the relavent function
            if option == 1:
                print("You have selected Enter Book")
                enter_books()
            # Option to Update a book and call to the relavent function
            elif option == 2:
                print("You have selected Update Book")
                update_books()
            # Option to Delete a book and call to the relavent function
            elif option == 3:
                print("You have selected Delete Book")
                delete_books()
            # Option to Search a book and call to the relavent function
            elif option == 4:
                print("You have selected Search Book")
                search_books()
            # Option to Exit the program
            elif option == 0:
                print("You have selected Exit...Goodbye!")
                break
            # Invalid choice
            else:
                print("You have made an incorrect choice, please try again")
# This exception is defined for unique contsraint violation on id column
except sqlite3.IntegrityError:
    print("The book ID already exists, please try again later")
# This is for all the other violations
except Exception as e:
    print(e)
# Finally clause to close the connection
finally:
    db.close()
    print("All done")
