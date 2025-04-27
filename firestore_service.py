from firebase_config import db

def add_client(data):
    return db.collection('clients').add(data)

def get_clients():
    docs = db.collection('clients').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]

def get_client(client_id):
    doc = db.collection('clients').document(client_id).get()
    return {**doc.to_dict(), 'id': doc.id} if doc.exists else None

def update_client(client_id, data):
    return db.collection('clients').document(client_id).update(data)

def delete_client(client_id):
    return db.collection('clients').document(client_id).delete()

def add_program(data):
    return db.collection('programs').add(data)

def get_programs():
    docs = db.collection('programs').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]

def get_program(program_id):
    doc = db.collection('programs').document(program_id).get()
    return doc.to_dict() if doc.exists else None
