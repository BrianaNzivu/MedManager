from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/programs')
def programs():
    return render_template('programs.html')

if __name__ == '__main__':
    app.run(debug=True)
