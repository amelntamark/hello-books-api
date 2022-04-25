from flask import Blueprint, jsonify

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description 

books = [
    Book(1, "Jane Eyre", "Classic"),
    Book(2, "Dune", "Science Fiction"),
    Book(3, "My Year of Rest and Relaxation", "Fiction"),
    Book(4, "Manufacturing Consent", "Nonfiction")
]

@books_bp.route("", methods=["GET"])
def get_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response), 200