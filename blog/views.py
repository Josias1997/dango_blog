from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from datetime import datetime

# Create your views here.


def home(request):
    """
    Non valid HTML page example
    :param request:
    :return: HttpResponse
    """
    return HttpResponse("""
        <h1>Welcome to my blog ! </h1>
        <p>Breton creeps are really delicious !</p1>
    """)


def view_article(request, id_article):
    """
    Return an article according to the ID Passed in the url
    :param request:
    :param id_article:
    :return:
    """
    if id_article > 100:
        raise Http404
    return redirect(view_article, id_article=42)


def view_redirection(request):
    return HttpResponse("You've been redirected")


def list_articles_by_tag(request, tag):
    """

    :param request:
    :param tag:
    :return:
    """
    return redirect("https://www.djangoproject.com")


def list_articles(request, year, month):
    """

    :param request:
    :param year:
    :param month:
    :return:
    """
    return HttpResponse(
        f"You've asked for the article of {month}-{year}"
    )


def actual_date(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, number1, number2):
    total = number1 + number2
    return render(request, 'blog/addition.html', locals())

