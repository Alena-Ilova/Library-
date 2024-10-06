from Library import Book


books = [
    Book("Society of lies", "Lauren Ling Brown", 2024, 14.99),
    Book("How to speak about art in English", "Falkovich", 1949, 15.99),
    Book("To Kill a Mockingbird", "Harper Lee", 1960, 12.99),
    Book("The Catcher in the Rye", "J.D. Salinger", 1951, 8.99),
    Book("Dracula", "Bram Stoker", 1897, 5.99)
]


print("Information about each book:")
for book in books:
    book.get_info()


most_expensive_book = Book.find_most_expensive(books)
print("\nMost expensive book:")
if most_expensive_book:
    most_expensive_book.get_info()
else:
    print("No books available.")


print("\nSetting stoplist for '1984' to True:")
for book in books:
    book.censor("George Orwell", True)


print("\nInformation after censorship:")
for book in books:
    book.get_info()