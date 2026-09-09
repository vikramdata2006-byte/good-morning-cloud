from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route("/")
def home():

    ist = datetime.now(ZoneInfo("Asia/Kolkata"))
    cet = datetime.now(ZoneInfo("Europe/Stockholm"))

    ist_time = ist.strftime("%I:%M:%S %p")
    cet_time = cet.strftime("%I:%M:%S %p")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Good Morning Cloud!</title>

        <style>
            body {{
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #dff6ff, #ffffff);
            }}

            .card {{
                background: rgba(255,255,255,0.85);
                padding: 40px 25px;
                border-radius: 25px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.12);
                width: 85%;
                max-width: 500px;
            }}

            h1 {{
                font-size: 42px;
                color: #2878b5;
                margin-bottom: 35px;
            }}

            p {{
                font-size: 21px;
                color: #444;
                margin: 18px 0;
            }}

            .cloud {{
                font-size: 45px;
            }}
        </style>
    </head>

    <body>

        <div class="card">

            <div class="cloud">☁️</div>

            <h1>Good Morning Cloud!</h1>

            <p>🇮🇳 <b>Now your time is:</b><br>
            {ist_time} IST</p>

            <p>🇸🇪 <b>My time is:</b><br>
            {cet_time} CET</p>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
