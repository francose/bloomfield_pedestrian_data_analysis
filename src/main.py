from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
