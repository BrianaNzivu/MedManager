import os
from flask import Flask, render_template
from firestore_service import get_clients, get_programs, get_client

# point Flask at the correct folders:
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR   = os.path.join(BASE_DIR, 'static')

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    clients = get_clients()
    programs = get_programs()
    enrolled_clients = sum(1 for c in clients if c.get('enrolled_programs'))
    return render_template(
        'dashboard.html',
        total_clients=len(clients),
        total_programs=len(programs),
        enrolled_clients=enrolled_clients
    )

@app.route('/clients')
def clients():
    clients_list = get_clients()
    return render_template('clients.html', clients=clients_list)

@app.route('/clients/<client_id>')
def client_profile(client_id):
    client = get_client(client_id)
    if not client:
        return "Client not found", 404
    return render_template('client_profile.html', client=client)

@app.route('/programs')
def programs():
    programs_list = get_programs()
    return render_template('programs.html', programs=programs_list)

if __name__ == '__main__':
    app.run(debug=True)
