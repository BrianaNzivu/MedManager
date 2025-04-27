# This file defines routes for rendering the dashboard, displaying client and program statistics.

from flask import Blueprint, render_template
from routes.client_service import get_clients
from routes.program_service import get_programs

dashboard_bp = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard_bp.route('/')
@dashboard_bp.route('/dashboard')
def dashboard():
    clients = get_clients()
    programs = get_programs()
    return render_template(
        'dashboard.html',
        total_clients=len(clients),
        total_programs=len(programs),
        enrolled_clients=sum(bool(c.get('enrolled_programs')) for c in clients)
    )
