from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, status, mixins, generics


class FIRViewset(viewsets.ModelViewSet):
    """Manage FIRs in the database"""

    serializer_class = serializers.FIRSerializer
    queryset = models.FIR.objects.all()

    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [AllowAny]}

    # authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class FIRStatusViewset(viewsets.ModelViewSet):
    """Manage FIR Status in the database"""

    serializer_class = serializers.FIRStatusSerializer
    queryset = models.FIRStatus.objects.all()

    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [AllowAny],
                                    'update': [AllowAny]}

    # authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
