from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Impulse Blog")


def detail(request, post_id):
    content_dict = {}
    # post = Article.objects.get(id = post_id)
    post = get_object_or_404(Article, id=post_id)
    # output_str = ("title=%s, category=%s, date=%s, content=%s" % (post.title, post.category, post.date, post.content))
    # return HttpResponse(output_str)
    content_dict['post'] = post
    return render(request, 'home.html', content_dict)



def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})