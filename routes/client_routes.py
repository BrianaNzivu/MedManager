from flask import Blueprint, render_template, request, redirect, url_for
from services.client_service import add_client, get_clients, get_client
from services.program_service import get_programs

client_bp = Blueprint('clients', __name__, template_folder='templates')

@client_bp.route('/', methods=['GET', 'POST'])
def clients():
    if request.method == 'POST':
        add_client({
            'name': request.form['name'],
            'age': int(request.form['age']),
            'gender': request.form['gender'],
            'enrolled_programs': request.form.getlist('programs')
        })
        return redirect(url_for('clients.clients'))

    return render_template(
        'clients.html',
        clients=get_clients(),
        programs=get_programs()
    )

@client_bp.route('/<client_id>')
def client_profile(client_id):
    client = get_client(client_id)
    return render_template('client_profile.html', client=client)
