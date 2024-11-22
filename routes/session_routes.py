from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.models import Session, db
from datetime import datetime

# Create a new session
session_bp = Blueprint('session_bp', __name__)

@session_bp.route('/sessions', methods=['POST'])
def add_session():
    if request.method == 'POST':
        data = request.form
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
        session.title = request.form.get('title', session.title)
        session.description = request.form.get('description', session.description)
        session.end_time = datetime.strptime(request.form['end_time'], '%H:%M:%S').time()
        db.session.commit()
        flash('Session updated successfully!', 'success')
        return redirect(url_for('session_bp.get_sessions'))
    return render_template('sessions/edit_session.html', session=session)

# Delete a session
@session_bp.route('/sessions/<int:session_id>/delete', methods=['POST'])
def delete_session(session_id):
    session = Session.query.get_or_404(session_id)
    db.session.delete(session)
    db.session.commit()
    flash('Session deleted successfully!', 'danger')
    return redirect(url_for('session_bp.get_sessions'))
