from flask import Flask,render_template, request, session, jsonify,redirect
import json
#from keys import Key
#from models import *
from datetime import date, timedelta

app = Flask(__name__)

app.secret_key = "secret key"

@app.route("/admin/logout",methods=['GET','POST'])
@app.route("/logout",methods=['GET','POST'])
def logout():
    session.clear()
    return redirect("/login")

@app.route("/admin/login",methods=['GET','POST'])
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return redirect("/admin")
    return render_template("login.html",**locals())

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

@app.route("/admin/categories/<int:id>/edit")
def categories_edit(id):
    return render_template("categories/edit/edit.html",**locals())

@app.route("/admin/categories/<int:id>")
def categories_view(id):
    return render_template("categories/view.html",**locals())

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
@app.route("/admin/events/manage")
def events():
    return render_template("events.html",**locals())

@app.route("/admin/events/<string:title>")
@app.route("/admin/events/manage/<string:title>")
def events_view(title):
    return render_template("events.html",**locals())

@app.route("/venues")
def venues_all():
    return render_template("dashboard/dashboard/venues.html",**locals())

@app.route("/venues/<string:title>")
def venues_single(title):
    return render_template("dashboard/dashboard/venues_single.html",**locals())

@app.route("/admin/venues")
def venues():
    return render_template("venues/index.html",**locals())

@app.route("/admin/venues/<int:id>/edit")
def venues_edit(id):
    return render_template("venues/edit/edit.html",**locals())

@app.route("/admin/venues/<int:id>")
def venues_view(id):
    return render_template("venues/view.html",**locals())

@app.route("/admin/venues/create")
def venues_create():
    return render_template("venues/create.html",**locals())

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
@app.route("/profile")
def profile():
    return render_template("profile/index.html",**locals())

@app.route("/admin/media")
def media():
    return render_template("media/index.html",**locals())

@app.route("/admin/media/<int:id>")
def media_edit():
    return render_template("media/edit.html",**locals())

@app.route("/events")
def events_all():
    return render_template("dashboard/dashboard/event/index.html")

@app.route("/events/<string:title>")
def event_single(title):
    return render_template("dashboard/dashboard/event/event.html")

@app.route("/events/<string:title>/<string:tag>")
def event_tag(title,tag):
    return render_template("dashboard/dashboard/event/tag.html")


@app.route("/dashboard/myevents/manage",methods=['GET','POST'])
@app.route("/dashboard/events/create",methods=['GET','POST'])
@app.route("/admin/events/create",methods=['GET','POST'])
def events_create():
    if request.method == 'POST':
        if 'next_tab' in request.form:
            return redirect("#/"+request.form['next_tab'])
    return render_template("dashboard/dashboard/myevents/manage.html",**locals())

@app.route("/dashboard/myevents/manage/<string:title>",methods=['GET','POST'])
def events_edit(title):
    return render_template("dashboard/dashboard/myevents/manage.html",**locals())

@app.route("/dashboard/mybookings/<int:id>")
def bookings_view(id):
    return render_template("dashboard/dashboard/mybookings/booking.html",**locals())

@app.route("/dashboard/myearning")
def earnings():
    return render_template("dashboard/dashboard/myevents/earnings.html",**locals())

@app.route("/dashboard/ticket-scan")
def scan():
    return render_template("dashboard/dashboard/myevents/scan.html",**locals())

@app.route("/template/<string:files>")
def load_files(files):
    return render_template("dashboard/dashboard/"+files)



if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)