class book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.status = 'available'

    def display_book(self):
        print(self.title)
        print(self.author)
        print(self.book_id)
        print(self.status)

    def borrow_book(self):
        if self.status == 'available':
            self.status = 'borrowed'
            print('book borrowed successfully')
        else:
             print('book alrady borrowed')

    def return_book(self):
        if self.status == 'borrowed':
           self.status = 'available'
           print('book return successfully')
        else:
            print('book are not borrowed')

class library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print('Book added successfully')

    def show_books(self):
        total_book = 0
        available_book = 0
        borrow_book = 0

        
        for book_id, book in self.books.items():
            total_book += 1
            if book.status == 'available':
                available_book += 1
                print('available book id:', book_id)
                
            elif book.status == 'borrowed':
                borrow_book += 1

        print('totla book:', total_book)
        print('avilable book:',  available_book)
        print('borrowed book:',  borrow_book)

    def search_book(self):
        book_id = int(input('Enter book id'))

        if book_id in self.books:
            book = self.books[book_id]

            print('book in the library')

            if book.status == 'available':
                print('book is available')
            else:
                print('book are borrowed')
        else:
            print('book are not in the library')

    def borrow_book(self):
        book_id = int(input('enter book id'))

        if book_id in self.books:
           book = self.books[book_id]
           book.borrow_book()
                    
        else:
            print('book is not in library')

    def return_book(self):
        book_id = int(input('enter book id'))

        if book_id in self.books:
            book = self.books[book_id]
            book.return_book()
        else:
            print('book not in library')
        
book1 = book('Python', 'Riyad', 101)
book2 = book('Java', 'Rihan', 102)
book3 = book('C++', 'Rifat', 103)
book4 = book('Javascript', 'Rahib', 104)
book5 = book('Data science', 'Riyaz', 105)

lib = library()

while True:
    print('\n===== Library Management System =====')
    print('1. Show Books')
    print('2. Search Book')
    print('3. Borrow Book')
    print('4. Return Book')
    print('5. Exit')

    choice = int(input('\nEnter your choice: '))

    if choice == 1:
        lib.show_books()

    elif choice == 2:
        lib.search_book()

    elif choice == 3:
        lib.borrow_book()

    elif choice == 4:
        lib.return_book()

    elif choice == 5:
        print('Thank you for using Library Management System')
        break

    else:
        print('Invalid choice! Please try again.')

    print()
