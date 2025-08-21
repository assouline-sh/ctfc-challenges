from flask import Flask, request, render_template_string

app = Flask(__name__)

FLAG = "CTF{w3lc0me_t0_th3_p4rty!}"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Join the Party! but...</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1e1e2f;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background-color: #2a2a40;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        }
        h1 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #ff6f61;
        }
        p {
            font-size: 1.2rem;
            margin: 0.5rem 0;
        }
        .flag {
            font-size: 1.5rem;
            color: #4caf50;
            font-weight: bold;
            margin-top: 1.5rem;
        }
        .error {
            color: #ff6f61;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Join the Party! But...</h1>
        <p>{{ message }}</p>
        {% if flag %}
            <p class="flag">{{ flag }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Step 1: Check User-Agent
    user_agent = request.headers.get('User-Agent')
    if user_agent != 'neu-ctf-club':
        return render_template_string(HTML_TEMPLATE, message="You must be an agent of neu-ctf-club secure browser!")

    # Step 2: Check Accept
    accept = request.headers.get('Accept')
    if accept != 'fl4g':
        return render_template_string(HTML_TEMPLATE, message="You must be open to Accept fl4g but you don't right now")

    # Step 3: Check Connection
    connection = request.headers.get('Connection')
    if connection != 's3cur3':
        return render_template_string(HTML_TEMPLATE, message="Your connection must be s3cur3")

    # Step 4: Check Referer
    referer = request.headers.get('Referer')
    if referer != 'the.bouncer':
        return render_template_string(HTML_TEMPLATE, message="You must be referred to by the.bouncer")

    # Step 5: Check Give-Flag
    give_flag = request.headers.get('Give-Flag')
    if give_flag:
        if give_flag != '7ru3':
            return render_template_string(HTML_TEMPLATE, message="Your Give-Flag must be 7ru3")

    # All checks passed, return the flag
    return render_template_string(HTML_TEMPLATE, message="Congratulations! Here's your flag:", flag=FLAG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5432)
