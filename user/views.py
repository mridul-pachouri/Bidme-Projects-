from django.shortcuts import render,redirect
from django.conf import settings
from myadmin import models as  myadmin_models

MEDIA_URL=settings.MEDIA_URL

#middleware to check session for user routes
def sessioncheckuser_middleware(get_response):
	def middleware(request):
		if request.path=='/user/' :
			if request.session['sunm']==None or request.session['srole']!="user":
				response = redirect('/login/')
			else:
				response = get_response(request)
		else:
			response = get_response(request)		
		return response	
	return middleware


# Create your views here.
def userhome(request):
     return render(request,"userhome.html",{"sunm":request.session["sunm"]})
def viewcategory(request):
    clist=myadmin_models.Category.objects.all()
    return render(request,"viewcategory.html",{"sunm":request.session["sunm"],"clist":clist,"MEDIA_URL":MEDIA_URL})
 