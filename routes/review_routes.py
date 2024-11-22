from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.models import Review, db

# Create a new review
reviews_bp = Blueprint('reviews_bp', __name__)

@reviews_bp.route('/reviews', methods=['POST'])
def add_review():
    if request.method == 'POST':
        data = request.form
        review = Review(
            comments=data.get('comments'),
            rating=data.get('rating'),
            paper_id=data['paper_id'],
            reviewer_id=data['reviewer_id']
        )
        db.session.add(review)
        db.session.commit()
        flash('Review created successfully!', 'success')
        return redirect(url_for('reviews_bp.get_reviews'))

# Get all reviews
@reviews_bp.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return render_template('reviews/reviews_list.html', reviews=reviews)

# Update a review
@reviews_bp.route('/reviews/<int:review_id>/edit', methods=['GET', 'POST'])
def update_review(review_id):
    review = Review.query.get_or_404(review_id)
    if request.method == 'POST':
        review.comments = request.form.get('comments', review.comments)
        review.rating = request.form.get('rating', review.rating)
        db.session.commit()
        flash('Review updated successfully!', 'success')
        return redirect(url_for('reviews_bp.get_reviews'))
    return render_template('reviews/edit_review.html', review=review)

# Delete a review
@reviews_bp.route('/reviews/<int:review_id>/delete', methods=['POST'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    flash('Review deleted successfully!', 'danger')
    return redirect(url_for('reviews_bp.get_reviews'))
