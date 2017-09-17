from django.shortcuts import render, render_to_response
from gamma.models import Projects,Models,Services,News,Gallery,Image,ServicesSecond,ImageGallery,HomePhoto

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404, get_object_or_404



def index(request):
    content = {
        'Projects' : Projects.objects.all(),
        'Photos' : HomePhoto.objects.all(),
        'Models' : Models.objects.all(),
    }
    return render(request, 'home.html', content)

def services(request):
    content = {
        'Photos' : HomePhoto.objects.all(),
        'Services' : Services.objects.all(),

    }
    return render(request, 'services.html', content)

def service(request, pk):
    content = {
        'Services' : Services.objects.filter(pk=pk),
        'ServicesSecond' : ServicesSecond.objects.filter(service=pk),
    }
    return render(request, 'service.html', content)

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
        'Gallery' : Gallery.objects.all(),
    }
    return render(request, 'gallery.html', content)

def photogallery(request, pk):
    content = {
        'Gallery' : ImageGallery.objects.filter(gallery=pk),
    }
    return render(request, 'photogallery.html', content)



def news(request):
    content = {
        'News' : News.objects.all(),
    }
    return render(request, 'news.html', content)

def contact(request):

    return render(request, 'contact.html', content)
