'''from models.models import User,db
from flask import Blueprint
from flask import Flask, jsonify, request, abort
from datetime import datetime

# Create a new user

user_bp = Blueprint('user_bp', __name__)
@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],  # Note: Hash passwords in production!
        role=data['role']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!', 'id': user.id}), 201

# Get all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role
        } for user in users
    ])

# Get a single user by ID
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role
    })

# Update a user
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

# Delete a user
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})'''

from models.models import User, db
from flask import Blueprint, render_template, request, redirect, url_for, flash

user_bp = Blueprint('user_bp', __name__)

# Create a new user (HTML form submission)
@user_bp.route('/users/new', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.form  # Form data from the frontend
        user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],  # Note: Hash passwords in production!
            role=data['role']
        )
        try:
            db.session.add(user)
            db.session.commit()
            flash('User created successfully!', 'success')
            return redirect(url_for('user_bp.get_all_users'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating user: ' + str(e), 'danger')
            return redirect(url_for('user_bp.add_user'))
    return render_template('user/add_user.html')

# Get all users (HTML display)
@user_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return render_template('user/users.html', users=users)

# Get a single user by ID (HTML display)
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/user_detail.html', user=user)

# Update a user (HTML form submission)
@user_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        data = request.form
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.role = data.get('role', user.role)
        try:
            db.session.commit()
            flash('User updated successfully!', 'success')
            return redirect(url_for('user_bp.get_all_users'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating user: ' + str(e), 'danger')
            return redirect(url_for('user_bp.update_user', user_id=user.id))
    return render_template('user/edit_user.html', user=user)

# Delete a user (HTML action)
@user_bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting user: ' + str(e), 'danger')
    return redirect(url_for('user_bp.get_all_users'))

