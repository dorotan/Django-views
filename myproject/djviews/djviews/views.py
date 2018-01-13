from django.http import HttpResponse, HttpResponseRedirect


# def home(request):
# 	return HttpResponse("<h1>Hello World</h1>")


def home(request):
	response = HttpResponse(content_type="text/html")
	response.content = "<!DOCTYPE html><html><head></head><body><p>Here's the next paragraph</p></body></html>"
	print(response.status_code)
	return response



def redirect_somewhere(request):
	return HttpResponseRedirect('/some/redirect')