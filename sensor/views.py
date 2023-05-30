from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
# from .forms import registrationForm, AccountAuthenticationForms
from sensor.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import messages
from .models import sensor_register
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
class ServiceWorker(TemplateView):
    template_name = "templates/sw.js"
    content_type = "application/javascript"

cred = credentials.Certificate("serviceKey.json")


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://connectnodemcu-a8b8d-default-rtdb.firebaseio.com/'
})

def homepage(request):
    return render(request, 'Homepage.html')

from django.contrib.auth.models import User
def register_user(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')

        user = User.objects.create_user(username=username1, email=email1, password=password1, is_superuser=True)
        # Additional fields and save() if needed
        # user.save()

        return user

    return render(request, 'register.html')
def userlogin(request):
    if request.method == 'POST':
        username1 = request.POST.get('login_username')
        password1 = request.POST.get('login_password')
        print(username1, password1)
        user = authenticate(request, username=username1, password=password1)
        print(user)
        print("authenticating user")
        if user is not None:
            login(request, user)
            print("not none")
            return redirect('Home')

        else:
            messages.error(request, "Invalid Credentials!")

    else:
        return render(request, 'Login.html')
    return render(request, 'Login.html')

@login_required
def home(request):

    return render(request, 'home.html')

# @login_required
def Dashboard(request):
    #     return render(request, 'Dashboard.html')
    all2 = sensor_register.objects.all()
    all3 = records.objects.all()
    # print(all2[1].register_no)

    if request.method == 'POST':
        try:
            print(request.POST)
            print('iffff')
            dev_num = request.POST.get('dev_num')
            reg_num = request.POST.get('reg_num')
            longi = request.POST.get('longi')
            lat = request.POST.get('lat')
            date1 = request.POST.get('date')
            time1 = request.POST.get('time')
            sensor_type = request.POST.get('sensor_type')
            plant_name = request.POST.get('plant_name')
            measure1 = request.POST.get('measure')
            plotid = request.POST.get('plotid')
            crop = request.POST.get('crop')
            post = sensor_register(device_no=dev_num, sen_longitude=longi, sen_latitude=lat, date=date1, time_zone=time1,
                                   plant_name=plant_name, sen_type=sensor_type, measurement=measure1, plot_id=plotid, crop=crop)
            post.save()
            print("saved successfully")
            message1 = messages.success(
                request, "Device Registered Successfully!")
            return render(request, 'Dashboard.html', message1)

        except:
            messages.error(request, "Invalid details")
    return render(request, 'Dashboard.html')

@login_required
def daily_records(request):
    context = {}

    data = sensor_register.objects.all()
    plot = request.GET.get('param')
    if request.method == 'POST':
        sensor_register.objects.filter(plot_id=plot, plant_name=request.POST.get(
            'select_plant_name')).update(sensor_value=request.POST.get('sensor_value'))
        messages.success(request, "Value Updated Successfully!")
        print(request.POST.get('select_plant_name'))
        print(sensor_register.objects.filter(plot_id=plot,
              plant_name=request.POST.get('select_plant_name')))
    if request.GET.get('name'):
        maindata = sensor_register.objects.all().filter(
            plot_id=plot, name=request.GET.get('name'))
        context['senseval'] = maindata[0].sensor_value
    else:
        maindata = sensor_register.objects.all().filter(plot_id=plot)
    context['data'] = maindata
    context['num'] = plot

    if request.method == 'POST':
        print("This is in records")
        plant_name2 = request.POST.get('select_plant_name')
        sensor_value2 = request.POST.get('sensor_value')
        post2 = records(plant_name2=plant_name2, sensor_value2=sensor_value2)
        post2.save()

    return render(request, 'read_record.html', context)

@login_required
def Reports(request):
    context = {}
    data = sensor_register.objects.all()
    plot = request.GET.get('param')
    # if request.method == 'POST':
    #     sensor_register.objects.filter(plot_id=plot,plant_name=request.POST.get('display_plant_name')).update(sensor_value=request.POST.get('sensor_value'))
    #     print(request.POST.get('display_plant_name'))
    #     print(sensor_register.objects.filter(plot_id=plot,plant_name=request.POST.get('display_plant_name')))
    # if request.GET.get('name'):
    #     maindata=sensor_register.objects.all().filter(plot_id=plot,name=request.GET.get('name'))
    #     context['senseval']=maindata[0].sensor_value
    # else:
    maindata = sensor_register.objects.all().filter(plot_id=plot)
    if 'param1' in request.GET:
        name = request.GET.get('param1')
        data = sensor_register.objects.all().filter(pk=name)
        history = records.objects.all().filter(plant_name2=data[0].plant_name)
        context['history'] = history
    context['data'] = maindata
    context['num'] = plot
    context['sensors'] = data
    return render(request, 'Reports.html', context)

@login_required
def logoutuser(request):
    logout(request)
    return redirect('homepage')

@login_required
def charts(request):

    firebase_admin.get_app()
    # print("This is realtime data", data)
    ref = db.reference("/DHT/")
    data = ref.get()
    print(data)
    return render(request, 'charts.html',data)
    
@login_required
def chartsData(request):

    firebase_admin.get_app()
    # print("This is realtime data", data)
    ref = db.reference("/DHT/")
    data = ref.get()
    print("In ChartsDatas",data)
    return JsonResponse(data)
