from firebase_config import db

def add_client(data):
    """Add a new client document to Firestore."""
    return db.collection('clients').add(data)

def get_clients():
    """Return all clients as a list of dicts with Firestore IDs."""
    docs = db.collection('clients').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]

def get_client(client_id):
    """Fetch a single client by ID, or None if it doesn’t exist."""
    doc = db.collection('clients').document(client_id).get()
    return doc.to_dict() if doc.exists else None

def add_program(data):
    """Add a new program document to Firestore."""
    return db.collection('programs').add(data)

def get_programs():
    """Return all programs as a list of dicts with Firestore IDs."""
    docs = db.collection('programs').stream()
    return [{**doc.to_dict(), 'id': doc.id} for doc in docs]
