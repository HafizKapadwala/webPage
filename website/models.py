#we are going to use this for our database model

#we are going to create database model

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now)
    #we have to also store which user created this note
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    #this is basically associating a user with different notes -- 1 to many
class User(db.Model,UserMixin):
    id = db.Column(db.Intger,primary_key=True)
    email = db.Column(db.String(150),unique=True)
    pass_user = db.Column(db.String)
    first_name =  db.Column(db.String(150))
    notes = db.relationship('Note')
    #this just tell to add a particular note to user database
