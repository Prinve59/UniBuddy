from django.shortcuts import render,redirect
from home.models import CustomUser
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
import re
from datetime import timedelta
from django.utils import timezone


from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.utils.encoding import force_bytes , force_str
from django.core.mail import send_mail,EmailMessage
from .tokens import generate_token
from UniBuddy import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        name=request.POST.get('name')
        year=request.POST.get('year')
        email=request.POST.get('email')
        domain1=request.POST.get('domain1')
        domain2=request.POST.get('domain2')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if not year or not email or not username or not password or not name:
            messages.warning(request, "All fields are required!")
            return redirect('/register')
        if CustomUser.objects.filter(username=username):
            messages.warning(request,"Username already exist,Try new username!")
            return redirect('/register')
        if CustomUser.objects.filter(email=email):
            messages.warning(request,"Email already exist,Try to Login!")
            return redirect('/register')
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters")
            return redirect('/register')
        if(password!=cpassword):
            messages.error(request,"Password not Matching!")
            return redirect('/register')
        if '@kiet.edu' not in email:
            messages.error(request, "Pls use your college Email Id!")
            return redirect('/register')
        password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).+$')
        if not password_regex.match(password):
            messages.error(request, "Password must contain at least one uppercase letter, one number, and one special symbol.")
            return redirect('/register')
        user = CustomUser.objects.create_user(email=email,password=password,username=username,name=name,year=year,domain1=domain1,domain2=domain2,cpassword=cpassword)
        messages.success( request , "Account Created Successfully!\nWe have sent u a confirmation email,Please confirm your email address in order to activate your account.")
        user.is_active=False
        
        current_site=get_current_site(request)
        email_subject="Confirm your email"
        message2=render_to_string('email_confirmation.html',{
            'name':user.username,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user),
        })
        email=EmailMessage(
            email_subject,  
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.fails_silently=True
        email.send()
        user.save()
        return redirect('/')
    return render(request,'register.html')

def activate(request , uidb64 , token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=CustomUser.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,CustomUser.DoesNotExist):
        user=None
    
    if user is not None and generate_token.check_token(user,token):
        time_diff = timezone.now() - user.created_at

        if time_diff > timedelta(hours=4):
            user.delete()
            messages.error(request, "Your activation link has expired. Please register again.")
            return redirect('/register')

        user.is_active=True
        user.save()
        login(request,user)
        return redirect('/')
    else:
        return render(request,'activation_failed.html')

def loginuser(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if not email or not password:
            messages.warning(request,"Oops! Looks like some fields are missing. Try again.")
            return render(request,'login.html') 
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('/')
        else:   
            messages.error(request,"Bad Credentials!")
            # No backend authenticated the credentials
            return render(request,'login.html')
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')
