from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.datetime.now()
    return 'Time is {}'.format(now)

if __name__ == "__main__":
    app.run(debug=True)

