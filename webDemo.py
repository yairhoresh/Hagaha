from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello from Yair'

if __name__ == '__main__':
    app.run(debug = True)