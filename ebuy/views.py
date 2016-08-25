from django.shortcuts import render_to_response
#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def  home(request):
	#site_name = "EBUY"
	#response = "Welcome to %s." % site_name
	#return HttpResponse(response)
	return render_to_response("ebuy/index.html")
