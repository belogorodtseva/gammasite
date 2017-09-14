from django.shortcuts import render, render_to_response
from gamma.models import Projects,Models,Services,News,Gallery,Image
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404



def index(request):
    content = {
        'Projects' : Projects.objects.all(),
        'Services' : Services.objects.all(),
        'Models' : Models.objects.all(),
    }
    return render(request, 'home.html', content)

def projects(request):
    content = {
        'Projects' : Projects.objects.all(),
        'Models' : Models.objects.all(),
    }
    return render(request, 'projects.html', content)

def project(request, pk):
    content = {
        'Models' : Models.objects.all(),
        'Project' : Projects.objects.filter(pk=pk),
        'Image' : Image.objects.filter(project=pk),
    }
    return render(request, 'project.html', content)

def gallery(request):
    content = {
        'Gallery' : gallery.objects.all(),
    }
    return render(request, 'gallery.html', content)


def news(request):
    content = {
        'News' : News.objects.all(),
    }
    return render(request, 'news.html', content)

def contact(request):

    return render(request, 'contact.html', content)
