import json
import hashlib

USERS_FILE = "users.json"

def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    users = load_users()
    hashed = hash_password(password)
    for user in users:
        if user["username"] == username and user["password"] == hashed:
            return True
    return False

def register_user(username, password):
    users = load_users()
    users.append({
        "username": username,
        "password": hash_password(password)
    })
    save_users(users)
