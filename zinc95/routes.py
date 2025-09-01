from flask import Blueprint, render_template, redirect, url_for

zinc95 = Blueprint("zinc95", __name__)

@zinc95.route("/")
def main():
    return render_template("zinc95.html")
