# This file provides service functions for interacting with the 'programs' collection in the database.

from firebase_config import db

def add_program(data):
    return db.collection('programs').add(data)

def get_programs():
    docs = db.collection('programs').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]
