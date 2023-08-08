# Lets create a flask web application
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Learning API in depth'

if __name__ == '__main__':
    app.run(debug=True)