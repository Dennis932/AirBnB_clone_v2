<<<<<<< HEAD
#!/usr/bin/python3
""" 1. Script to start a Flask web application with 2 commands """

from flask import Flask


=======

#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
>>>>>>> 01ab989fc791a9bb63437a69dd58130562176b24
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_world():
    """ Returns some text. """
=======
def index():
    """returns Hello HBNB!"""
>>>>>>> 01ab989fc791a9bb63437a69dd58130562176b24
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
<<<<<<< HEAD
def hello():
    """ Return other text. """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
def hbnb():
    """returns HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

>>>>>>> 01ab989fc791a9bb63437a69dd58130562176b24
