from django.urls import path
from . import views
from knox import views as knox_views

urlpatterns = [
       path('portal/', views.Portal.as_view()),
       path('register/', views.RegisterView.as_view()),
       path('login/', views.LoginView.as_view()),
       path('logout/', knox_views.LogoutView.as_view(), name="knox_logout"),
]
