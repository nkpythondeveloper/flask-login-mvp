from flask import Flask
from .extensions import db, csrf, login_manager
from .config import Config
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))
    
    from .routes import auth_bp
    from .logic import logic_bp
    from .landing import landing_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(logic_bp)
    app.register_blueprint(landing_bp)
    
    with app.app_context():
        db.create_all()

    return app