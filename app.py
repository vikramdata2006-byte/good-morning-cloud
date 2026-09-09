
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
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            height: 100vh;
            overflow: hidden;
            font-family: Georgia, serif;
            background: linear-gradient(
                to bottom,
                #172554 0%,
                #4338ca 25%,
                #f97316 65%,
                #fde68a 100%
            );
        }

        /* Sunrise glow */
        .sun {
            position: absolute;
            width: 130px;
            height: 130px;
            border-radius: 50%;
            background: #fff7ae;
            box-shadow:
                0 0 30px #fff3a3,
                0 0 70px #ffd166,
                0 0 120px #ffb703;
            left: 50%;
            bottom: -150px;
            transform: translateX(-50%);
            animation: sunrise 8s ease-out forwards;
        }

        @keyframes sunrise {
            0% {
                bottom: -150px;
            }
            100% {
                bottom: 48%;
            }
        }

        /* Main greeting */
        .message {
            position: absolute;
            top: 38%;
            width: 100%;
            text-align: center;
            z-index: 20;
            opacity: 0;
            animation: appear 3s ease forwards;
            animation-delay: 2s;
        }

        h1 {
            margin: 0;
            padding: 0 15px;
            font-size: clamp(38px, 9vw, 72px);
            color: white;
            font-weight: 500;
            letter-spacing: 2px;
            text-shadow:
                0 3px 10px rgba(0,0,0,0.35),
                0 0 20px rgba(255,255,255,0.3);
        }

        .heart {
            font-size: 35px;
            margin-top: 15px;
            animation: heartbeat 1.5s infinite;
        }

        @keyframes heartbeat {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.2);
            }
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Clouds */
        .cloud {
            position: absolute;
            font-size: 80px;
            opacity: 0.85;
            z-index: 10;
            animation: cloudMove linear infinite;
        }

        .cloud1 {
            top: 16%;
            left: -150px;
            animation-duration: 32s;
        }

        .cloud2 {
            top: 28%;
            left: -250px;
            font-size: 110px;
            animation-duration: 42s;
            animation-delay: 5s;
        }

        .cloud3 {
            top: 62%;
            left: -180px;
            font-size: 75px;
            animation-duration: 28s;
            animation-delay: 2s;
        }

        @keyframes cloudMove {
            from {
                transform: translateX(0);
            }
            to {
                transform: translateX(130vw);
            }
        }

        /* Birds */
        .birds {
            position: absolute;
            top: 20%;
            left: -100px;
            font-size: 30px;
            z-index: 15;
            animation: birdsMove 18s linear infinite;
        }

        .birds2 {
            top: 30%;
            left: -150px;
            font-size: 24px;
            animation-duration: 24s;
            animation-delay: 5s;
        }

        @keyframes birdsMove {
            from {
                transform: translateX(0);
            }
            to {
                transform: translateX(130vw);
            }
        }

        /* Flying sparkle particles */
        .sparkle {
            position: absolute;
            color: white;
            font-size: 18px;
            animation: float 5s ease-in-out infinite;
            opacity: 0.7;
        }

        .s1 { left: 15%; top: 30%; }
        .s2 { left: 80%; top: 25%; animation-delay: 1s; }
        .s3 { left: 25%; top: 70%; animation-delay: 2s; }
        .s4 { left: 70%; top: 65%; animation-delay: 3s; }

        @keyframes float {
            0%, 100% {
                transform: translateY(0);
                opacity: 0.4;
            }
            50% {
                transform: translateY(-25px);
                opacity: 1;
            }
        }

        /* Bottom landscape */
        .ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 18%;
            background: linear-gradient(to top, #14532d, #166534);
            border-radius: 50% 50% 0 0;
        }

        @media (max-width: 600px) {
            .sun {
                width: 95px;
                height: 95px;
            }

            .cloud {
                font-size: 60px;
            }

            .cloud2 {
                font-size: 80px;
            }

            .message {
                top: 40%;
            }

            .heart {
                font-size: 28px;
            }
        }
    </style>
</head>

<body>

    <div class="sun"></div>

    <div class="cloud cloud1">☁️</div>
    <div class="cloud cloud2">☁️</div>
    <div class="cloud cloud3">☁️</div>

    <div class="birds">🐦 🐦</div>
    <div class="birds birds2">🐦 🐦 🐦</div>

    <div class="sparkle s1">✦</div>
    <div class="sparkle s2">✧</div>
    <div class="sparkle s3">✦</div>
    <div class="sparkle s4">✧</div>

    <div class="message">
        <h1>Good Morning Meghaaa!</h1>
        <div class="heart">❤️</div>
    </div>

    <div class="ground"></div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run()
