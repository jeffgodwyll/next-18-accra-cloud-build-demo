from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.datetime.now()
    return render_template('index.html', now=now)

if __name__ == "__main__":
    app.run(debug=True)

