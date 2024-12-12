from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from models import User

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('login'))
        
        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)  # Log the user in
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to user dashboard or home page
        else:
            flash('Login failed. Check your email and/or password.', 'danger')
    
    return render_template('login.html')

@app.route("/dashboard")
@login_required  # Ensure the user is logged in
def dashboard():
    return render_template('dashboard.html')  # Add a dashboard template or page

@app.route("/logout")
@login_required  # Ensure the user is logged in
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))  # Redirect to the login page
