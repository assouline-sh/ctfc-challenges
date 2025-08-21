from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

VALID_USER_AGENT = "CTFC2THEMOON"

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
	user_agent = request.headers.get('User-Agent')
    
	if user_agent == VALID_USER_AGENT:
		return render_template('flag.html')
	return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == "admin" and password == "password":
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials. Please try again."
	

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1338)

