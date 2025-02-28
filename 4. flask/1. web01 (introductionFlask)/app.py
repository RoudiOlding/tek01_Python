from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

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

# Error handler for 404
def page_not_found(error):
    # return render_template('404.html'), 404
    return redirect(url_for('home'))  # Redirect to the home route

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)