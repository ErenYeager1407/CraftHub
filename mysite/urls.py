
from django.contrib import admin
from django.urls import path

import myapp.views

urlpatterns = [
    path("", myapp.views.home),
    path("about-us/", myapp.views.about),
    path("add-student/", myapp.views.addstd),
    path("insstd/", myapp.views.insstd),
    path("dashboard/", myapp.views.dashboard),
    path("addProduct/", myapp.views.addProduct),
    path("insproduct/", myapp.views.insproduct),
    path("listproducts/", myapp.views.listproducts),
    path("delproduct/", myapp.views.delproduct),
    path("editproduct/", myapp.views.editproduct),
    path("updproduct/", myapp.views.updproduct),
    path("adminlogin/", myapp.views.adminlogin),
    path("login_check/", myapp.views.login_check)



]
