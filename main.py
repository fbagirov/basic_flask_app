# import Flask class from the flask package
# make sure you installed flask package in your environment
# by running 'pip install flask' in your shell. 
from flask import Flask 

# Instantiate the new application by using
# a constructor Flask(). This constructor takes the name of 
# current modeule (__name__) as argument. 
app = Flask(__name__)


# Create the route (a path that will show after the url).
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call the 
# associated function. The '/' parameter represents URL 
# that will execute the function home() once the user 
# browses to that url. 
@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
	# '__main__' is the name of the scope in which top-level
	# code executes. There are two ways of using a Python 
	# module: running directly as a script, or importing it. 
	# When a module is run as a script, it's __name__ is set 
	# to __main__.
    # This is used when running locally only. When deploying to a 
    # webserver(for example, Gunicorn), the server will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)
