from flask import Flask, request, make_response
from urllib.parse import urlparse

FLAG = "byuctf{dirb_is_the_loml}"
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    page = """
<html>
<head>
    <title>Ice Cream Shop!</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 2.5em;
            color: #ff6f61;
            margin-top: 20px;
        }
        p {
            font-size: 1.2em;
            color: #555;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            font-size: 1.2em;
            margin: 10px 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
        .featured {
            background-color: #fff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
            max-width: 800px;
        }
        .flavor-img {
            width: 300px;
            height: 200px;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <br><br>
    <h1>Welcome to My Ice Cream Shop!</h1>
    <p>We have lots of flavors, so feel free to look around!</p>
    <ul>
        <li>/Chocolate</li>
        <li>/Vanilla</li>
        <li>/Strawberry</li>
        <li>And more!</li>
    </ul>
    <br><br>
    <div class="featured">
        <h2>This Month's Featured Flavor:</h2>
        <h3>Ice Cream Sandwich Flavored Ice Cream</h3>
        <img src="https://cdn.tasteatlas.com/images/dishes/dd8a8aba1b914240a13336fa48af6700.jpg" width="600" height="400">
    </div>
</body>
</html>
    """
    return page

@app.route('/vanilla', methods=['GET'])
def vanilla():
    page = """
<html>
<head>
    <title>Vanilla Ice Cream</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>Vanilla Ice Cream</h1>
    <img src="https://images.getrecipekit.com/20230327191311-Vanilla%2520Ice%2520Cream.jpg?width=650&quality=90&" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/chocolate', methods=['GET'])
def chocolate():
    page = """
<html>
<head>
    <title>Chocolate Ice Cream</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>Chocolate Ice Cream</h1>
    <img src="https://sugarpursuit.com/wp-content/uploads/2023/05/Chocolate-ice-cream-thumbnail.jpg" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/strawberry', methods=['GET'])
def strawberry():
    page = """
<html>
<head>
    <title>Strawberry Ice Cream</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>Strawberry Ice Cream</h1>
    <img src="https://butterandbliss.net/wp-content/uploads/2022/05/Dairy-Free-Strawberry-Ice-Cream-BUTTERANDBLISS-6-of-10.jpg" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/flag', methods=['GET'])
def flag():
    page = """
<html>
<head>
    <title>CTF{</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>CTF{</h1>
    <img src="https://www.daringgourmet.com/wp-content/uploads/2023/07/Cookies-and-Cream-Ice-Cream-Recipe-3.jpg" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/zimbra', methods=['GET'])
def zimbra():
    page = """
<html>
<head>
    <title>w3ll_n</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>w3ll_n</h1>
    <img src="https://www.davidlebovitz.com/wp-content/uploads/2016/08/Salted-butter-caramel-ice-cream-recipe-6.jpg" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/2013', methods=['GET'])
def twentythirteen():
    page = """
<html>
<head>
    <title>0w_i_w</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>0w_i_w</h1>
    <img src="https://saltandbaker.com/wp-content/uploads/2024/08/Birthday-Cake-Ice-Cream-5.jpg" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/admin', methods=['GET'])
def admin():
    page = """
<html>
<head>
    <title>4nt_</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px
              0;
        }
    </style>
</head>
<body>
    <h1>4nt_</h1>
    <img src="https://www.rotinrice.com/wp-content/uploads/2011/08/MatchaIceCream-1-500x500.jpg" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/zeus', methods=['GET'])
def zeus():
    page = """
<html>
<head>
    <title>1c3_</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>1c3_</h1>
    <img src="https://hips.hearstapps.com/vidthumb/images/delish-blueberry-no-churn-ice-cream-still002-1530884427.jpg?crop=0.526xw:0.934xh;0.220xw,0.0199xh&resize=1200:*" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/mojo', methods=['GET'])
def mojo():
    page = """
<html>
<head>
    <title>cr34</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>cr34</h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz3WOAGKM22qpVwDuMenRJGcko1QMHoZRLYQ&s" class="flavor-img">
</body>
</html>
    """
    return page

@app.route('/tuscany', methods=['GET'])
def tuscany():
    page = """
<html>
<head>
    <title>m}</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <h1>m}</h1>
    <img src="https://www.chewoutloud.com/wp-content/uploads/2020/04/Mint-Chip-Ice-Cream-Square.jpg" class="flavor-img">
</body>
</html>
    """
    return page

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=40008)
