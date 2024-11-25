from django.urls import path
from crudapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('addstudy',views.addstudy,name="addstudy"),
    path('select/<id>',views.selectdata,name="selectdata"),
    path('update/<id>',views.updatedata,name="updatedata"),
    path('delete',views.delete,name="delete")
]