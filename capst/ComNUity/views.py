# from tkinter import Variable
from urllib.request import Request
from django.forms import EmailField
from django.shortcuts import render
import time
from datetime import datetime, timezone
import time
import pytz
from pyrebase import pyrebase
from firebase import firebase
from django.contrib import sessions
from django.contrib.auth import logout

config = {
  "apiKey": "AIzaSyArCkk4P0MrgoLc7IGN8uJgSPkd1JrlxR4",
  "authDomain": "comnuity-d42e8.firebaseapp.com",
  "databaseURL": "https://comnuity-d42e8-default-rtdb.firebaseio.com/",
  "projectId": "comnuity-d42e8",
  "storageBucket": "comnuity-d42e8.appspot.com",
  "messagingSenderId": "797236358165",
  "appId": "1:797236358165:web:ead4864b9ef85cf1eb721c",
  "measurementId": "G-W08WKGYPFY"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database =  firebase.database()
#Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def signIn(request):
    return render(request,"index.html")

def home(request):
    interest= request.POST.getlist("activity")
    extra = request.POST['extra']
    email= request.session['em']
    # stop=str(extra).replace(" ","")
    
    li = list(extra.split(","))
    interest.extend(li)
    data={
        "interest":interest,
    }
    print(email)
    database.child('users').child('interests').child(email).set(data)
    e = database.child('users').child('profile').child(email).child('fname').get().val()
    print(e)
    return render(request,"dash.html",{'e':e})

def dash(request):
    email= request.session['em']
    e = database.child('users').child('profile').child(email).child('fname').get().val()
    print(e)
    return render(request,"dash.html",{'e':e})
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    request.session['email'] = email
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"index.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"home.html",{"email":email})

# def logout(request):
#     try:
#         del request.session['uid']
#     except:
#         pass
#     return render(request,"login.html")
 
def signUp(request):
    return render(request,"registration.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     ema = email.replace('.','-')
     request.session['em'] = ema
     print(email)
     print("....... .....",email)
     
        # creating a user with the given email and password
     print(".......akshit .....",)
     user=authe.create_user_with_email_and_password(email,passs)
     print(".......akshit1 .....",)
     #uid = user['localId']
     print(".......akshit2 .....",)
     print(request.session.keys)
     for key, value in request.session.items():
        print(".......akshit4 .....")
        print('{} => {}'.format(key, value))
    #  idtoken = request.session['uid']
     print(".......akshit3 .....")
     #print("....... .....",uid)
     
         
     print("....... .....",passs)
     return render(request, "profile.html")


def profile(request):
    return render (request,'profile.html')

def showprofile(request):
    chk= request.session['em']
    butt=request.POST.get("butt")
    if butt=="Edit":
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        dob= request.POST.get('dob')
        about= request.POST.get('about')
        gender= request.POST.get('gender')
        number= request.POST.get('number')
        email= request.POST.get('email')
        country= request.POST.get('country')
        state=request.POST.get('state')
        url= request.POST.get('url')

        database.child('users').child('profile').child(chk).update({"fname":fname})
        database.child('users').child('profile').child(chk).update({"lname":lname})
        database.child('users').child('profile').child(chk).update({"dob":dob})
        database.child('users').child('profile').child(chk).update({"about":about})
        database.child('users').child('profile').child(chk).update({"email":email})
        database.child('users').child('profile').child(chk).update({"number":number})
        database.child('users').child('profile').child(chk).update({"gender":gender})
        database.child('users').child('profile').child(chk).update({"state":state})
        database.child('users').child('profile').child(chk).update({"country":country})
        database.child('users').child('profile').child(chk).update({"image":url})

        fname = database.child('users').child('profile').child(chk).child('fname').get().val()
        lname = database.child('users').child('profile').child(chk).child('lname').get().val()
        number = database.child('users').child('profile').child(chk).child('number').get().val()
        date = database.child('users').child('profile').child(chk).child('dob').get().val()
        ema = database.child('users').child('profile').child(chk).child('email').get().val()
        country = database.child('users').child('profile').child(chk).child('country').get().val()
        state = database.child('users').child('profile').child(chk).child('state').get().val()
        fb = database.child('users').child('profile').child(chk).child('fb').get().val()    
        insta = database.child('users').child('profile').child(chk).child('insta').get().val()
        gender = database.child('users').child('profile').child(chk).child('gender').get().val()
        about = database.child('users').child('profile').child(chk).child('about').get().val()
        url = database.child('users').child('profile').child(chk).child('image').get().val()

        # return render(request,'showprofile.html')
        return render (request,'showprofile.html',{"fname":fname,"lname":lname,"number":number,"date":date,"email":ema,"country":country,"state":state,"fb":fb,"insta":insta,"gender": gender,"about":about,"url":url})

    fname = database.child('users').child('profile').child(chk).child('fname').get().val()
    lname = database.child('users').child('profile').child(chk).child('lname').get().val()
    number = database.child('users').child('profile').child(chk).child('number').get().val()
    date = database.child('users').child('profile').child(chk).child('dob').get().val()
    ema = database.child('users').child('profile').child(chk).child('email').get().val()
    country = database.child('users').child('profile').child(chk).child('country').get().val()
    state = database.child('users').child('profile').child(chk).child('state').get().val()
    fb = database.child('users').child('profile').child(chk).child('fb').get().val()    
    insta = database.child('users').child('profile').child(chk).child('insta').get().val()
    gender = database.child('users').child('profile').child(chk).child('gender').get().val()
    about = database.child('users').child('profile').child(chk).child('about').get().val()
    url = database.child('users').child('profile').child(chk).child('image').get().val()
    print(gender)
    print(state)

    return render (request,'showprofile.html',{"fname":fname,"lname":lname,"number":number,"date":date,"email":ema,"country":country,"state":state,"fb":fb,"insta":insta,"gender": gender,"about":about,"url":url})

def edprofile(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    number = request.POST.get('number')
    dob = request.POST.get('dob')
    email = request.POST.get('email')
    about = request.POST.get('about')
    gender = request.POST.get('gender')
    image = request.POST.get('url')

    chk=request.session['em']

    data = {
        "fname":fname, 
        "lname":lname, 
        "number":number, 
        "dob":dob, 
        "email":email, 
        "about":about, 
        "gender":gender, 
        "image":image,
    }

    print(data)

    database.child('users').child('profile').child(chk).set(data)
    return render(request,'editprofile.html')

def editprofile(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    number = request.POST.get('number')
    dob = request.POST.get('dob')
    email = request.POST.get('email')
    about = request.POST.get('about')
    gender = request.POST.get('gender')
    image = request.POST.get('url')

    chk=request.session['em']

    data = {
        "fname":fname, 
        "lname":lname, 
        "number":number, 
        "dob":dob, 
        "email":email, 
        "about":about, 
        "gender":gender, 
        "image":image,
    }

    print(data)

    database.child('users').child('profile').child(chk).set(data)
    
    return render(request,'showprofile.html')

def createprofile(request):
    tz = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    milli = int(time.mktime(time_now.timetuple()))
    
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    number = request.POST.get('number')
    dob = request.POST.get('dob')
    email = request.POST.get('email')
    about = request.POST.get('about')
    gender = request.POST.get('gender')
    image = request.POST.get('url')
    country = request.POST.get('country')
    state = request.POST.get('state')

    chk=request.session['em']
    print(chk)
    # request.session['email'] = email

    #idtoken = request.session['uid']
    # print("..... ......", idtoken)
    # a = authe.get_account_info(idtoken)
    # a = ['localId']
    data = {
        "fname":fname, 
        "lname":lname, 
        "number":number, 
        "dob":dob, 
        "email":email, 
        "about":about, 
        "gender":gender, 
        "image":image,
        "country":country,
        "state":state,
    }

    database.child('users').child('profile').child(chk).set(data)
    return render(request, 'home.html')


def logout(request):
    logout(request)
    return render(request, 'index.html')


def createblog(request):
    # if request.POST.get('Send')=='Post':
    #     comment=request.POST.get('comment')
    #     database.child('comments')
    # tz = pytz.timezone('Asia/Kolkata')
    # time_now = datetime.now(timezone.utc).astimezone(tz)
    # milli = int(time.mktime(time_now.timetuple()))
    # date=str(datetime.fromtimestamp(milli/1000))
    date=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print(date)
    chk=request.session['em']
    email=database.child('users').child('profile').child(chk).child('email').get().val()
    title=request.POST.get('title')
    group=request.POST.get('group')
    about=request.POST.get('about')
    image=request.POST.get('url')
    data={
        "title":title,
        "group":group,
        "about":about,
        "image":image,
        "email":email,
        "date":date,
    }
    database.child("blogs").child(title).set(data)
    blogs = database.child('blogs').get().val()
    dat = list(blogs.items())
    print(dat)
    groups=[]
    abouts=[]
    titles=[]
    dates=[]
    uname=database.child('users').child('profile').child(chk).child('fname').get().val()
    for i in dat:
        titles.append(i[0])
        #titles.append(i[1])
    print(titles)
    print(uname)
    for j in titles:
        groups.append(database.child('blogs').child(j).child('group').get().val())
        abouts.append(database.child('blogs').child(j).child('about').get().val())
        dates.append(database.child('blogs').child(j).child('date').get().val())
    print(groups)
    print(abouts)
    print(dates)
    # for j in groups:
    #     chk=database.child('blogs').child(j).child(chk).get().val()
    #     tmp=list(chk.items())
    #     print(tmp)
    #     for k in tmp:
    #         titles.append(k[0])
    #     print(titles)
    #     # about=database.child('blogs').child(j).child(chk).get().val()
    #     # print(about)
    #     # for l in titles:
    #     #     about=database.child('blogs').child(j).child(chk).child(l).child('about').get().val()
    #     #     print(about)
    #     #     abouts.append(about)
    com_list=zip(titles,abouts,groups,dates)
    return render(request,'createblog.html',{'com_lis':com_list,'fname':uname})

def addblog(request):
    return render(request,'addblog.html')

def makeblog(request):
    return render(request,'createblog.html')

