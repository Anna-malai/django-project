from django.urls import path

from . import views

urlpatters=[
    path('',views.HomePageView.as_view(),name='register')
]