from models.book import Book

book_1 = Book("The Twits", "Roald Dahl", "Children's", True)
book_2 = Book("Warrior Errant", "Harry Elliot", "Science Fiction", False)
book_3 = Book("Tishomingo Blues", "Elroy Leonard", "Crime", False)
book_4 = Book("Slugfest", "Reed Tucker", "History", True)
book_5 = Book("Choke", "Chuck Palahniuk", "Fiction", False)
book_6 = Book("Babel", "R. F. Kuang", "Fantasy", False)

book_list = [book_1, book_2, book_3, book_4, book_5, book_6]

def list_all_books(list_of_books):
    for book in list_of_books:
        return book.title
    
def add_new_book(new_book):
    book_list.append(new_book)

def remove_book(book_title):
    for book in book_list:
        if book.title == book_title:
            book_list.remove(book)
            break 
        
def get_book_by_title(book_title):
    for book in book_list:
        if book.title == book_title:
            return book

