from django.contrib import admin
from django.urls import path
from sensor import views
from django.conf.urls.static import static
from django.conf import settings
from sensor.views import ServiceWorker

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("Login/", views.userlogin, name="Login"),
    path("Home/", views.home, name="Home"),
    path("device-register/", views.Dashboard, name="Dashboard"),
    path("DailyRecords/", views.daily_records, name="DailyRecords"),
    path("Reports/", views.Reports, name="Reports"),
    path("logout/", views.logoutuser, name="logoutuser"),
    path("charts/", views.charts, name="charts"),
    path("register/", views.register_user, name="register"),
    path("chartsData/", views.chartsData, name="chartsData"),
    path('', ServiceWorker.as_view(), name="sw"),
]
