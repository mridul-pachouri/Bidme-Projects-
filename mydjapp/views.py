from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models
import time

#middleware to check session for mainapp routes
def sessioncheck_middleware(get_response):
	def middleware(request):
		if request.path=='/home/' or request.path=='/about/' or request.path=='/contact/' or request.path=='/login/' or request.path=='/service/' or request.path=='/register/':
			request.session['sunm']=None
			request.session['srole']=None
			response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware




def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")
def register(request):
    if request.method=="GET":
        return render(request,"register.html",{"output":"text"})
    else:
        #print(request.POST)
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        mobile=request.POST.get("mobile")
        address=request.POST.get("address")
        city=request.POST.get("city")
        gender=request.POST.get("gender")                                                                                                   
        info=time.asctime()
        
        #insert data using mobile class 
        p=models.Register(name=name,email=email,password=password,mobile=mobile,address=address,city=city,gender=gender,status=0,role="user",info=info)
        p.save()
        
        return render(request,"register.html",{"User register successfully"})
    
def login(request):
    if request.method=="GET":
        return render(request,"login.html",{"output":""})
    else:
        #to get data from login form
        email=request.POST.get("email")
        password=request.POST.get("password")    

        #match above details in models to make login
        userDetails=models.Register.objects.filter(email=email,password=password,status=1)

        #print(userDetails)
        if len(userDetails)>0:

            #to store user details is session
            request.session["sunm"]=userDetails[0].email
            request.session["srole"]=userDetails[0].role            

            if userDetails[0].role=="admin":
                return redirect("/myadmin/")
            else:
                return redirect("/user/")                 
        else:
            return render(request,"login.html",{"output":"Invalid user , please login again...."})
def about(request):
    return render(request,"about.html")
def home(request):
    return render(request,"home.html")

   
   
   
   
   
   