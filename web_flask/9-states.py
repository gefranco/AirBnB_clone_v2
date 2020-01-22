#!/usr/bin/python3
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def show_cities_by_state(id=None):
    if id is not None:
        id = 'State.'+id
    return render_template(
        '9-states.html', states=storage.all("State"), state_id=id)


if __name__ == '__main__':
    app.run()
