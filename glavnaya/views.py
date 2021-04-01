from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail

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
    if request.method == 'POST':    
        soobch = True
        return render(request, 'checker/who.html', {'soobch':soobch})
    else:
        return render(request, 'checker/who.html')

def demo(request):
    
    return render(request, 'checker/demo.html')

def demo2(request):
    if request.method == 'POST':
        eye = 'ГЛАЗ'
        zayavka_name = request.POST.get('zayavka-name', False)
        zayavka_email = request.POST.get('zayavka-email', False)
        zayavka_city = request.POST.get('zayavka-city', False)
        
        otpravka = request.POST.get('otpravka')
        
        payment = request.POST.get('payment')

        phone_number = request.POST.get('phone-number', False)
        telegram = request.POST.get('telegram', False)
        whats_up = request.POST.get('whats-up', False)
        inst = request.POST.get('inst', False)    
        comment = request.POST.get('comment', False)

        message = f"""Заявка на покупку работы: {eye},
        ИМЯ: {zayavka_name}, 
        e-mail: {zayavka_email}, 
        Город: {zayavka_city}, 
        Отправка через: {otpravka},
        Оплата следующим способом: {payment},
        Номер телефона: {phone_number},
        Телега: {telegram},
        ВАЦАП: {whats_up},
        ИНСТ: {inst},
        Комментарий к заказу: {comment}."""

        if zayavka_name == False:
            return render(request, 'checker/demo2.html', {'eye':eye})
        else:        
            send_mail (
                eye, #subject
                message, #message
                zayavka_email, #from Email
                ['archiforeverything@gmail.com'], #To Email
                fail_silently=False,
                )
            return render(request, 'home.html')
    else:
        return render(request, 'checker/demo2.html')

def demo3(request):
    return render(request, 'checker/demo3.html')

def demo4(request):
    if request.method == 'POST':
        eye = 'ГЛАЗ'
        zayavka_name = request.POST.get('zayavka-name', False)
        zayavka_email = request.POST.get('zayavka-email', False)
        zayavka_city = request.POST.get('zayavka-city', False)
        
        otpravka = request.POST.get('otpravka')
        payment = request.POST.get('payment')

        phone_number = request.POST.get('phone-number', False)
        telegram = request.POST.get('telegram', False)
        whats_up = request.POST.get('whats-up', False)
        inst = request.POST.get('inst', False)    
        comment = request.POST.get('comment', False)

        message = f"""Заявка на покупку работы: {eye},
        ИМЯ: {zayavka_name}, 
        e-mail: {zayavka_email}, 
        Город: {zayavka_city}, 
        Отправка через: {otpravka},
        Оплата следующим способом: {payment},
        Номер телефона: {phone_number},
        Телега: {telegram},
        ВАЦАП: {whats_up},
        ИНСТ: {inst},
        Комментарий к заказу: {comment}."""
        
        send_mail (
            eye, #subject
            message, #message
            zayavka_email, #from Email
            ['archiforeverything@gmail.com'], #To Email
            fail_silently=False,
            )
        return render(request, 'checker/demo4.html')
    else:
        return render(request, 'checker/demo4.html')

def demo5(request):
    if request.method == 'POST':    
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        #send an email
        send_mail (
            message_name, #subject
            message, #message
            message_email, #from Email
            ['archiforeverything@gmail.com'], #To Email
            fail_silently=False,
            )
        return render(request, 'checker/demo5.html', {'message_name': message_name})
    else:
        return render(request, 'checker/demo5.html', {})



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
