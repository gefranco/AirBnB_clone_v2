#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/states_list')
def show_states():
    return render_template(
        '7-states_list.html', states=storage.all("State").values())

if __name__ == '__main__':
    app.run()
