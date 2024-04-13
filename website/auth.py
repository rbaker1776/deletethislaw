from flask import Blueprint, render_template, request



auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["get", "post"])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route("/sign-up", methods=["get", "post"])
def sign_up():
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return "<p>logout</p>"


def is_password_valid(password: str) -> bool:
    valid_len: bool = len(password) >= 8
    has_lower: bool = False
    has_upper: bool = False
    has_digit: bool = False
    has_symbol: bool = False

    for c in password:
        has_lower |= c.islower()
        has_upper |= c.isupper()
        has_digit |= c.isdigit()
        has_symbol |= c in "!@#$%^&*_-+=`~\\|{}[]()<>,.:;\"'/?"

    return valid_len and has_lower and has_upper and has_digit and has_symbol