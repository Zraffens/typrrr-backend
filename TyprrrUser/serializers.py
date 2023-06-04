from wsgiref import validate
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import TyprrrUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyprrrUser
        fields = ('id', 'username', 'email', 'created', 'races_completed', 'average_speed', 'races_won', 
                  'best_speed')


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyprrrUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        print(password, make_password(password))
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyprrrUser
        fields = ('id', 'username', 'email', 'created', 'races_completed', 'average_speed', 'races_won', 'best_speed')

