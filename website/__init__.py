from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate



db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "unyUNYDs4fyy723csdDSOhuh"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"

    migrate = Migrate(app, db) 

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Post, Comment
    with app.app_context():
        '''with db.engine.connect() as con:
            trans = con.begin()
            for table in db.metadata.sorted_tables:
                con.execute(table.delete())
            trans.commit()'''
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "views.home"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
