from django.shortcuts import render, HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    context={'message':'AniMouth'}
    template = loader.get_template("animouth/index.html")
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, "animouth/about.html", {'title':'about us page'})

def index(request):
    return render(request, "animouth/index.html", {'title':'home page'})