from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from models import User
from app import db  # We can still import `db` from app to interact with the database

# Create a Blueprint for the views
views = Blueprint('views', __name__)

@views.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('views.login'))  # Use Blueprint-specific route
        
        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('views.login'))  # Use Blueprint-specific route
    
    return render_template('register.html')

@views.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)  # Log the user in
            flash('Login successful!', 'success')
            return redirect(url_for('views.dashboard'))  # Use Blueprint-specific route
        else:
            flash('Login failed. Check your email and/or password.', 'danger')
    
    return render_template('login.html')

@views.route("/dashboard")
@login_required  # Ensure the user is logged in
def dashboard():
    return render_template('dashboard.html')  # Add a dashboard template or page

@views.route("/logout")
@login_required  # Ensure the user is logged in
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out.', 'success')
    return redirect(url_for('views.login'))  # Use Blueprint-specific route
