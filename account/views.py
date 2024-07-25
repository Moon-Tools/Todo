from django.shortcuts import render
from rest_framework import generics, permissions
from .seralizers import UserSeralizer, RegisterSeralizer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegisterSeralizer

  permission_classes = [permissions.AllowAny]

class UserDetail(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSeralizer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    return self.request.user
  
  



