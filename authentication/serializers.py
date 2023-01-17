from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

        return user