from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Routes
@app.route('/')
def home():
    cursos = ['PHP', 'PYTHON', 'Java', 'Kotlin', 'Dart', 'JavaScript']
    data = {
        "tittle": 'Index',
        "welcome": 'Hi!',
        'courses': cursos,
        'quantity_courses': len(cursos)
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)