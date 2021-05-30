import os
from flask import Flask, render_template, abort, url_for

app = Flask(__name__,template_folder='.')

@app.route("/")

def index():
    return render_template('index.html', title="page")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')