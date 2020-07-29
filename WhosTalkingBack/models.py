from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    ''' users for the app, contains basic demographic information'''
    id = DB.Column(DB.Integer, primary_key=True)
    display_name = DB.Column(DB.Text)
    gender = DB.Column(DB.Text)
    ethnicity = DB.Column(DB.Text)
    other = DB.Column(DB.Text)

    def __repr__(self):
        return f'{self.display_name}: {self.ethnicity}, {self.gender}, {self.other}'
