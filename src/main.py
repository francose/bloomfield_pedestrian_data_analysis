from flask import Flask, jsonify, request
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import os, json
from flask import url_for
app = Flask(__name__, static_url_path='')

@app.route("/", methods=('GET', 'POST'))
def main():

    return render_template('index.html')

@app.route('/send')
def send():
    return "<a href=%s>file</a>" % url_for('static', filename='Coordinates.json')

if __name__ == "__main__":
    app.run(debug=True)

# He is a bit retarded today haha
