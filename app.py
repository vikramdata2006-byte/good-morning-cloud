from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Good Morning Cloud!</title>

    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #dff6ff, #ffffff);
        }

        .card {
            background: rgba(255,255,255,0.9);
            padding: 40px 25px;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.12);
            width: 85%;
            max-width: 600px;
        }

        .cloud {
            font-size: 50px;
        }

        h1 {
            font-size: 42px;
            color: #2878b5;
            margin: 15px 0 35px;
        }

        .time-row {
            font-size: 20px;
            color: #444;
            margin: 25px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .time {
            font-size: 25px;
            font-weight: bold;
            color: #2878b5;
        }

        .zone {
            font-size: 14px;
            color: #666;
        }

        @media (max-width: 600px) {

            h1 {
                font-size: 32px;
            }

            .time-row {
                font-size: 17px;
            }

            .time {
                font-size: 22px;
            }

            .card {
                padding: 30px 15px;
            }
        }
    </style>
</head>

<body>

<div class="card">

    <div class="cloud">☁️</div>

    <h1>Good Morning Cloud!</h1>

    <div class="time-row">
        🇮🇳
        <b>Now your time is:</b>
        <span id="ist" class="time"></span>
        <span class="zone">IST</span>
    </div>

    <div class="time-row">
        🇸🇪
        <b>My time is:</b>
        <span id="sweden" class="time"></span>
        <span id="swedenZone" class="zone"></span>
    </div>

</div>

<script>

function updateTime() {

    const now = new Date();

    // India / Kolkata time
    const indiaTime = new Intl.DateTimeFormat('en-US', {
        timeZone: 'Asia/Kolkata',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    }).format(now);

    // Sweden / Stockholm time
    const swedenTime = new Intl.DateTimeFormat('en-US', {
        timeZone: 'Europe/Stockholm',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    }).format(now);

    document.getElementById("ist").textContent = indiaTime;
    document.getElementById("sweden").textContent = swedenTime;

    // Automatically detect CET / CEST
    const parts = new Intl.DateTimeFormat('en-US', {
        timeZone: 'Europe/Stockholm',
        timeZoneName: 'short'
    }).formatToParts(now);

    const zone = parts.find(
        part => part.type === 'timeZoneName'
    );

    document.getElementById("swedenZone").textContent =
        zone ? zone.value : "Sweden Time";
}

updateTime();

// Update every second
setInterval(updateTime, 1000);

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
