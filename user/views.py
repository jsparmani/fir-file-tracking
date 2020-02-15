from django.shortcuts import render
from . import serializers
from rest_framework.settings import api_settings
from rest_framework import generics, mixins, viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""

    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


@api_view(['POST'])
def check_user_status(request):

    try:
        if request.method == 'POST':

            user = Token.objects.get(key=request.data['token']).user
            if (user.is_superuser):
                return Response({"type": "superuser", "id": user.id})
            else:
                if len(user.ps.all()) != 0:
                    ps = user.ps.all()[0]
                    return Response({"type": "ps", "id": user.id, "ps": ps.id})
                elif len(user.districts.all()) != 0:
                    district = user.districts.all()[0]
                    return Response({"type": "district", "id": user.id, "district": district.id})

        else:
            return JsonResponse(request.data)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
