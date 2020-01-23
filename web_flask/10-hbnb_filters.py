#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/hbnb_filters')
def load_data():
    return render_template(
        '10-hbnb_filters.html', states=storage.all("State"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
