from rest_framework import serializers
from django.contrib.auth.models import User

class UserSeralizer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      "id", "username", "email"
    ]

class RegisterSeralizer(serializers.ModelSerializer):
  password = serializers.CharField(
    write_only=True
  )
  class Meta:
    model = User
    fields = [
      "password", "username", "email"
    ]
  def create(self, validated_data):
    user = User.objects.create_user(
      password=validated_data["password"],
      email=validated_data['email'],
      username=validated_data['username']

    )
    return user