from firebase_config import db

def add_client(client_data):
    return db.collection('clients').add(client_data)

def get_clients():
    docs = db.collection('clients').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]

def get_client_by_id(client_id):
    doc = db.collection('clients').document(client_id).get()
    return doc.to_dict() if doc.exists else None

def add_program(program_data):
    return db.collection('programs').add(program_data)

def get_programs():
    docs = db.collection('programs').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]
