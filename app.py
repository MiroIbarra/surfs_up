from flask import Flask

app = Flask(__name__)

@ app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == ‘__main__‘:
    app.run()

export FLASK_APP=app.py

set FLASK_APP=app.py

flask run
