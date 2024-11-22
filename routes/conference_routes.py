from models.models import Conference, db
from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

# Create a new conference
conference_bp = Blueprint('conference_bp', __name__)

# Route to display all conferences
@conference_bp.route('/conferences', methods=['GET'])
def get_conferences():
    conferences = Conference.query.all()
    return render_template('conference/conferences.html', conferences=conferences)

# Route to display form for adding a new conference
@conference_bp.route('/conferences/add', methods=['GET'])
def add_conference_page():
    return render_template('conference/add_conference.html')

# Route to handle the POST request for adding a new conference
@conference_bp.route('/conferences', methods=['POST'])
def add_conference():
    name = request.form['name']
    location = request.form['location']
    date = request.form['date']
    organizer_id = request.form['organizer_id']
    
    conference = Conference(
        name=name,
        location=location,
        date=datetime.strptime(date, '%Y-%m-%d'),
        organizer_id=organizer_id
    )
    
    db.session.add(conference)
    db.session.commit()
    
    return redirect(url_for('conference_bp.get_conferences'))

# Route to display a single conference
@conference_bp.route('/conferences/<int:conference_id>', methods=['GET'])
def get_conference(conference_id):
    conference = Conference.query.get_or_404(conference_id)
    return render_template('conference/conference_detail.html', conference=conference)

# Route to display form for editing a conference
@conference_bp.route('/conferences/<int:conference_id>/edit', methods=['GET'])
def update_conference_page(conference_id):
    conference = Conference.query.get_or_404(conference_id)
    return render_template('conference/edit_conference.html', conference=conference)

# Route to handle the PUT request for updating a conference
@conference_bp.route('/conferences/<int:conference_id>', methods=['POST'])
def update_conference(conference_id):
    conference = Conference.query.get_or_404(conference_id)
    
    conference.name = request.form.get('name', conference.name)
    conference.location = request.form.get('location', conference.location)
    if 'date' in request.form:
        conference.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    conference.organizer_id = request.form.get('organizer_id', conference.organizer_id)
    
    db.session.commit()
    
    return redirect(url_for('conference_bp.get_conference', conference_id=conference.id))

# Route to handle the delete request for a conference
@conference_bp.route('/conferences/<int:conference_id>/delete', methods=['GET'])
def delete_conference(conference_id):
    conference = Conference.query.get_or_404(conference_id)
    db.session.delete(conference)
    db.session.commit()
    
    return redirect(url_for('conference_bp.get_conferences'))
