from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Моя первая Flask-страница</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 100px;
                background-color: #f0f0f0;
            }
            h1 {
                color: #3366cc;
            }
        </style>
    </head>
    <body>
        <h1>Привет, мир!</h1>
        <p>Это моя первая веб-страница на Flask</p>
        <p><small>Flask работает успешно!</small></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)