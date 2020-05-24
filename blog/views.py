from django.shortcuts import render
from .models import Post,Group
from django.core.mail import send_mail
from django.conf import settings


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
		send_mail( request.POST['sub'], request.POST['msg'], settings.EMAIL_HOST_USER,['mesrop.araqelyan.09@gmail.com'])
	return render(request,'contact.html',{'group':group})