from firebase_config import db

def add_client(data):
    return db.collection('clients').add(data)

def get_clients():
    docs = db.collection('clients').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]

def get_client(client_id):
    doc = db.collection('clients').document(client_id).get()
    return doc.to_dict() if doc.exists else None
