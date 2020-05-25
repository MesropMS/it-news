from django.shortcuts import render
from .models import Post,Group
from django.contrib import messages


def main(request):
	post = Post.objects.all()
	group = Group.objects.all()
	return render(request,'index.html',{'group':group,'post':post})

def group_detail(request,slug):
	group = Group.objects.all()
	post = Post.objects.filter(group__slug=slug)
	return render(request,'detail.html',{'post':post,'group':group})

def post_detail(request,post_slug):
	group = Group.objects.all()
	post = Post.objects.get(slug=post_slug)
	post.view += 1
	post.save()

	return render(request,'post.html',{'post':post,'group':group})

def about(request):
	group = Group.objects.all()
	return render(request,'about.html',{'group':group})

def contact(request):
	group = Group.objects.all()
	if request.method == 'POST':
		pass
	return render(request,'contact.html',{'group':group})

def search(request):
	group = Group.objects.all()
	if request.method == 'POST':
		search = request.POST['search']
		post = Post.objects.filter(title__icontains=search)
		if post.count() == 0:
			messages.info(request,f'by search {search} result 0')
	return render(request,'detail.html',{'post':post,'group':group})
