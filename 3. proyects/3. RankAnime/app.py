from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# PostgreSQL connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anime_user:anime_password@localhost/anime_ranking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'  # Required for Flask-WTF and Flask-Login

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Anime Model
class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(200), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Anime {self.name}>'

# Login Form
class LoginForm(FlaskForm):
    username_or_email = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

# Anime Form
class AnimeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    photo_url = StringField('Photo URL', validators=[DataRequired()])
    submit = SubmitField('Add Anime')

# Flask-Login User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def home():
    animes = Anime.query.order_by(Anime.position).all()
    return render_template('home.html', animes=animes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter((User.username == form.username_or_email.data) | (User.email == form.username_or_email.data)).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid username/email or password', 'error')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/add_anime', methods=['GET', 'POST'])
@login_required
def add_anime():
    form = AnimeForm()
    if form.validate_on_submit():
        new_anime = Anime(name=form.name.data, photo_url=form.photo_url.data, position=Anime.query.count() + 1)
        db.session.add(new_anime)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_anime.html', form=form)

@app.route('/move_up/<int:anime_id>')
@login_required
def move_up(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    if anime.position > 1:
        anime_above = Anime.query.filter_by(position=anime.position - 1).first()
        anime_above.position += 1
        anime.position -= 1
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/move_down/<int:anime_id>')
@login_required
def move_down(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    anime_below = Anime.query.filter_by(position=anime.position + 1).first()
    if anime_below:
        anime_below.position -= 1
        anime.position += 1
        db.session.commit()
    return redirect(url_for('home'))

# Create tables when the app starts
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)