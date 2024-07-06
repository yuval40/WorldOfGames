from flask import Flask
from Score import read_score

app = Flask(__name__)


def score_server():
    try:
        score = read_score()
        html_content = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    except Exception as e:
        html_content = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{e}</div></h1>
        </body>
        </html>
        """
    return html_content


@app.route("/")
def index():
    return score_server()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
