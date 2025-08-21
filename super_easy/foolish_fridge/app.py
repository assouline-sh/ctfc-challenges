from flask import Flask, request
from urllib.parse import urlparse

FLAG = "CTF{I_c0ntr0l_th3_fr1dg3!}"
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    page = """
<html>
<head>
    <title>IOT</title>
</head>
<body style="text-align:center;">
    <br><br>
    <h1>INTERNET OF THINGS</h1>
    <p>You know your family has some great treasures hidden in their Samsung smart refrigerator... See if you can connect to their device over wifi and see what you find. 
    <br><br><br>
    <h2>Login</h2>
    <form action="/adminflag" method="POST">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Submit">
    </form>
    <img src="https://i.insider.com/612fc7289ef1e50018f93bec?width=2000&format=jpeg&auto=webp">
</body>
</html>
    """
    return page


@app.route('/adminflag',methods = ['POST'])
def link():
    # get user input
    try:
        password = request.form['password']
    except:
        return "No Form Submitted"

    if password == "1111122222":
        page = f"""
<html>
<head>
    <title>IOT</title>
</head>
<body style="text-align:center;">
    <br><br>
    <h1>INTERNET OF THINGS</h1>
    <p> This is what happens if you don't change the default credentials for your smart devices! </p>
    <p>{FLAG} </p>

</body>
</html>
        """
        return page
    else:
        return "Invalid Credentials"



    # if all checks are passed, then 'urmom' is in the fragment!
    return FLAG


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40006)