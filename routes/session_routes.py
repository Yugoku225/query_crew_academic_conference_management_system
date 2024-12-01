from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.models import Session, db, Conference
from datetime import datetime

# Create a blueprint for session management
session_bp = Blueprint('session_bp', __name__)

# Add a new session
@session_bp.route('/sessions/new', methods=['GET', 'POST'])
def add_session():
    if request.method == 'POST':
        data = request.form
        # Check if the conference exists
        conference = Conference.query.get(data['conference_id'])
        if not conference:
            flash('Conference not found!', 'danger')
            return redirect(url_for('session_bp.add_session'))

        try:
            session = Session(
                title=data['title'],
                description=data.get('description'),
                end_time=datetime.strptime(data['end_time'], '%H:%M:%S').time(),
                conference_id=data['conference_id']
            )
            db.session.add(session)
            db.session.commit()
            flash('Session created successfully!', 'success')
            return redirect(url_for('session_bp.get_sessions'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('session_bp.add_session'))

    # Render the add session form for GET requests
    return render_template('sessions/add_session.html')

# Get all sessions
@session_bp.route('/sessions', methods=['GET'])
def get_sessions():
    sessions = Session.query.all()
    return render_template('sessions/sessions_list.html', sessions=sessions)

# Update a session
@session_bp.route('/sessions/<int:session_id>/edit', methods=['GET', 'POST'])
def update_session(session_id):
    session = Session.query.get_or_404(session_id)
    if request.method == 'POST':
        try:
            session.title = request.form.get('title', session.title)
            session.description = request.form.get('description', session.description)
            session.end_time = datetime.strptime(request.form['end_time'], '%H:%M:%S').time()
            db.session.commit()
            flash('Session updated successfully!', 'success')
            return redirect(url_for('session_bp.get_sessions'))
        except Exception as e:
            db.session.rollback()
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('session_bp.update_session', session_id=session_id))
    return render_template('sessions/edit_session.html', session=session)

# Delete a session
@session_bp.route('/sessions/<int:session_id>/delete', methods=['POST'])
def delete_session(session_id):
    session = Session.query.get_or_404(session_id)
    try:
        db.session.delete(session)
        db.session.commit()
        flash('Session deleted successfully!', 'danger')
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred: {e}', 'danger')
    return redirect(url_for('session_bp.get_sessions'))
