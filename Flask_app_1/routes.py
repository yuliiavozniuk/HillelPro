from flask import Blueprint, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from extensions import db
from models import User
from forms import RegistrationForm, LoginForm
from auth import login_required, authenticate


app = Blueprint('app', __name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username
        password = form.password
        hashed_password = generate_password_hash(password.data)
        user = User(username=username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('app.login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = authenticate(form.username.data, form.password.data)
        if user:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('app.dashboard'))
        flash('Invalid credentials!', 'danger')
    return render_template('login.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out!', 'info')
    return redirect(url_for('app.home'))

@app.route('/hello')
@login_required
def hello():
    user_id = session.get('user_id')
    if not user_id:
        flash('You need to login first!', 'danger')
        return redirect(url_for('app.login'))

    user = User.query.get(user_id)
    if not user:
        flash('User not found!', 'danger')
        return redirect(url_for('app.logout'))

    return render_template('hello.html', username=user.username)

@app.route('/user_count')
@login_required
def user_count():
    count = User.query.count()
    return render_template('user_count.html', count=count)
