'''
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello/<username>')
def hello(username):
    return f'Hello: {username}!'

def helloUser(user, age):
    return f"Hello: {user}! You already have: {age}"

# An alternative way to use route, it more flexible
app.add_url_rule('/helloUser/<user>/<age>', 'helloUser', helloUser)

if __name__ == '__main__':
    app.run(debug=True)
'''

# Importing Necessary Modules
from flask import *
app = Flask(__name__)

# Create a Main route here
@app.route('/')
def input():
	return render_template('index.html')

# Create other routes here. 
# host/passing will be the website link
@app.route('/passing', methods=['GET', 'POST'])
def display():
	if request.method == 'POST':
		result = request.form
		
		# Send result data to result_data HTML file
		return render_template("result_data.html", result=result)


# main route to start with
if __name__ == '__main__':
	app.run(debug=True)