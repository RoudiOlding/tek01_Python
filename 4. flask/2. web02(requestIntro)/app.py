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
    return f"Hello: {user}, you already have: {age}"

# An alternative way to use route, it more flexible
app.add_url_rule('/helloUser/<user>/<age>', 'helloUser', helloUser)

if __name__ == '__main__':
    app.run(debug=True)