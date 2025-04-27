# This file provides service functions for interacting with the clients collection in the database.
from firebase_config import db

#Add a new client to the database
def add_client(data):
    return db.collection('clients').add(data)

#Retrieve all clients from the database
def get_clients():
    docs = db.collection('clients').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]

# Retrieve specific client
def get_client(client_id):
    doc = db.collection('clients').document(client_id).get()
    return doc.to_dict() if doc.exists else None
