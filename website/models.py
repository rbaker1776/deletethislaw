from . import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, name="id")
    title = db.Column(db.String(150), unique=True, name="title")
    description = db.Column(db.String(600))
    jurisdiction = db.Column(db.String(20))
    upvotes = db.Column(db.Integer)
    comments = db.relationship("Comment", backref="post")

'''
class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(600))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id", name="comment_post_fk"))

'''