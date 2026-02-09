class Library:
    def __init__(self):
        self.books = ["Python Basics", "Data Science 101", "SQL Guide"]

    def show_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f"- {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Success! You borrowed '{book_name}'")
        else:
            print("Sorry, book not available.")

my_lib = Library()
my_lib.show_books()
book = input("\nEnter book name to borrow: ")
my_lib.borrow_book(book)
