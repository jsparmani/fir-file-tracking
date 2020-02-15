from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from . import models


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""

    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""

        print(attrs.get('email'), attrs.get('password'))

        email = attrs.get('email'),
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email[0],
            password=password
        )

        if not user:
            msg = 'Unable to authenticate with provided credentials'

            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs
