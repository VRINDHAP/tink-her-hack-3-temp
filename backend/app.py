from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory dictionary to store user data (email -> password)
users_db = {}

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()  # Get JSON data from the request
    email = data.get('email')
    password = data.get('password')

    # Check if email or password is missing
    if not email or not password:
        return jsonify({"error": "Email and password are required!"}), 400

    # Check if the user already exists in the dictionary
    if email in users_db:
        return jsonify({"error": "User with this email already exists!"}), 400

    # Store the user data (email and password) in the dictionary
    users_db[email] = password

    # For demonstration purposes, we'll print the dictionary content
    print(f"Users Database: {users_db}")

    return jsonify({"message": "Sign-up successful!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get JSON data from the request
    email = data.get('email')
    password = data.get('password')

    # Check if email or password is missing
    if not email or not password:
        return jsonify({"error": "Email and password are required!"}), 400

    # Validate user credentials
    if email not in users_db or users_db[email] != password:
        return jsonify({"error": "Invalid email or password!"}), 400

    return jsonify({"message": "Login successful!"})

if __name__ == '__main__':
    app.run(debug=True)
