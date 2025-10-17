import sqlite3
import os

class LibrarySystem:
    def __init__(self):
        # Create 'database' folder if it does not exist
        if not os.path.exists("database"):
            os.makedirs("database")
        self.setup_database()

    def setup_database(self):
        conn = sqlite3.connect("database/library.db")
        c = conn.cursor()

        # Create table if it does not exist
        c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            isbn TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            is_available INTEGER
        )
        ''')

        conn.commit()
        conn.close()
        print("Database and table created successfully.")

    def add_book(self, isbn, title, author):
        """Add a new book."""
        try:
            conn = sqlite3.connect("database/library.db")
            c = conn.cursor()
            c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
                      (isbn, title, author, 1))
            conn.commit()
            conn.close()
            print(f" Book added: {title} ({author})")

        except sqlite3.IntegrityError:
            print("⚠️ This ISBN already exists!")

    def show_books(self):
        """List all books."""
        conn = sqlite3.connect("database/library.db")
        c = conn.cursor()

        c.execute("SELECT * FROM books")
        books = c.fetchall()  # Fetch all records
        conn.close()

        if len(books) == 0:
            print("📭 No books have been added yet.")
        else:
            print("\n--- 📚 BOOK LIST ---")
            for book in books:
                isbn, title, author, is_available = book
                status = "Available ✅" if is_available == 1 else "Borrowed ❌"
                print(f"ISBN: {isbn} | {title} - {author} | Status: {status}")
            print("----------------------------\n")

    def borrow_book(self, isbn):
        """Borrow a book by ISBN."""
        conn = sqlite3.connect("database/library.db")
        c = conn.cursor()

        c.execute("SELECT is_available FROM books WHERE isbn = ?", (isbn,))
        result = c.fetchone()

        if result is None:
            print("❌ No book found with this ISBN.")
        elif result[0] == 0:
            print(" This book is already borrowed!")
        else:
            c.execute("UPDATE books SET is_available = 0 WHERE isbn = ?", (isbn,))
            conn.commit()
            print(" Book borrowed successfully!")

        conn.close()

    def return_book(self, isbn):
        """Return a borrowed book."""
        conn = sqlite3.connect("database/library.db")
        c = conn.cursor()

        c.execute("SELECT is_available FROM books WHERE isbn = ?", (isbn,))
        result = c.fetchone()

        if result is None:
            print("❌ No book found with this ISBN.")
        elif result[0] == 1:
            print(" This book is already in the library!")
        else:
            c.execute("UPDATE books SET is_available = 1 WHERE isbn = ?", (isbn,))
            conn.commit()
            print(" Book returned successfully!")

        conn.close()

    def search_books(self, keyword):
        """Search books by title or author."""
        conn = sqlite3.connect("database/library.db")
        c = conn.cursor()

        c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", 
                  (f"%{keyword}%", f"%{keyword}%"))
        books = c.fetchall()
        conn.close()

        if not books:
            print(f"❌ No books found matching '{keyword}'.")
        else:
            print(f"\n🔍 Search Results for '{keyword}':")
            for book in books:
                isbn, title, author, is_available = book
                status = "Available ✅" if is_available else "Borrowed ❌"
                print(f"ISBN: {isbn} | {title} - {author} | Status: {status}")
            print("----------------------------\n")


def main_menu():
    library = LibrarySystem()

    while True:
        print("\n=== LIBRARY MENU ===")
        print("1. Add a book")
        print("2. Show all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Search for a book")
        print("6. Exit")

        choice = input("Your choice (1-6): ")

        if choice == "1":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(isbn, title, author)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            isbn = input("Enter ISBN of the book to borrow: ")
            library.borrow_book(isbn)

        elif choice == "4":
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)

        elif choice == "5":
            keyword = input("Enter a keyword to search (title or author): ")
            library.search_books(keyword)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("⚠️ Invalid choice! Please enter a number between 1-6.")


if __name__ == "__main__":
    main_menu()
