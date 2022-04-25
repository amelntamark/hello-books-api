from flask import Blueprint, jsonify

books_bp = ("books_bp", __name__, "/books")

@books.route("", methods=["GET"])
def get_books():
    books_response = []
    return jsonify(books_response)