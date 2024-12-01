from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:qwe1234!@localhost/academic_conference_management_system')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    
    # Import and register blueprints
    from routes.users_routes import user_bp
    from routes.conference_routes import conference_bp
    from routes.paper_routes import paper_bp
    from routes.review_routes import reviews_bp
    from routes.session_routes import session_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(conference_bp)
    app.register_blueprint(paper_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(session_bp)


    app.secret_key = "abcdefg"


    @app.route('/')
    def home():
        return render_template('home.html')
    
    return app

# Main execution
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
