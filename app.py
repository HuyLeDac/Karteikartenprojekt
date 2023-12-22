from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates')

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

if __name__ == '__main__':
    app.run(debug=True)