from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.models import Review, db

# Create a new review
reviews_bp = Blueprint('reviews_bp', __name__)

# Route to display all reviews
@reviews_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return render_template('reviews/reviews_list.html', reviews=reviews)

# Route to display form for adding a new review
@reviews_bp.route('/reviews/add', methods=['GET'])
def add_review_page():
    return render_template('reviews/add_review.html')

# Route to handle the POST request for adding a new review
@reviews_bp.route('/reviews', methods=['POST'])
def add_review():
    comments = request.form['comments']
    rating = request.form['rating']
    paper_id = request.form['paper_id']
    reviewer_id = request.form['reviewer_id']

    # Create a new Review object
    review = Review(
        comments=comments,
        rating=rating,
        paper_id=paper_id,
        reviewer_id=reviewer_id
    )

    db.session.add(review)
    db.session.commit()

    flash('Review created successfully!', 'success')
    return redirect(url_for('reviews_bp.get_reviews'))  # Redirect to the list of reviews

# Route to display a single review
@reviews_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    return render_template('reviews/review_detail.html', review=review)

# Route to display form for editing a review
@reviews_bp.route('/reviews/<int:review_id>/edit', methods=['GET'])
def update_review_page(review_id):
    review = Review.query.get_or_404(review_id)
    return render_template('reviews/edit_review.html', review=review)

# Route to handle the PUT request for updating a review
@reviews_bp.route('/reviews/<int:review_id>', methods=['POST'])
def update_review(review_id):
    review = Review.query.get_or_404(review_id)

    review.comments = request.form.get('comments', review.comments)
    review.rating = request.form.get('rating', review.rating)
    db.session.commit()

    flash('Review updated successfully!', 'success')
    return redirect(url_for('reviews_bp.get_reviews'))

# Route to handle the delete request for a review
@reviews_bp.route('/reviews/<int:review_id>/delete', methods=['POST'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()

    flash('Review deleted successfully!', 'danger')
    return redirect(url_for('reviews_bp.get_reviews'))
