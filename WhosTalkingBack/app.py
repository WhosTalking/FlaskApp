from flask import Flask
from dotenv import load_dotenv
import os
from .models import *

load_dotenv()
POSTGRES = {
    'user': os.environ['user'],
    'pw': os.environ['pw'],
    'db': os.environ['db'],
    'host': os.environ['host'],
    'port': '5432'
}


def create_app():
    app = Flask(__name__)

    # for production
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
    #         %(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    # for development I'll just work locally
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whosTalkingDb.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True

    DB.init_app(app)

    @app.route('/')
    def home_route():
        DB.session.add(User(display_name='example', gender='female',
                            ethnicity='white', other=None))
        DB.session.add(User(display_name='example', gender='female',
                            ethnicity='white', other=None))
        DB.session.commit()

        return f'{User.query.all()}'

    return app
