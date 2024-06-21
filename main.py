from flask import Flask,render_template, request, session, jsonify,redirect
import json
#from keys import Key
#from models import *
from datetime import date, timedelta

app = Flask(__name__)

app.secret_key = "secret key"

@app.route("/")
@app.route("/dashboard")
@app.route("/admin")
def home():
    user_id = 0
    if session.get("user"):
        user_id = session["user"]["user_id"]

    return render_template("dashboard.html",**locals())

@app.route("/admin/categories")
def categories():
    return render_template("categories/index.html",**locals())

@app.route("/admin/categories/create")
def categories_create():
    return render_template("categories/create.html",**locals())

@app.route("/admin/tags")
def tags():
    return render_template("tags/index.html",**locals())

@app.route("/admin/tags/create")
def tags_create():
    return render_template("tags/create.html",**locals())

@app.route("/admin/bookings")
def bookings():
    return render_template("bookings/index.html",**locals())

@app.route("/admin/commissions")
def commissions():
    return render_template("commissions/index.html",**locals())
@app.route("/admin/commissions/<int:id>")
def commissions_detail(id):
    if id:
        return render_template("commissions/edit/index.html",**locals())
    return render_template("commissions/index.html",**locals())

@app.route("/admin/events")
def events():
    return render_template("events.html",**locals())

@app.route("/admin/venues")
def venues():
    return render_template("venues/index.html",**locals())

@app.route("/admin/venues/<int:id>/edit")
def venues_edit(id):
    return render_template("venues/edit/edit.html",**locals())

@app.route("/admin/venues/<int:id>")
def venues_view(id):
    return render_template("venues/view.html",**locals())

@app.route("/admin/taxes")
def taxes():
    return render_template("taxes/taxes.html",**locals())

@app.route("/admin/taxes/<int:id>")
def taxes_edit(id):
    return render_template("taxes/edit/edit.html",**locals())

@app.route("/admin/users")
def users():
    return render_template("users/index.html",**locals())

@app.route("/admin/users/create")
def users_create():
    return render_template("users/create/index.html",**locals())

@app.route("/admin/users/<int:id>/edit")
def users_edit(id):
    return render_template("users/edit/edit.html",**locals())

@app.route("/admin/users/<int:id>")
def users_view(id):
    return render_template("users/view.html",**locals())


@app.route("/admin/contacts")
def contacts():
    return render_template("contacts/index.html",**locals())

@app.route("/admin/contacts/<int:id>")
def contatcs_edit(id):
    return render_template("contacts/edit/edit.html",**locals())

@app.route("/admin/banners")
def banners():
    return render_template("banners/index.html",**locals())

@app.route("/admin/banners/<int:id>")
def banners_edit(id):
    return render_template("banners/edit/edit.html",**locals())

@app.route("/admin/banners/create")
def banners_create():
    return render_template("banners/create.html",**locals())

@app.route("/admin/pages")
def pages():
    return render_template("pages/index.html",**locals())

@app.route("/admin/pages/<int:id>/edit")
def pages_edit(id):
    return render_template("pages/edit/edit.html",**locals())

@app.route("/admin/pages/<int:id>")
def pages_view(id):
    return render_template("pages/view/index.html",**locals())

@app.route("/admin/pages/create")
def pages_create():
    return render_template("pages/create.html",**locals())

@app.route("/admin/posts")
def posts():
    return render_template("posts/index.html",**locals())

@app.route("/admin/posts/<int:id>/edit")
def posts_edit(id):
    return render_template("posts/edit/edit.html",**locals())

@app.route("/admin/posts/<int:id>")
def posts_view(id):
    return render_template("posts/view/index.html",**locals())

@app.route("/admin/posts/create")
def posts_create():
    return render_template("posts/create.html",**locals())

@app.route("/admin/settings")
def settings():
    return render_template("settings/index.html",**locals())



@app.route("/admin/menus/<int:id>/builder")
def menus_edit(id):
    return render_template("menus/"+str(id)+"/builder.html",**locals())

@app.route("/admin/profile")
def profile():
    return render_template("profile/index.html",**locals())

@app.route("/admin/media")
def media():
    return render_template("media/index.html",**locals())

@app.route("/admin/media/<int:id>")
def media_edit():
    return render_template("media/edit.html",**locals())


@app.route("/dashboard/myevents/manage")
@app.route("/dashboard/events/create")
@app.route("/admin/events/create")
def events_create():
    return render_template("dashboard/dashboard/myevents/manage.html",**locals())

@app.route("/dashboard/myearning")
def earnings():
    return render_template("dashboard/dashboard/myevents/earnings.html",**locals())

@app.route("/dashboard/ticket-scan")
def scan():
    return render_template("dashboard/dashboard/myevents/scan.html",**locals())



if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)