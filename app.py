from flask import Flask, jsonify, request
import json
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Load data from JSON files
def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

users = load_data('users.json')
books = load_data('books.json')
rentals = load_data('rentals.json')

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/rentals', methods=['GET', 'POST'])
def handle_rentals():
    if request.method == 'GET':
        return jsonify(rentals)
    elif request.method == 'POST':
        rental = request.json
        rentals.append(rental)
        save_data('rentals.json', rentals)
        return jsonify(rental), 201

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Pega a porta do ambiente ou usa 5000 como padrão
    app.run(host='0.0.0.0', port=port)  # Permite que o app seja acessado externamente