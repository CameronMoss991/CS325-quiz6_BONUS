from abc import ABC, abstractmethod

# Interfaces for different types of users

class GuestUser(ABC):
    @abstractmethod
    def search_book(self, title: str, author: str, genre: str):
        print("Guest User: Search book")

class RegisteredUser(ABC):
    @abstractmethod
    def search_book(self, title: str, author: str, genre: str):
        print("User: Search book")

    @abstractmethod
    def borrow_book(self, book_id: str):
        print("User: Borrow book")

    @abstractmethod
    def return_book(self, book_id: str):
        print("User: Return book")

class Librarian(ABC):
    @abstractmethod
    def search_book(self, title: str, author: str, genre: str):
        print("Librarian: Search book")

    @abstractmethod
    def borrow_book(self, book_id: str):
        print("Librarian: Borrow book")

    @abstractmethod
    def return_book(self, book_id: str):
        print("Librarian: Return book")

    @abstractmethod
    def add_book(self, title: str, author: str, genre: str):
        print("Librarian: Add book")

    @abstractmethod
    def remove_book(self, book_id: str):
        print("Librarian: Remove book")

    @abstractmethod
    def generate_reports(self):
        print("Librarian: Generate reports")

# Implementations of the interfaces

class GuestUserImpl(GuestUser):
    def search_book(self, title: str, author: str, genre: str):
        print(f"Searching for books: title='{title}', author='{author}', genre='{genre}'")

class RegisteredUserImpl(RegisteredUser):
    def search_book(self, title: str, author: str, genre: str):
        print(f"Searching for books: title='{title}', author='{author}', genre='{genre}'")

    def borrow_book(self, book_id: str):
        print(f"Borrowing book with ID '{book_id}'")

    def return_book(self, book_id: str):
        print(f"Returning book with ID '{book_id}'")

class LibrarianImpl(Librarian):
    def search_book(self, title: str, author: str, genre: str):
        print(f"Searching for books: title='{title}', author='{author}', genre='{genre}'")

    def borrow_book(self, book_id: str):
        print(f"Borrowing book with ID '{book_id}'")

    def return_book(self, book_id: str):
        print(f"Returning book with ID '{book_id}'")

    def add_book(self, title: str, author: str, genre: str):
        print(f"Adding book: title='{title}', author='{author}', genre='{genre}'")

    def remove_book(self, book_id: str):
        print(f"Removing book with ID '{book_id}'")

    def generate_reports(self):
        print("Generating reports")


def main():
    guest_user = GuestUserImpl()
    registered_user = RegisteredUserImpl()
    librarian = LibrarianImpl()

    guest_user.search_book("Lord Of The Rings", "J.R.R Tolkein", "Fantasy, Adventure")
    registered_user.borrow_book("1234")
    librarian.generate_reports()

if __name__ == "__main__":
    main()
