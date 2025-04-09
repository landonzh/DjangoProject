import firebase_admin
from firebase_admin import credentials, db
import os

# Path to the serviceAccountKey.json file
cred_path = os.environ.get("FIREBASE_CREDENTIALS_PATH")
current_directory = os.path.dirname(os.path.abspath(__file__))

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(cred_path)
# Reference to the Realtime Database
database_ref = db.reference()
# Function to add a user to Firebase
def add_user_to_firebase(name, email):
    user_ref = database_ref.child('users').push({
        'name': name,
        'email': email
    })
    return user_ref
# Function to retrieve all users from Firebase
def get_users_from_firebase():
    users_ref = database_ref.child('users')
    users = users_ref.get() # Fetch all users from the database
    return users

