from django.urls import path

from .views import*

urlpatterns=[
    path('documents/',documents,name='documents'),
    path('login/',login,name='login'),
    path('',applications,name='applications'),
    path('application/',application,name='application'),
    path('create_application/',create_application,name='create_application'),
    path('cemetery/', cemetery,name='cemetery'),
    path('iin/', iin, name="iin")
]