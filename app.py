from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Second version"

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
