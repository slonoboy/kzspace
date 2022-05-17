from datetime import date
from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
import psycopg2
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages


# Create your views here.
# def pageNotFound(request):
#     return HttpResponseBadRequest
conn = psycopg2.connect(
    host="ec2-18-210-191-5.compute-1.amazonaws.com",
    database="d1oalts4gtqfq8",
    user="wpehyswhaauumr",
    password="f481a4d7c5c2edc02cb328ad5d5a2d8e159c50f8e6fcddde3fbd8fe6fd3d5e80")
cursor = conn.cursor()


def documents(request):
    return render(request, 'app1/documents.html')


def login(request):
    if request.method == "POST":
        user = authenticate(request, username='111111111112', password='230801bek')
        if user is not None:
            auth_login(request, user)
            return redirect('/iin')
        else:
            messages.error(request,'wrong password or login')
        return redirect('/')
    return render(request, 'app1/login.html')


def applications(request):
    if request.POST.get('submit'):
        return redirect('five/')
    return render(request, 'app1/applications.html')


def application(request):
    return render(request, 'app1/application.html')


def create_application(request):
    if request.POST.get("button_reg"):
        li = request.POST.getlist("data")
        cursor.execute("insert into mestomogily(iin, last_name, first_name, middle_name, date_of_birth, cause_of_death, kladbishe_name, vera, morg_number, year_death, spravka_o_smerti, id_mogily, lat_coord_mogila, lng_coord_mogila) values ('"+li[0] + "','" +
                       li[1] + "','" + li[2] + "','" + li[3] + "','" + li[4] + "','" + li[5] + "','" + li[6] + "','" + li[7] + "','" + li[8] + "','" + li[9] + "','" + li[10] + "','" + li[11] + "','" + li[12] + "','" + li[13] + "')")
        conn.commit()

    return render(request, 'app1/reg_usopshi.html')


def cemetery(request):
    return render(request, 'app1/vybor_kladbisha.html')


def iin(request):
    account = Account.objects.filter(user=request.user).first()
    person = Person.objects.filter(id=account.person.id).first()
    if request.method == "POST":
        iin = request.POST.get("iin")
        deceased = Deceased.objects.filter(person__iin=iin).first()
        person = None
        if deceased:
            person = Person.objects.filter(iin=iin).first()
            application = Application.objects.create(
                account = account,
                deceased = deceased
            )
            application.save()
            
        return render(request, 'app1/application.html')
        
    return render(request, 'app1/iin_page.html')
