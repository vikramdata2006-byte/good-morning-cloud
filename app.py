from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Good Morning Meghaaa!</title>

    <style>
        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #dff6ff, #ffffff);
            overflow: hidden;
        }

        .card {
            background: rgba(255, 255, 255, 0.92);
            padding: 40px 25px;
            border-radius: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
            width: 90%;
            max-width: 600px;
            box-sizing: border-box;
        }

        .cloud {
            font-size: 55px;
            margin-bottom: 5px;
        }

        h1 {
            font-size: 42px;
            color: #2878b5;
            margin: 10px 0 35px;
        }

        /* Keep everything on ONE LINE */
        .time-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;

            white-space: nowrap;

            font-size: 18px;
            color: #444;

            margin: 25px 0;
        }

        .time {
            font-size: 22px;
            font-weight: bold;
            color: #2878b5;
        }

        .zone {
            font-size: 13px;
            color: #666;
        }

        /* Mobile */
        @media (max-width: 600px) {

            .card {
                width: 94%;
                padding: 30px 10px;
            }

            .cloud {
                font-size: 45px;
            }

            h1 {
                font-size: 31px;
                margin-bottom: 30px;
            }

            .time-row {
                font-size: 14px;
                gap: 4px;
                margin: 22px 0;
            }

            .time {
                font-size: 18px;
            }

            .zone {
                font-size: 10px;
            }
        }

        /* Very small phones */
        @media (max-width: 380px) {

            h1 {
                font-size: 27px;
            }

            .time-row {
                font-size: 12px;
                gap: 3px;
            }

            .time {
                font-size: 16px;
            }

            .zone {
                font-size: 9px;
            }
        }

    </style>
</head>

<body>

<div class="card">

    <div class="cloud">👋</div>

    <h1>Good Morning Meghaaa!</h1>


    <!-- INDIA TIME -->

    <div class="time-row">

        <span>🇮🇳</span>

        <b>Now your time is:</b>

        <span id="ist" class="time"></span>

        <span class="zone">IST</span>

    </div>


    <!-- SWEDEN TIME -->

    <div class="time-row">

        <span>🇸🇪</span>

        <b>My time is:</b>

        <span id="sweden" class="time"></span>

        <span id="swedenZone" class="zone"></span>

    </div>

</div>


<script>

function updateTime() {

    const now = new Date();


    // 🇮🇳 India / Kolkata time

    const indiaTime = new Intl.DateTimeFormat('en-US', {

        timeZone: 'Asia/Kolkata',

        hour: '2-digit',

        minute: '2-digit',

        second: '2-digit',

        hour12: true

    }).format(now);


    // 🇸🇪 Sweden / Stockholm time

    const swedenTime = new Intl.DateTimeFormat('en-US', {

        timeZone: 'Europe/Stockholm',

        hour: '2-digit',

        minute: '2-digit',

        second: '2-digit',

        hour12: true

    }).format(now);


    // Display times

    document.getElementById("ist").textContent = indiaTime;

    document.getElementById("sweden").textContent = swedenTime;


    // Automatically detect CET or CEST

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


// Run immediately

updateTime();


// Update every second

setInterval(updateTime, 1000);

</script>

</body>
</html>
"""


if __name__ == "__main__":
    app.run()
