from django.urls import path
from .views import RegisterView, UserDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
  path("register/", RegisterView.as_view(), name="Register"),
  path("me/", UserDetail.as_view(), name="Me"),
  path("access/", TokenObtainPairView.as_view(), name="Access"),
  path("refresh/", TokenRefreshView.as_view(), name="Refresh")
]