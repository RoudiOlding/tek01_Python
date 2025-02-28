from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL 

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'abaco'

mysql = MySQL(app)  # Initialize MySQL

# Routes
@app.route('/')
def home():
    cursos = ['PHP', 'PYTHON', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data = {
        "title": 'Index',
        "welcome": 'Hi!',
        'courses': cursos,
        'quantity_courses': len(cursos)
    }
    return render_template('index.html', data=data)

@app.route('/contact/<name>/<int:age>/<favBand>')
def contact(name, age, favBand):
    data = {
        'title': 'Contact',
        'name': name,
        'age': age,
        'favBand': favBand
    }
    return render_template('contact.html', data=data)

@app.route('/query_string')
def query_string():
    # Print query parameters for debugging
    print(request.args)
    param1 = request.args.get('param1')
    return f"Query String Parameter: {param1}"

@app.route('/cursos')
def listar_cursos():
    data = {}
    cursor = None  # Initialize cursor to None
    try:
        cursor = mysql.connection.cursor()  # Use the correct connection object
        sql = "SELECT code, name, credits FROM curso ORDER BY name ASC"
        cursor.execute(sql)
        cursos = cursor.fetchall()
        print(cursos)  # Debugging: Print fetched data
        data['mensaje'] = 'Exito'
        data['cursos'] = cursos  # Add fetched data to the response
    except Exception as ex:
        data['mensaje'] = 'Error'
        data['error'] = str(ex)  # Include the error message for debugging
    finally:
        if cursor:  # Only close the cursor if it was successfully created
            cursor.close()

    return jsonify(data)

# Error handler for 404
def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('home'))  # Redirect to the home route
'''
@app.before_request
def before_request():
    print('Before the request... ')

@app.after_request
def after_request(response):
    print('After the request... ')
    return response
'''

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)