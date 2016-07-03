from django.shortcuts import render
from django.http import Http404
from .forms import CommentForm
# Create your views here.

from .models import Blog
from .models import Comment

def fenye_blog(request,yeshu):
    a=int(yeshu)
    ctx={
        'str':yeshu,
        'blogs': Blog.objects.all()[(a-1)*5:a*5]
    }
    return render(request, 'fenye.html', ctx,)

def get_blogs(request):
    ctx = {
        'blogs': Blog.objects.all().order_by('-created')[0:5]
    }
    return render(request, 'index.html', ctx)


def get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'detail.html', ctx)

def base(request):
    return render(request, 'base.html')
