from flask import render_template, request, redirect, flash
from app import app
from models.book import Book
from models.book_list import book_list, add_new_book, remove_book, get_book_by_title, check_out

@app.route('/our-books')
def index():
    return render_template('index.jinja', title="Our Books", book_list=book_list)

# for viewing individual book information
@app.route('/our-books/<path:book_title>')
def book(book_title):
    title = book_title.replace('-', ' ')
    book = get_book_by_title(title)
    return render_template('book.jinja', title="More About This Book", book=book)

# for adding a book to the library
@app.route('/our-books', methods = ['POST'])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = True if "checked out" in request.form else False
    new_book = Book(title, author, genre, checked_out)
    add_new_book(new_book)
    return redirect('/our-books')

# for deleting a book from the library - though this is not working
@app.route('/our-books/<path:book_title>/remove', methods = ['POST'])
def remove(book_title):
    remove_book(book_title)
    return redirect('/our-books')


@app.route('/about')
def about():
    return render_template('about.jinja', title="About Us")

@app.route('/contact')
def contact():
    return render_template('contact.jinja', title="Contact Us")

# @app.route('/our-books/<path:book_title', methods = ['POST'])›
# def check_out_book(book_title):
#     check_out(book_title)
#     return redirect ('/our-books/<path:book_title>')


