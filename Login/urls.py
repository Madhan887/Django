from django.urls import path
from Login import views
urlpatterns=[
    path('Login',views.Login),
    path('create',views.Create1)
]