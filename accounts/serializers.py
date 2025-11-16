from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
    
    def validate_password(self, value):
        """Validate password meets complexity requirements."""
        if len(value) < 8:
            raise serializers.ValidationError(
                "A senha deve ter no mínimo 8 caracteres."
            )
        
        if not re.search(r'\d', value):
            raise serializers.ValidationError(
                "A senha deve conter pelo menos um número."
            )
        
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "A senha deve conter pelo menos uma letra maiúscula."
            )
        
        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError(
                "A senha deve conter pelo menos uma letra minúscula."
            )
        
        if re.search(r'\s', value):
            raise serializers.ValidationError(
                "A senha não pode conter espaços em branco."
            )
        
        return value
    
    def validate(self, data):
        """Validate password confirmation."""
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError(
                {'password': 'As senhas não coincidem.'}
            )
        return data
    
    def validate_username(self, value):
        """Check if username already exists."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Este usuário já existe.')
        return value
    
    def validate_email(self, value):
        """Check if email already exists and normalize to lowercase."""
        value = value.lower()
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email já está registrado.')
        return value
    
    def create(self, validated_data):
        """Create user with hashed password."""
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    """Serializer for user login with custom token claims."""
    
    def get_token(self, user):
        """Customize token with user data."""
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class AuthResponseSerializer(serializers.Serializer):
    """Standard response serializer for authentication endpoints."""
    
    user = UserSerializer()
    access = serializers.CharField()
    refresh = serializers.CharField()
