from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import os, json
from flask import url_for
app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=('GET', 'POST'))
def main():

    return render_template('index.html')




@app.route('/send')
def send():
    # json_url = os.path.join( 'static', 'locations.json')
    data = json.loads('/static/locations.json')
    return "<a href=%s>file</a>" % url_for('static',filename=data)

if __name__ == "__main__":
    app.run(debug=True)
