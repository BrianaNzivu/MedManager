import os
from flask import Flask, render_template, request, redirect, url_for
from firestore_service import (
    get_clients, add_client, update_client, delete_client, get_client,
    get_programs, add_program, get_program
)

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR   = os.path.join(BASE_DIR, 'static')

app = Flask(__name__,
            template_folder=TEMPLATE_DIR,
            static_folder=STATIC_DIR)

# ── Dashboard ────────────────────────────────────────────────────────────────
@app.route('/')
@app.route('/dashboard')
def dashboard():
    clients  = get_clients()
    programs = get_programs()

    total_clients    = len(clients)
    total_programs   = len(programs)
    enrolled_clients = sum(1 for c in clients if c.get('enrolled_programs'))

    # Chart.js data
    labels = [p['name'] for p in programs]
    counts = [sum(1 for c in clients if p['name'] in c.get('enrolled_programs', []))
              for p in programs]
    colors = [p.get('color','#0d6efd') for p in programs]

    return render_template('dashboard.html',
        total_clients=total_clients,
        total_programs=total_programs,
        enrolled_clients=enrolled_clients,
        program_labels=labels,
        program_counts=counts,
        program_colors=colors
    )

# ── Clients (List + Create) ─────────────────────────────────────────────────
@app.route('/clients', methods=['GET', 'POST'])
def clients():
    if request.method == 'POST':
        add_client({
            'name': request.form['name'],
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'enrolled_programs': request.form.getlist('programs')
        })
        return redirect(url_for('clients'))

    return render_template('clients.html',
                           clients=get_clients(),
                           programs=get_programs())

# ── Client Profile / Update / Delete ────────────────────────────────────────
@app.route('/clients/<client_id>', methods=['GET', 'POST'])
def client_profile(client_id):
    if request.method == 'POST':
        update_client(client_id, {
            'name': request.form['name'],
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'enrolled_programs': request.form.getlist('programs')
        })
        return redirect(url_for('clients'))

    return render_template('client_profile.html',
                           client=get_client(client_id),
                           programs=get_programs())

@app.route('/clients/<client_id>/delete', methods=['POST'])
def client_delete(client_id):
    delete_client(client_id)
    return redirect(url_for('clients'))

# ── Programs (List + Create) ────────────────────────────────────────────────
@app.route('/programs', methods=['GET', 'POST'])
def programs():
    if request.method == 'POST':
        add_program({
            'name':   request.form['name'],
            'status': request.form['status'],
            'color':  request.form['color']
        })
        return redirect(url_for('programs'))

    return render_template('programs.html',
                           programs=get_programs())

# ── Program Detail (Clients in a Program) ──────────────────────────────────
@app.route('/programs/<program_id>')
def program_detail(program_id):
    program = get_program(program_id)
    if not program:
        return "Program not found", 404
    clients = [c for c in get_clients()
               if program['name'] in c.get('enrolled_programs',[])]
    return render_template('program_detail.html',
                           program=program,
                           clients=clients)

if __name__ == '__main__':
    app.run(debug=True)
