from django.urls import path

from . import views

# must be called urlpatterns as django looks for it
urlpatterns = [
    path('meetups/', views.index) # our-domain.com/meetups (we put slash so even if user adds slash at end of url it'll work)
]