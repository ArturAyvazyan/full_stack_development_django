from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from glavnaya import models
from glavnaya.models import Zakaz
from .forms import ZakazForm

def home(request):
    if request.method == 'POST':
        what = 'send_message'

        soobch_name = request.POST.get('name', False)
        soobch_email = request.POST.get('email', False)
        soobch_message = request.POST.get('soobch', False)
        
        message = f"""СООБЩЕНИЕ С ГЛАВНОЙ: {what}, 
        ИМЯ: {soobch_name}, 
        e-mail: {soobch_email}, 
        СУТЬ: {soobch_message}, """

        if soobch_name == False:
            return render(request, 'home.html', {'send_message':what})
        else:
            send_mail (
                what, #subject
                message, #message
                soobch_email, #from Email
                ['archiforeverything@gmail.com'], #To Email
                fail_silently=True,
                )
            return render(request, 'home.html')
        
    else:
        return render(request, 'home.html')

def who(request):
    if request.method == 'POST':    
        soobch = True
        return render(request, 'checker/who.html', {'soobch':soobch})
    else:
        return render(request, 'checker/who.html')

def demo(request):
    return render(request, 'checker/demo.html')

def demo4(request):
    if request.method == 'POST':
        eye = 'ГЛАЗ'
        zayavka_name = request.POST.get('zayavka-name', False)
        zayavka_email = request.POST.get('zayavka-email', False)
        zayavka_city = request.POST.get('zayavka-city', False)
        
        otpravka = request.POST.get('otpravka')
        
        payment = request.POST.get('payment')
        
        better = request.POST.get('better', False)
        better_more = request.POST.get('better_more', False)
  
        koment = request.POST.get('koment', False)

        message = f"""Заявка на покупку работы: {eye},
        ИМЯ: {zayavka_name}, 
        e-mail: {zayavka_email}, 
        Город: {zayavka_city}, 
        Отправка через: {otpravka},
        Оплата следующим способом: {payment},
        Дополнительный способ связи: {better} : {better_more},
        Комментарий к заказу: {koment}."""

        
        if zayavka_name == False:
            return render(request, 'checker/demo4.html', {'eye':eye})
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
    if request.method == 'POST':
            golova = 'ПУТЬ'
            zayavka_name = request.POST.get('zayavka-name', False)
            zayavka_email = request.POST.get('zayavka-email', False)
            zayavka_city = request.POST.get('zayavka-city', False)
            otpravka = request.POST.get('otpravka')
            payment = request.POST.get('payment')
            koment = request.POST.get('koment', False)

            message = f"""Заявка на покупку работы: {golova},
            ИМЯ: {zayavka_name}, 
            e-mail: {zayavka_email}, 
            Город: {zayavka_city}, 
            Отправка через: {otpravka},
            Оплата следующим способом: {payment},
            Комментарий к заказу: {koment}."""

            
            if zayavka_name == False:
                return render(request, 'works_desktop/golova.html', {'golova':golova})
            else:        
                send_mail (
                    golova, #subject
                    message, #message
                    zayavka_email, #from Email
                    ['archiforeverything@gmail.com'], #To Email
                    fail_silently=False,
                    )
                return render(request, 'home.html')
    else:
        return render(request, 'works_desktop/golova.html')

def krolik(request):
    return render(request, 'works_desktop/krolik.html')

def panno(request):
    if request.method == 'POST':
            panno = 'ПАННО'
            zayavka_name = request.POST.get('zayavka-name', False)
            zayavka_email = request.POST.get('zayavka-email', False)
            zayavka_city = request.POST.get('zayavka-city', False)
            otpravka = request.POST.get('otpravka')
            payment = request.POST.get('payment')
            koment = request.POST.get('koment', False)

            message = f"""Заявка на покупку работы: {panno},
            ИМЯ: {zayavka_name}, 
            e-mail: {zayavka_email}, 
            Город: {zayavka_city}, 
            Отправка через: {otpravka},
            Оплата следующим способом: {payment},
            Комментарий к заказу: {koment}."""

            
            if zayavka_name == False:
                return render(request, 'works_desktop/panno.html', {'panno':panno})
            else:        
                send_mail (
                    panno, #subject
                    message, #message
                    zayavka_email, #from Email
                    ['archiforeverything@gmail.com'], #To Email
                    fail_silently=False,
                    )
                return render(request, 'home.html')
    else:
        return render(request, 'works_desktop/panno.html')

def eye(request):
    if request.method == 'POST':
        eye = 'ГЛАЗ'
        zayavka_name = request.POST.get('zayavka-name', False)
        zayavka_email = request.POST.get('zayavka-email', False)
        zayavka_city = request.POST.get('zayavka-city', False)
        otpravka = request.POST.get('otpravka')
        payment = request.POST.get('payment')
        koment = request.POST.get('koment', False)

        message = f"""Заявка на покупку работы: {eye},
        ИМЯ: {zayavka_name}, 
        e-mail: {zayavka_email}, 
        Город: {zayavka_city}, 
        Отправка через: {otpravka},
        Оплата следующим способом: {payment},
        Комментарий к заказу: {koment}."""

        
        if zayavka_name == False:
            return render(request, 'works_desktop/eye.html', {'eye':eye})
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
        return render(request, 'works_desktop/eye.html')

def kosmos(request):
    return render(request, 'works_desktop/kosmos.html')

def zakis(request):
    if request.method == 'POST':
        zakis = 'ЗАКИС'
        zayavka_name = request.POST.get('zayavka-name', False)
        zayavka_email = request.POST.get('zayavka-email', False)
        zayavka_city = request.POST.get('zayavka-city', False)
        otpravka = request.POST.get('otpravka')
        payment = request.POST.get('payment')
        koment = request.POST.get('koment', False)

        message = f"""Заявка на покупку работы: {zakis},
        ИМЯ: {zayavka_name}, 
        e-mail: {zayavka_email}, 
        Город: {zayavka_city}, 
        Отправка через: {otpravka},
        Оплата следующим способом: {payment},
        Комментарий к заказу: {koment}."""

        
        if zayavka_name == False:
            return render(request, 'works_desktop/zakis.html', {'zakis':zakis})
        else:        
            send_mail (
                zakis, #subject
                message, #message
                zayavka_email, #from Email
                ['archiforeverything@gmail.com'], #To Email
                fail_silently=False,
            )
            return render(request, 'home.html')
    else:
        return render(request, 'works_desktop/zakis.html')

def maski(request):
    if request.method == 'POST':
        maski = 'МАСКИ'
        zayavka_name = request.POST.get('zayavka-name', False)
        zayavka_email = request.POST.get('zayavka-email', False)
        zayavka_city = request.POST.get('zayavka-city', False)
        otpravka = request.POST.get('otpravka')
        payment = request.POST.get('payment')
        koment = request.POST.get('koment', False)

        message = f"""Заявка на покупку работы: {maski},
        ИМЯ: {zayavka_name}, 
        e-mail: {zayavka_email}, 
        Город: {zayavka_city}, 
        Отправка через: {otpravka},
        Оплата следующим способом: {payment},
        Комментарий к заказу: {koment}."""

        
        if zayavka_name == False:
            return render(request, 'works_desktop/maski.html', {'maski':maski})
        else:        
            send_mail (
                maski, #subject
                message, #message
                zayavka_email, #from Email
                ['archiforeverything@gmail.com'], #To Email
                fail_silently=False,
            )
            return render(request, 'home.html')
    else:
        return render(request, 'works_desktop/maski.html')

def vibe(request):
    return render(request, 'works_desktop/vibe.html')