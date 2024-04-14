from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from profanity_check import predict_prob
from .models import Post
from . import db



views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/forum")
def forum():
    return render_template("forum.html")


@views.route("/createpost", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        title = str(request.form.get("title"))
        description = str(request.form.get("description"))
        jurisdiction = str(request.form.get("jurisdiction"))

        if any(predict_prob([title, description]) > 0.9): # title or description is profane
            flash("We ask that you refrain from using profanity. Thank you.", category="invalid-input")
        else:    
            new_post = Post(
                title=title, 
                description=description, 
                jurisdiction=jurisdiction,
                upvotes=0, 
                comments=[]
            )
            print(new_post.jurisdiction)
            db.session.add(new_post)
            db.session.commit()
            #flash("Post successfully added. Thank you!", category="success")
            #return render_template("forum.html")

    return render_template("createpost.html", username=current_user.name)
