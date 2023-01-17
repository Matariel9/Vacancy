from django.contrib import admin
from django.urls import path
from authentication import views
from rest_framework.authtoken import views as aViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('login/', aViews.obtain_auth_token),
    path('logout/', views.Logout.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view())
]
