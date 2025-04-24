import firebase_admin
from firebase_admin import credentials, firestore
import os

# Path to your downloaded service account key
KEY_PATH = os.path.join(os.path.dirname(__file__), 'firebase-key.json')

cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred)

db = firestore.client()
