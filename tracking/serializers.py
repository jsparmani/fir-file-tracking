from rest_framework import serializers
from . import models
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from location import models as loc_models


class FIRSerializer(serializers.ModelSerializer):
    """Serialize FIR model"""

    police_station = serializers.PrimaryKeyRelatedField(
        queryset=loc_models.PoliceStation.objects.all()
    )

    class Meta:
        model = models.FIR
        fields = ('id', 'fir_no',
                  'police_station', 'investigation_officer', 'accused_name', 'accused_status', 'challan_to_court_limitation_period')
        read_only_fields = ('id', )


class FIRStatusSerializer(serializers.ModelSerializer):
    """Serialize FIR Status model"""

    fir = serializers.PrimaryKeyRelatedField(
        queryset=models.FIR.objects.all()
    )

    class Meta:
        model = models.FIRStatus
        fields = ('id', 'fir',
                  'current_status', 'location', 'date_of_action', 'is_active')
        read_only_fields = ('id', )

    def create(self, validated_data):

        statuses = models.FIRStatus.objects.all().filter(
            fir__pk__exact=self.data['fir'], is_active__exact=True)
        for status in statuses:
            status.is_active = False
            status.save()
        obj = models.FIRStatus.objects.create(**validated_data)
        return obj
