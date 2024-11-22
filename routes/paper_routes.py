from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Paper
from datetime import datetime

paper_bp = Blueprint('paper_bp', __name__)

# Route to display all papers
@paper_bp.route('/papers', methods=['GET'])
def get_papers():
    papers = Paper.query.all()
    return render_template('paper/papers.html', papers=papers)

# Route to display form for adding a new paper
@paper_bp.route('/papers/add', methods=['GET'])
def add_paper_page():
    return render_template('paper/add_paper.html')

# Route to handle the POST request for adding a new paper
@paper_bp.route('/papers', methods=['POST'])
def add_paper():
    title = request.form['title']
    abstract = request.form['abstract']
    author_id = request.form['author_id']
    conference_id = request.form['conference_id']
    
    paper = Paper(
        title=title,
        abstract=abstract,
        submission_date=datetime.utcnow(),
        author_id=author_id,
        conference_id=conference_id
    )
    
    db.session.add(paper)
    db.session.commit()
    
    return redirect(url_for('paper_bp.get_papers'))

# Route to display a single paper
@paper_bp.route('/papers/<int:paper_id>', methods=['GET'])
def get_paper(paper_id):
    paper = Paper.query.get_or_404(paper_id)
    return render_template('paper/paper_detail.html', paper=paper)

# Route to display form for editing a paper
@paper_bp.route('/papers/<int:paper_id>/edit', methods=['GET'])
def update_paper_page(paper_id):
    paper = Paper.query.get_or_404(paper_id)
    return render_template('paper/edit_paper.html', paper=paper)

# Route to handle the POST request for updating a paper
@paper_bp.route('/papers/<int:paper_id>', methods=['POST'])
def update_paper(paper_id):
    paper = Paper.query.get_or_404(paper_id)
    
    paper.title = request.form.get('title', paper.title)
    paper.abstract = request.form.get('abstract', paper.abstract)
    paper.conference_id = request.form.get('conference_id', paper.conference_id)
    db.session.commit()
    
    return redirect(url_for('paper_bp.get_paper', paper_id=paper.id))

# Route to handle the delete request for a paper
@paper_bp.route('/papers/<int:paper_id>/delete', methods=['GET'])
def delete_paper(paper_id):
    paper = Paper.query.get_or_404(paper_id)
    db.session.delete(paper)
    db.session.commit()
    
    return redirect(url_for('paper_bp.get_papers'))
