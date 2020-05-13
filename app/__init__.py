# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .model import configure as config_db
from .serealizer import configure as config_ma


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/cadastro.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'A mas e dificil saber'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    JWTManager(app)

    from .person import bp_person
    app.register_blueprint(bp_person)

    from .user import bp_user
    app.register_blueprint(bp_user)

    from .login import bp_login
    app.register_blueprint(bp_login)

    return app
