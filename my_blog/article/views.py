from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from article.models import Article
from datetime import datetime


# Create your views here.

def home(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExit:
        raise Http404

    content_dict={
        'post_list': post_list
    }
    return render(request, 'home.html', content_dict)


def detail(request, post_id):
    content_dict = {}
    # post = Article.objects.get(id = post_id)
    post = get_object_or_404(Article, id=post_id)
    # output_str = ("title=%s, category=%s, date=%s, content=%s" % (post.title, post.category, post.date, post.content))
    # return HttpResponse(output_str)
    content_dict['post'] = post
    return render(request, 'detail.html', content_dict)


def archive(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExit:
        raise Http404

    content_dict={
        'post_list': post_list,
        'error': False
    }
    return render(request, 'archive.html', content_dict)


def about(request):
    return render(request, 'about.html', {'current_time': datetime.now()})


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__icontains = tag)
    except Article.DoesNotExit:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


def blog_search(request):
    if 'search' in request.GET:
        s = request.GET['search']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0:
                return render(request, 'archive.html', {'post_list': post_list,
                                                        'error': True})
            else:
                return render(request, 'archive.html', {'post_list': post_list,
                                                        'error': False})
    return redirect('/')