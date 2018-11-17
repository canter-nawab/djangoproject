from django.shortcuts import render
from django.http import HttpResponse
from .models import Banners,Entry

# Create your views here.
def index(request):
	#return HttpResponse('Hello from posts')
	posts = Banners.objects.all()[:10]

	context ={
		'title': 'Pashma Ads Private Limited',
		'posts': posts

	}
	return render(request, 'posts/index.html',context)


def details(request, id):
	post = Posts.objects.get(id=id)

	context ={
		'post': post
	}
	
	return render(request, 'posts/details.html',context)