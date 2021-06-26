from flask import Flask, render_template, session, redirect, request, json, flash
from flask_hashing import Hashing
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from flask_uploads import IMAGES, UploadSet, configure_uploads
import json
import os
import braintree
from werkzeug.datastructures import ImmutableOrderedMultiDict
import requests

with open('config.json','r') as c:
    params = json.load(c)['params']

local_server = False

#UPLOAD_FOLDER = '/path/to/the/uploads'
#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24)


#app.secret_key = 'key'
db = SQLAlchemy(app)
hashing = Hashing(app)

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

key_list=[]

if (local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['pro_uri']

db = SQLAlchemy(app)


class Blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=False, nullable=False)
    title = db.Column(db.String(120),unique=False,nullable=False)
    content = db.Column(db.String(),unique=False,nullable=False)
    img = db.Column(db.VARCHAR(22),unique=True,nullable=False)
    date_time = db.Column(db.String(15),unique=False,nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=False,nullable=False)
    email = db.Column(db.VARCHAR(50),unique=True,nullable=False)
    img = db.Column(db.VARCHAR(22),unique=True,nullable=True)
    password = db.Column(db.VARCHAR(50),unique=True,nullable=False)
    date_time = db.Column(db.String(6),unique=False,nullable=False)

class Upload_img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=False, nullable=False)
    user = db.Column(db.String(50), unique=False, nullable=False)
    date = db.Column(db.String(10),unique=False,nullable=False)
class Bcd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), unique=False, nullable=False)
    title = db.Column(db.String(120),unique=False,nullable=False)
    content = db.Column(db.String(22),unique=False,nullable=False)
    img1 = db.Column(db.String(22),unique=True,nullable=False)
    img2 = db.Column(db.String(22),unique=True,nullable=False)
    tag = db.Column(db.String(50),unique=False,nullable=False)
    date_time = db.Column(db.String(15),unique=False,nullable=False)

#title=title,slug=slug,cotent=content_blog,img1=img1,img2=img2,tag=tag
def verify_email(em):
    try:

        valid = validate_email(em)
        return True
    except EmailNotValidError as e:
        return False
def _upload_img_for_blog_(name_img,request):
    print('ready')
    print('0.3.1')
    if True:
        #user = session['user']
        print('0.3.2')
        user = 'no-user'
        date = datetime.now()
        str1_date = str(date)
        str_date = str1_date.strip()
        str_date = str_date.replace(' ', '-')
        str_date = str_date.replace(':', '-')
        str1_user = str(user)
        str_user = str1_user.strip()
        str_user = str_user.replace(':', '-')
        str_user = str_user.replace('', '-')
        slug = 'app/static/web/photo/'
        name = str_user + str_date
        name = name + '.jpg'
        #message = __save__(slug, name,name_img)
        slug1 = 'static/web/photo/' + name
        entry = Upload_img(slug=slug1, date=str1_date, user=str1_user)
        db.session.add(entry)
        db.session.commit()
        return slug1

@app.route("/")
def index():
    return render_template('index.html',message='Welcome')
@app.route("/gallery")
def _gallery_():
    data = Upload_img.query.all()
    return render_template('pages/gallery.html',images=data)
@app.route("/full-width")
def _full_width_():
    return render_template('pages/full-width.html')
@app.route("/sidebar-left")
def _sidebar_left_():
    return render_template('pages/sidebar-left.html')
@app.route("/sidebar-right")
def _sidebar_right_():
    return render_template('pages/sidebar-right.html')
@app.route("/basic-grid")
def _basic_grid_():
    return render_template('pages/basic-grid.html')
@app.route("/font-icons")
def _font_icons_():
    return render_template('pages/font-icons.html',form_submit='/sign-up')
@app.route('/search')
def __search__():
    if request.method == 'POST':
        key = request.form.get('search')
        if key in list:
            print('yes')
            search = 'yes'
        else:
            print('no')
            search='no'
    return search
@app.route('/.well-known/pki-validation/E5459302673D53989275A6261CBA42EF.txt')
def content():
		return render_template('E5459302673D53989275A6261CBA42EF.txt')
@app.route('/.well-known/pki-validation/')
def content1():
    return redirect('/.well-known/pki-validation/E5459302673D53989275A6261CBA42EF.txt')

@app.route('/sign-up',methods= ['GET','POST'])
def _sign_up_():
    if request.method=='POST':
        name = request.form.get('full-name')
        email = request.form.get('your-email')
        password = request.form.get('password')
        confirm_password = request.form.get('comfirm-password')
        date = datetime.now()
        try:
            valid = validate_email(email)
            e_mail = valid.email
            if validate_email(email) :
                if not(Users.query.filter_by(email=email).first()):
                    if password == confirm_password:
                        pass_word_key = password
                        password = hashing.hash_value(pass_word_key, salt='sha256')
                        entry = Users(name=name, email=e_mail, password=password, date_time=date)
                        db.session.add(entry)
                        db.session.commit()
                        return render_template('index.html', message='SUCCESSFUL SIGN-UP')
                    else:
                        return redirect('/sign-up')
                else:
                    return render_template('Sign-Up.html',message='email_already_exist')
            else:
                return redirect('/sign-up')
        except EmailNotValidError as e:
            return redirect('/sign-up')

    else:
        return render_template('Sign-Up.html',message='Sign-up Here')



@app.route('/log-in',methods= ['GET','POST'])
def _sign_in_():
    if 'user' not in session:
        if request.method == 'POST':

            email = request.form.get('your-email')

            password = request.form.get('password')

            validation = validate_email(email)

            if (validation and Users.query.filter_by(email=email).first()):

                data_user = Users.query.filter_by(email=email).first()
                if data_user:
                    if hashing.check_value(data_user.password, password, salt='sha256'):
                        session['user'] = data_user.id
                        return render_template('index.html',message='Login SUCCESSFUL')
                    else:
                        return render_template('log-in.html', form_submit='/log-in',
                                               error='PASSWORD_OR_EMAIL_NOT_CORRECT')
                else:
                    return render_template('log-in.html', form_submit='/log-in', error='PASSWORD_OR_EMAIL_NOT_CORRECT')

            else:
                return render_template('log-in.html', form_submit='/log-in', error='PASSWORD_OR_EMAIL_NOT_CORRECT')

        else:
            return render_template('log-in.html', form_submit='/log-in', error='')
    else:
        return render_template('index.html',message='Already Loged-in')


@app.route('/logout')
def log_out():
    if 'user' in session:
        if session['user']:
            session.pop('user')
            return render_template('index.html',message='You Logout')
    else:
        return render_template('index.html',message='Already Logout')

@app.route("/upload/img", methods=['GET', 'POST'])
def upload():
    print('ready')
    if request.method == 'POST' and 'photo' in request.files and session['user']=='admin':
        #user = session['user']
        user = 'no-user'
        date = datetime.now()
        str1_date = str(date)
        str_date = str1_date.strip()
        str_date = str_date.replace(' ', '-')
        str_date = str_date.replace(':', '-')
        str1_user = str(user)
        str_user = str1_user.strip()
        str_user = str_user.replace(':', '-')
        str_user = str_user.replace('', '-')
        slug = 'app/static/web/photo/'
        name = str_user + str_date
        name = name + '.jpg'
        message = __save__(slug, name)
        slug1 = 'static/web/photo/' + name
        entry = Upload_img(slug=slug1, date=str1_date, user=str1_user)
        db.session.add(entry)
        db.session.commit()
        # flash("Photo saved successfully.")
        return render_template('index.html', message=message)
    return render_template('upload.html')

@app.route('/admin/dashboard',methods=['POST','GET'])
def __admin_dashboard__():
    if 'user' in session and session['user']=='admin':
        return render_template('admin/index.html',index='/admin/dashboard',profile='/admin/dashboard/profile',table='/admin/dashboard/table',login='/admin/dashboard/login',blank='/admin/dashboard/blank')
    if request.method == 'POST':
        if request.form.get('email')==params['admin-user'] and request.form.get('password')==params['admin-password']:
            session['user']=params['admin-password']
            return render_template('admin/index.html',index='/admin/dashboard',profile='/admin/dashboard/profile',table='/admin/dashboard/table',login='/admin/dashboard/login',blank='/admin/dashboard/blank')
    elif request.method == 'GET':
        return redirect('/admin/dashboard/login')
    

@app.route('/admin/dashboard/profile')
def __admin_dashboard_procfile__():
    return render_template('admin/profile.html',index='/admin/dashboard',profile='/admin/dashboard/profile',table='/admin/dashboard/table',login='/admin/dashboard/login',blank='/admin/dashboard/blank')
@app.route('/admin/dashboard/table')
def __admin_dashboard_table__():
    return render_template('admin/table.html',index='/admin/dashboard',profile='/admin/dashboard/profile',table='/admin/dashboard/table',login='/admin/dashboard/login',blank='/admin/dashboard/blank')
@app.route('/admin/dashboard/login')
def __admin_dashboard_login__():
    return render_template('admin/login.html')
#    return render_template('admin/login.html',index='/admin/dashboard',profile='/admin/dashboard/profile',table='/admin/dashboard/table',login='/admin/dashboard/login',blank='/admin/dashboard/blank')
@app.route('/admin/dashboard/blank')
def __admin_dashboard_blank__():
    return render_template('admin/blank.html',index='/admin/dashboard',profile='/admin/dashboard/profile',table='/admin/dashboard/table',login='/admin/dashboard/login',blank='/admin/dashboard/blank',message='')


@app.route('/admin/dashboard/')
def __admin__dashboard__():
    return redirect('/admin/dashboard')

@app.route('/action',methods=['POST','GET'])
def __action__():
    print(0.01)
    if request.method=='POST' and 'user' in session and session['user']=='admin':
        print(0.1)
        title=request.form.get('title')
        print(1)
        print(1.1)
        print(title)
        print(0.2)
        tag=request.form.get('tag')
        print(2)
        print(2.1)
        print(tag)
        print(0.3)
        content_blog=request.form.get('description')
        print(3.1)
        print(3)
        print(content_blog)
        img1 =_upload_img_for_blog_('img1',request)
        print(4)
        print(img1)
        img2 =_upload_img_for_blog_('img2',request)
        print(5)
        print(img2)
        print(6)
        #print(data)
        print(7)
        # print(content)
        print(8)
        #filename
        name_content= 'name'
        print(9)
        filename = 'name_content'+'.txt'
        print(10)
        f = open(filename, "a")
        print(11)
        f.write(content_blog)
        print(12)
        f.close()
        print(13)
        #to make blog id
        #blog_data=Blogs.query.all()(-1)
        #id = blog_data.id + 1
        #slug='filename'
        #data_to_enter=Bcd(title=title,slug=slug,cotent=content_blog,img1=img1,img2=img2,tag=tag)
        #return content_blog
        return render_template('admin/blank.html', message='SUCCESSFULY_BLOG_UPLOADED')
    else:
        return '<h1>Hello Please Login...</h1>'



if __name__=='__main__':
    app.run(debug=True)


        
#and session['user']=='admin'

