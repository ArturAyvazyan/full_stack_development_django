from django.shortcuts import render
from django.contrib import messages
from glavnaya import models
from glavnaya.models import Work

#Exampple of what view with mobile must looks like
# def home(request):
#     Workas = Work.objects.all()
#     AGENTS = request.user_agent.is_mobile
#     if AGENTS:
#         print('count')
#         return render(request, 'home.html')
#     else:
#         print('conch')
#         return render(request, 'works/golova.html', {
#         'Workas': Workas
#     })

def home(request):
    return render(request, 'home.html')

def who(request):
    return render(request, 'checker/who.html')

def demo(request):
    return render(request, 'checker/demo.html')

def demo2(request):
    return render(request, 'checker/demo2.html')

def demo3(request):
    return render(request, 'checker/demo3.html')

def demo4(request):
    return render(request, 'checker/demo4.html')

def demo5(request):
    return render(request, 'checker/demo5.html')

def golova(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/golova.html', {
        'Workas': Workas
    })


def eye(request):
    # Здесь выбрать конкретную работу и в темплейтах поменять Воркас
    Workas = Work.objects.all()
    return render(request, 'works_desktop/eye.html', {
        'Workas': Workas
    })


def kosmos(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/kosmos.html', {
        'Workas': Workas
    })


def zakis(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/zakis.html', {
        'Workas': Workas
    })


def maski(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/maski.html', {
        'Workas': Workas
    })


def vibe(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/vibe.html', {
        'Workas': Workas
    })
