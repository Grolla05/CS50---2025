from cs50 import SQL
from flask import Flask, render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)

db = SQL("sqlite:///store.db")                                                  # Connect to SQLite database

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)                                                                    # Initialize session management

@app.route("/")
def index():
    books = db.execute("SELECT * FROM books")                                   # Query all books from the database
    return render_template("books.html", books=books)                           # Render the index template with the list of books

@app.route("/cart", methods=["GET", "POST"])
def cart():

    if "cart" not in session:                                                   # Initialize cart in session if it doesn't exist
        session["cart"] = []

    if request.method == "POST":
        book_id = request.form.get("book_id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")                                                # Redirect to cart after adding a book

    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])  # Get books in the cart
    return render_template("cart.html", books=books)                            # Render the cart template with the books in the cart
