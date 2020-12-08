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


def guy(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/guy.html', {
        'Workas': Workas
    })


def matrix(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/matrix.html', {
        'Workas': Workas
    })


def persik(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/persik.html', {
        'Workas': Workas
    })


def tarelka(request):
    Workas = Work.objects.all()
    return render(request, 'works_desktop/tarelka.html', {
        'Workas': Workas
    })
