<<<<<<< HEAD
#!/usr/bin/python3
""" 0. Script to start a Flask web application """

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
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

>>>>>>> 01ab989fc791a9bb63437a69dd58130562176b24
