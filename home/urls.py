from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('about/',views.about.as_view(),name='about'),
    path('reservation/',views.reservation.as_view(),name='reservation'),
    path('deals/',views.deals.as_view(),name='deals'),
    path('login/',views.login.as_view(),name='login')
]
