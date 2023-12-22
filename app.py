import json
import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates')

# Laden der Dummy-Anmeldedaten aus der JSON-Datei
json_file_path = os.path.join(os.path.dirname(__file__), "anmeldedaten_dummy.json")
# Laden der Dummy-Anmeldedaten aus der JSON-Datei
with open(json_file_path) as json_file:
    anmeldedaten = json.load(json_file)


@app.route('/')
def welcome_page():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # Handle the POST request here
        return jsonify({'redirect': '/login'})
    else:
        # Render the login page for a GET request
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        # Handle the POST request here
        return jsonify({'redirect': '/register'})
    else:
        return render_template('register.html')

@app.route('/check_anmeldung', methods=['POST'])
def check_anmeldung():
    benutzername = request.form.get('benutzername')
    passwort = request.form.get('passwort')

    # Überprüfe die Anmeldedaten
    if benutzername in anmeldedaten and anmeldedaten[benutzername]['passwort'] == passwort:
        return jsonify({'success': True, 'message': 'Anmeldung erfolgreich!', 'redirect': '/dashboard'})
    else:
        return jsonify({'success': False, 'message': 'Ungültige Anmeldedaten.'})


#TODO: Route für Resgistrierung

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)