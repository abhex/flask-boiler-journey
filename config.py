import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretShhhhhhhh'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'postgresql://postgres:Kwanso123!@localhost:5432/flask-test' 
        # or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False