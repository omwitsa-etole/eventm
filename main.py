from flask import Flask,render_template, request, session, jsonify,redirect,g,flash,url_for
import json
#from keys import Key
#from models import *
from datetime import date, timedelta
import time
from controller import *
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.before_request
async def before_request():
    # This code will run before each request
    g.start_time = request.start_time = time.time()
    #print(f"Request started at {g.start_time}")
    if session.get("user") == None:
        user = {'admin':False,'loggedIn':False,'time':g.start_time}
        session['user'] = user

@app.route("/admin/logout",methods=['GET','POST'])
@app.route("/logout",methods=['GET','POST'])
async def logout():
    session.clear()
    return redirect("/login")

@app.route("/login",methods=['GET','POST'])
async def user_login():
    if request.method == 'POST':

        result = await User.validate(request.form['email'],request.form['password'])
        if result == None:
            result = {'message':'Invalid Credentials, No access'}
        if result.get("message"):
            return render_template("login/login.html",message = result.get("message"))

        user = result
        user['loggedIn'] = True
        if user['group'] >= 5:
            user['admin'] = True
        session['user'] = user
        return redirect("/")
    return render_template("login/login.html",message=None)

@app.route("/register",methods=['GET','POST'])
async def user_signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        result = await User.create(name,email,password)
        if result.get("message"):
            return render_template("login/register.html",message=result['message'])
        
    return render_template("login/register.html")

@app.route("/admin/login",methods=['GET','POST'])
async def login():
    if request.method == 'POST':
        user = {'admin':False,'loggedIn':True,'time':g.start_time}
        session['user'] = user
        return redirect("/admin")
    return render_template("login.html",**locals())


@app.route("/dashboard")
@app.route("/admin")
async def home():
    user_id = 0
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("dashboard.html",**locals())

@app.route("/admin/categories")
async def categories():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    categories = await Category.get_all()
    return render_template("categories/index.html",**locals())

@app.route("/admin/categories/<int:id>/edit")
async def categories_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    category = await Category.get(id)
    if category == None:
        message = 'Category not found'
    return render_template("categories/edit/edit.html",**locals())

@app.route("/admin/categories/<int:id>")
async def categories_view(id):
    return render_template("categories/view.html",**locals())

@app.route("/admin/categories/create",methods=['GET','POST'])
async def categories_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method == 'POST':
        name = request.form['name']
        slug  = request.form['slug']
        file = request.files['thumb']
        if file.filename == '':
            thumb = '/default.png'
        else:
            if not allowed_file(file.filename):
                message = 'Invalid file ext, not allowed'
                return render_template("categories/create.html",**locals())
            thumb = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb))
        
        status = request.form['status']
        result = await Category.create(name,slug,thumb,status)
        if result and result == True:
            message= 'New Category Added'
        else:
            message = 'Error occured could not inseert record'
        return render_template("categories/create.html",**locals())
    return render_template("categories/create.html",**locals())

@app.route("/admin/tags")
async def tags():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    tags = await Tag.get_all()
    return render_template("tags/index.html",**locals())

@app.route("/admin/tags/create",methods=['GET','POST'])
async def tags_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method == 'POST':
        name = request.form['title']
        file = request.files['image']
        type = request.form['type']
        sub_title = request.form['sub_title']
        website = request.form['website'];facebook = request.form['facebook'];instagram = request.form['instagram']
        is_page = request.form['is_page'];twitter = request.form['twitter'];linkedin = request.form['linkedin']
        description = request.form['description']
        phone = request.form['phone'];email = request.form['email']
        status = request.form['status']
        if file.filename == '':
            thumb = '/default.png'
        else:
            if not allowed_file(file.filename):
                message = 'Invalid file ext, not allowed'
                return render_template("tags/create.html",**locals())
            thumb = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb))
        result = await Tag.create(name,thumb,type,sub_title,website,is_page,description,phone,email,status)
        if result and result == True:
            message = 'New Tag addedd'
        else:
            message = 'Error occured could not add tag'
        
    return render_template("tags/create.html",**locals())

@app.route("/admin/bookings")
async def bookings():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    bookings = await Booking.get_all()
    return render_template("bookings/index.html",**locals())

@app.route("/admin/commissions")
async def commissions():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    commissions = await Commission.get_all()
    return render_template("commissions/index.html",**locals())

@app.route("/admin/commissions/create",methods=['GET','POST'])
async def commissions_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    commissions = await Commission.get_all()
    return render_template("commissions/create.html",**locals())

@app.route("/admin/commissions/<int:id>")
async def commissions_detail(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    commission = await Commission.find(id)
    return render_template("commissions/edit/index.html",**locals())
    

@app.route("/admin/events")
@app.route("/admin/events/manage")
async def events():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("events.html",**locals())

@app.route("/admin/events/<string:title>")
@app.route("/admin/events/manage/<string:title>")
async def events_view(title):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("events.html",**locals())

@app.route("/venues")
async def venues_all():
    return render_template("dashboard/dashboard/venues.html",**locals())

@app.route("/venues/<string:title>")
async def venues_single(title):
    return render_template("dashboard/dashboard/venues_single.html",**locals())

@app.route("/admin/venues")
async def venues():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("venues/index.html",**locals())

@app.route("/admin/venues/<int:id>/edit")
async def venues_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("venues/edit/edit.html",**locals())

@app.route("/admin/venues/<int:id>")
async def venues_view(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    venue = await Venue.find(id)
    return render_template("venues/view.html",**locals())

@app.route("/admin/venues/create",methods=['GET','POST'])
async def venues_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method == 'POST':
        name = request.form['title']
        slug = request.form['slug']
        description = request.form['description']
        venue_type = request.form['venue_type']
        seated_guestnumber = request.form['seated_guestnumber']
        standing_guestnumber = request.form['standing_guestnumber']
        contact_email = request.form['contact_email'];country = request.form['country']
        ammenities = request.form['ammenities'];address = request.form['address']
        neighbourhoods = erquest.form['neighbourhoods'];city = request.form['city'];state = request.form['state']
        availability = request.form['availability']
        food = request.form['food'];show_quoteform = request.form['show_quoteform']
        zipcode = request.form['zipcode']
        files = request.files['images'];status = request.form['status']
        thumbs = ''
        for file in files:
            if file.filename == '':
                thumbs  += '/default.png;'
            else:
                if not allowed_file(file.filename):
                    message = 'Invalid file ext, not allowed'
                    return render_template("venues/create.html",**locals())
                thumb = secure_filename(file.filename)
                thumbs += thumb+";"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb))
        result = await Venue.create(name,slug,thumbs,statusdescription,venue_type,seated_guestnumber,standing_guestnumber,
            contact_email,ammenities,neighbourhoods,availability,food,country,address,city,state,zip_code,show_quoteform
        )
        if result and result == True:
            message= 'New Venue Added'
        else:
            message = 'Error occured could not insert record'
    return render_template("venues/create.html",**locals())

@app.route("/admin/taxes")
async def taxes():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    taxes = await Tax.get_all()
    return render_template("taxes/taxes.html",**locals())

@app.route("/admin/taxes/create",methods=['GET','POST'])
async def taxes_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method  == 'POST':
        name = request.form['title']
        rate_type = request.form['rate_type']
        rate = request.form['rate']
        net_price = request.form['net_price']
        status = request.form['status']
        admin_tax = request.form['admin_tax']
        result = await Tax.create(name,rate_type,rate,net_price,status,admin_tax)
        if result and result == True:
            message = 'New tax Added'
        else:
            message = 'Error cooured, cuould not insert record'
    return render_template("taxes/create.html",**locals())

@app.route("/admin/taxes/<int:id>")
async def taxes_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    tax = await Tax.find(id)
    return render_template("taxes/edit/edit.html",**locals())

@app.route("/admin/users")
async def users():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    users = await User.get_all()
    return render_template("users/index.html",**locals())

@app.route("/admin/users/create",methods=['GET','POST'])
async def users_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("users/create/index.html",**locals())

@app.route("/admin/users/<int:id>/edit")
async def users_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    user = await User.find(id)
    return render_template("users/edit/edit.html",**locals())

@app.route("/admin/users/<int:id>")
async def users_view(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    user = await User.find(id)
    return render_template("users/view.html",**locals())


@app.route("/admin/contacts")
async def contacts():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    contacts = await Contact.get_all()
    return render_template("contacts/index.html",**locals())

@app.route("/admin/contacts/<int:id>")
async def contatcs_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    contact = await Contact.find(id)
    return render_template("contacts/edit/edit.html",**locals())

@app.route("/admin/banners")
async def banners():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    banners = await Banner.get_all()
    return render_template("banners/index.html",**locals())

@app.route("/admin/banners/<int:id>")
async def banners_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    banner = await Banner.find(id)
    return render_template("banners/edit/edit.html",**locals())

@app.route("/admin/banners/create",methods=['GET','POST'])
async def banners_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method == 'POST':
        file = request.files['image']
        name = request.form['title']
        sub_title = request.form['subtitle']
        button_url = request.form['button_url']
        button_title = request.form['button_title']
        order_no = request.form['order_no']
        status = request.form['status']
        if file.filename == '':
            thumb = '/default.png'
        else:
            if not allowed_file(file.filename):
                message = 'Invalid file ext, not allowed'
                return render_template("banners/create.html",**locals())
            thumb = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb))
        result = await Banner.create(name,sub_title,thumb,button_url,button_title,order_no,status)
        if result and result == True:
            message = 'New Banner Created'
        else:
            message = 'Error occured could not create banner'
    return render_template("banners/create.html",**locals())

@app.route("/admin/pages")
async def pages():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    pages = await Page.get_all()
    return render_template("pages/index.html",**locals())

@app.route("/admin/pages/<int:id>/edit")
async def pages_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    page = await Page.find(id)
    return render_template("pages/edit/edit.html",**locals())

@app.route("/admin/pages/<int:id>")
async def pages_view(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    page = await Page.find(id)
    return render_template("pages/view/index.html",**locals())

@app.route("/admin/pages/create",methods=['GET','POST'])
async def pages_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method == 'POST':
        file = request.files['image']
        name = request.form['title']
        excerpt = request.form['excerpt']
        body = request.form['body']
        slug = request.form['slug']
        meta_description = request.form['meta_description']
        meta_keywords = request.form['meta_keywords']
        status = request.form['status']
        if file.filename == '':
            thumb = '/default.png'
        else:
            if not allowed_file(file.filename):
                message = 'Invalid file ext, not allowed'
                return render_template("pages/create.html",**locals())
            thumb = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb))
        result = await Page.create(name,slug,thumb,excerpt,body,meta_description,meta_keywords,status)
        if result and result == True:
            message = 'New Page added'
        else:
            message = 'An Error occured coould not create page'
    return render_template("pages/create.html",**locals())

@app.route("/admin/posts")
async def posts():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    post = await Post.get_all()
    return render_template("posts/index.html",**locals())

@app.route("/admin/posts/<int:id>/edit")
async def posts_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    post = await Post.find(id)
    return render_template("posts/edit/edit.html",**locals())

@app.route("/admin/posts/<int:id>")
async def posts_view(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    post = await Post.find(id)
    return render_template("posts/view/index.html",**locals())

@app.route("/admin/posts/create",methods=['GET','POST'])
async def posts_create():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method == 'POST':
        file = request.files['image']
        name = request.form['title']
        slug = request.form['slug']
        body = request.form['body']
        excerpt = request.form['excerpt']
        status = request.form['status']
        category_id = request.form['category_id']
        featured = request.form['featured']
        meta_description = request.form['meta_description']
        meta_keywords = request.form['meta_keywords']
        seo_title = request.form['seo_title']
        if file.filename == '':
            thumb = '/default.png'
        else:
            if not allowed_file(file.filename):
                message = 'Invalid file ext, not allowed'
                return render_template("posts/create.html",**locals())
            thumb = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb))
        result = await Post.create(name,slug,thumb,body,excerpt,status,category_id,featured,meta_description,meta_keywords,seo_title)
        if result and result == True:
            message = 'New Post addedd'
        else:
            message = 'An error occured could not add post'
    return render_template("posts/create.html",**locals())

@app.route("/admin/settings",methods=['GET','POST'])
async def settings():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    if request.method == 'POST':
        bg_image = request.files['admin.bg_image']
        loader = request.files['admin.loader']
        icon_image = request.files['admin.icon_image']
        logo = request.files['site.logo']
        site_favicon = request.files['site.site_favicon']
        files = [bg_image,loader,icon_image,logo,site_favicon]
        thumbs = []
        for file in files:
            if file.filename == '':
                thumbs.append('/default.png')
            else:
                thumb = secure_filename(file.filename)
                thumbs.append(secure_filename(file.filename))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb))
        result = await Settings.create(bg_image=thumbs[0],loader=thumbs[1],icon_image=thumbs[2],
            logo = thumbs[3],
            site_favicon = thumbs[4]
        )
        if result and result == True:
            message = "Settings Updated"
        else:
            message ='Could not updated settings | Error'
    return render_template("settings/index.html",**locals())



@app.route("/admin/menus/<int:id>/builder")
async def menus_edit(id):
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("menus/"+str(id)+"/builder.html",**locals())

@app.route("/admin/profile")
@app.route("/profile")
async def profile():
    return render_template("profile/index.html",**locals())

@app.route("/admin/media")
async def media():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("media/index.html",**locals())

@app.route("/admin/media/<int:id>")
async def media_edit():
    if session.get("user") and session["user"].get("loggedIn"):
        if session['user']['admin'] == False:
            return redirect('/logout')
    else:
        return redirect("/logout")
    return render_template("media/edit.html",**locals())

@app.route("/")
@app.route("/events")
async def events_all():
    events = await Event.get_all()
    return render_template("dashboard/dashboard/event/index.html")

@app.route("/events/<string:title>")
async def event_single(title):
    event = await Event.find_slug(title)
    return render_template("dashboard/dashboard/event/event.html")

@app.route("/events/<string:title>/<string:tag>")
async def event_tag(title,tag):
    event = await Event.find_slug(title)
    return render_template("dashboard/dashboard/event/tag.html")


@app.route("/dashboard/myevents/manage",methods=['GET','POST'])
@app.route("/dashboard/events/create",methods=['GET','POST'])
@app.route("/admin/events/create",methods=['GET','POST'])
async def events_create():
    if request.method == 'POST':
        if 'next_tab' in request.form:
            return redirect("#/"+request.form['next_tab'])
    return render_template("dashboard/dashboard/myevents/manage.html",**locals())

@app.route("/dashboard/myevents/manage/<string:title>",methods=['GET','POST'])
async def events_edit(title):
    event = await Event.find_slug(title)
    return render_template("dashboard/dashboard/myevents/manage.html",**locals())

@app.route("/dashboard/mybookings/<int:id>")
async def bookings_view(id):
    return render_template("dashboard/dashboard/mybookings/booking.html",**locals())

@app.route("/dashboard/myearning")
async def earnings():
    return render_template("dashboard/dashboard/myevents/earnings.html",**locals())

@app.route("/dashboard/ticket-scan")
async def scan():
    return render_template("dashboard/dashboard/myevents/scan.html",**locals())

@app.route("/template/<string:files>")
async def load_files(files):
    return render_template("dashboard/dashboard/"+files)



if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)