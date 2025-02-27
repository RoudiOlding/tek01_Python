from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global variable to store tasks (replace with a database later)
notionTask = {
    'name': [],
    'status': []  # 'completed' or 'pending'
}

# Task management functions
def addTask(ftask):
    notionTask['name'].append(ftask)
    notionTask['status'].append('pending')

def markTask(task_id):
    if 0 <= task_id < len(notionTask['name']):
        notionTask['status'][task_id] = 'completed'

def deleteTask(task_id):
    if 0 <= task_id < len(notionTask['name']):
        notionTask['name'].pop(task_id)
        notionTask['status'].pop(task_id)

# Flask routes
@app.route('/')
def home():
    return render_template('index.html', tasks=notionTask)

@app.route('/add', methods=['POST']) #router decorator, will handle the request with that url and only acept the post method
def add():
    task = request.form.get('task') # catch the value of the form in index.html, cath exaclty when the user summits
    if task:
        addTask(task)
    return redirect(url_for('home')) # redirect to the home page

@app.route('/mark/<int:task_id>')
def mark(task_id):
    markTask(task_id)
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    deleteTask(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)