from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>DevOps CI/CD Demo</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
            min-height: 100vh;
        }

        .container {
            max-width: 1100px;
            margin: auto;
            padding: 40px 20px;
        }

        .hero {
            text-align: center;
            padding: 50px 20px;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .hero h1 span {
            color: #38bdf8;
        }

        .hero p {
            color: #cbd5e1;
            font-size: 18px;
        }

        .status {
            display: inline-block;
            margin-top: 25px;
            padding: 10px 20px;
            background: #064e3b;
            color: #6ee7b7;
            border: 1px solid #10b981;
            border-radius: 25px;
            font-weight: bold;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .card {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 16px;
            padding: 25px;
            text-align: center;
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .icon {
            font-size: 40px;
            margin-bottom: 15px;
        }

        .card h3 {
            margin-bottom: 10px;
        }

        .card p {
            color: #cbd5e1;
            font-size: 14px;
        }

        .pipeline {
            margin-top: 50px;
            background: rgba(255, 255, 255, 0.06);
            border-radius: 16px;
            padding: 30px;
        }

        .pipeline h2 {
            text-align: center;
            margin-bottom: 30px;
        }

        .steps {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .step {
            flex: 1;
            min-width: 130px;
            text-align: center;
        }

        .circle {
            width: 55px;
            height: 55px;
            margin: auto;
            border-radius: 50%;
            background: #0ea5e9;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 20px;
        }

        .step p {
            margin-top: 10px;
            color: #e2e8f0;
        }

        .arrow {
            font-size: 25px;
            color: #38bdf8;
        }

        .health-link {
            display: inline-block;
            margin-top: 20px;
            padding: 12px 25px;
            background: #0ea5e9;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
        }

        .health-link:hover {
            background: #0284c7;
        }

        footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            color: #94a3b8;
        }
    </style>
</head>

<body>

    <div class="container">

        <section class="hero">

            <h1>🚀 <span>DevOps</span> CI/CD Demo</h1>

            <p>
                Flask Application deployed using
                GitHub Actions, Docker & AWS EC2
            </p>

            <div class="status">
                ● Application Running
            </div>

        </section>


        <section class="cards">

            <div class="card">
                <div class="icon">🔄</div>
                <h3>GitHub Actions</h3>
                <p>
                    Automated CI/CD pipeline for build,
                    test and deployment.
                </p>
            </div>


            <div class="card">
                <div class="icon">🐳</div>
                <h3>Docker</h3>
                <p>
                    Application packaged and deployed
                    as a Docker container.
                </p>
            </div>


            <div class="card">
                <div class="icon">☁️</div>
                <h3>AWS EC2</h3>
                <p>
                    Application running on an Ubuntu
                    EC2 instance.
                </p>
            </div>


            <div class="card">
                <div class="icon">❤️</div>
                <h3>Health Check</h3>
                <p>
                    Application health endpoint
                    available for monitoring.
                </p>
            </div>

        </section>


        <section class="pipeline">

            <h2>⚙️ CI/CD Pipeline</h2>

            <div class="steps">

                <div class="step">
                    <div class="circle">1</div>
                    <p>Git Push</p>
                </div>

                <div class="arrow">→</div>

                <div class="step">
                    <div class="circle">2</div>
                    <p>GitHub Actions</p>
                </div>

                <div class="arrow">→</div>

                <div class="step">
                    <div class="circle">3</div>
                    <p>Build & Test</p>
                </div>

                <div class="arrow">→</div>

                <div class="step">
                    <div class="circle">4</div>
                    <p>Docker Hub</p>
                </div>

                <div class="arrow">→</div>

                <div class="step">
                    <div class="circle">5</div>
                    <p>AWS EC2</p>
                </div>

            </div>


            <div style="text-align: center;">
                <a class="health-link" href="/health">
                    Check Application Health
                </a>
            </div>

        </section>


        <footer>
            <p>
                Built with ❤️ using Flask |
                GitHub Actions |
                Docker |
                AWS
            </p>
        </footer>

    </div>

</body>
</html>
"""


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "application": "GA Demo",
            "service": "Flask",
            "message": "Application is running successfully"
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

