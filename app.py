from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Good Morning Cloud</title>
        </head>
        <body>
            <h1>Good Morning Cloud!!!</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
