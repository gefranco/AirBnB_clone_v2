from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_HBNB():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c(text):
    return 'C %s' % text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    return 'Python %s' % text.replace('_', ' ')

if __name__ == '__main__':
    app.run()
