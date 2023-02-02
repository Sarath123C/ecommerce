from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
app_name='app'
from app import views

urlpatterns = [

    path('',views.allproducts,name='allproducts'),
    path('<slug:c_slug>/',views.allproducts,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='products_Detail'),
]