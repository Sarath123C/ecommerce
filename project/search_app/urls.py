from django.urls import path
app_name='search_app'
from . import views

urlpatterns = [

    path('search_app',views.searchresult,name='searchresult'),

]
