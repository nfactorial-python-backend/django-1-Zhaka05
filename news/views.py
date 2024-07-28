from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import News, Comments

def index(request): # get function
    news = News.objects.order_by("-created_at").all() # first question: why objects are got like that?
    context = {"news": news}

    return render(request, "news/index.html", context)

def add_new_info(request): # post function
    print(request)
    new_info_title = request.POST["title"]
    new_info_content = request.POST["text"]
    new_info = News(title=new_info_title, content=new_info_content)
    new_info.save()
    return HttpResponseRedirect(reverse('news:detail', args=(new_info.id, )))


def detail(request, news_id): # get function
    new = get_object_or_404(News, pk=news_id) # 2 question: why new = error, object
    comments = Comments.objects.filter(news_id=news_id).all()
    context = {"new": new, "comments": comments}
    return render(request, "news/detail.html", context)


def add_comment(request, news_id): # get function
    # news = get_object_or_404(News, pk=news_id)
    new = get_object_or_404(News, pk=news_id)
    text = request.POST["comment"] # 3 question: why from request, post comment "comment"
    new_comment = Comments(news=new, content=text)
    new_comment.save()
    return HttpResponseRedirect(reverse('news:detail', args=(news_id, )))
     
    

    # return HttpResponseRedirect("/polls/{{question_id}}")