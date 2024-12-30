import csv

BOOKS_FILE = "books.csv"  # Book details file
Library_Members = "members.csv"  # Library members details file


def add_borrower():
    borrower_id = input("Enter Borrower ID: ")
    borrower_name = input("Borrower Name: ")
    borrow_status = "No"
    borrowed_books = " "

    with open(Library_Members, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([borrower_id, borrower_name, borrow_status, borrowed_books])
    print(f"Library member '{borrower_name}' added successfully!")


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    availability = "Yes"
    borrower_id = " "

    with open(BOOKS_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, availability, borrower_id])
    print(f"Book '{title}' added successfully!")


def display_books():
    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)
        books = list(reader)
        if len(books) <= 1:
            print("No books found.")
            return
        print("\nAvailable Books:")
        print("{:<10} {:<50} {:<20} {:<15} {:<15}".format("ID", "Title", "Author", "Availability", "Borrower ID"))
        for book in books[1:]:
            print("{:<10} {:<50} {:<20} {:<15} {:<15}".format(*book))


def display_borrowers():
    with open(Library_Members, "r") as file:
        reader = csv.reader(file)
        borrowers = list(reader)
        if len(borrowers) <= 1:
            print("No borrowers found.")
            return
        print("\nList of Borrowers:")
        print("{:<10} {:<20} {:<15} {:<30}".format("Member ID", "Name", "Borrow Status", "Borrowed Book ID"))
        for borrower in borrowers[1:]:
            print("{:<10} {:<20} {:<15} {:<30}".format(*borrower))


def borrow_book():
    book_id = input("Enter Book ID to borrow: ")
    borrower_id = input("Enter Borrower ID: ")

    books = []
    book_found = False
    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == book_id and row[3] == "Yes":
                row[3] = "No"
                row[4] = borrower_id
                book_found = True
            books.append(row)

    borrowers = []
    borrower_found = False
    with open(Library_Members, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == borrower_id and row[2] == "No":
                row[2] = "Yes"
                row[3] = book_id
                borrower_found = True
            borrowers.append(row)

    # Write updates back to files
    if book_found and borrower_found:
        with open(BOOKS_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)

        with open(Library_Members, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(borrowers)

        print(f"Book '{book_id}' borrowed successfully by Borrower '{borrower_id}'.")
    else:
        print("Unable to borrow book. Check book availability or borrower details.")


def return_book():
    book_id = input("Enter Book ID to return: ")
    borrower_id = input("Enter Borrower ID: ")

    books = []
    book_found = False
    with open(BOOKS_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == book_id and row[3] == "No" and row[4] == borrower_id:
                row[3] = "Yes"
                row[4] = ""
                book_found = True
            books.append(row)

    borrowers = []
    borrower_found = False
    with open(Library_Members, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == borrower_id and row[2] == "Yes" and row[3] == book_id:
                row[2] = "No"
                row[3] = ""
                borrower_found = True
            borrowers.append(row)

    if book_found and borrower_found:
        with open(BOOKS_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)

        with open(Library_Members, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(borrowers)

        print(f"Book '{book_id}' returned successfully by Borrower '{borrower_id}'.")
    else:
        print("Unable to return book. Check book or borrower details.")


def interface():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Borrower")
        print("3. Display Books")
        print("4. Display Borrowers")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            add_borrower()
        elif choice == "3":
            display_books()
        elif choice == "4":
            display_borrowers()
        elif choice == "5":
            borrow_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


interface()
