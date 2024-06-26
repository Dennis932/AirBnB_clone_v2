<<<<<<< HEAD
#!/usr/bin/python3
""" 7. Start flask service that does something. """

from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


#@app.route()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======

#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

>>>>>>> 01ab989fc791a9bb63437a69dd58130562176b24
