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

    def get_queryset(self):
        ps = self.request.query_params.get('ps')

        queryset = self.queryset
        if ps:
            return queryset.filter(police_station=int(ps))
        return queryset

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
    queryset = models.FIRStatus.objects.all().filter(is_active__exact=True)

    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [AllowAny],
                                    'update': [AllowAny]}

    def get_queryset(self):
        ps = self.request.query_params.get('ps')

        queryset = self.queryset
        if ps:
            return queryset.filter(fir__police_station=int(ps))
        return queryset

    # authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class FIRStatusAllViewset(viewsets.ModelViewSet):
    """Manage FIR Status in the database"""

    serializer_class = serializers.FIRStatusSerializer
    queryset = models.FIRStatus.objects.all()

    permission_classes_by_action = {'list': [AllowAny], }

    def get_queryset(self):
        ps = self.request.query_params.get('ps')
        fir = self.request.query_params.get('fir')

        queryset = self.queryset
        if ps:
            queryset.filter(fir__police_station=int(ps))
        if fir:
            return queryset.filter(fir=int(fir))
        return queryset

    # authentication_classes = (TokenAuthentication, )

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
