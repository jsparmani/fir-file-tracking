from django.db import models


class FIR(models.Model):

    ACCUSED_STATUS_CHOICES = [
        ('arrested', 'Arrested'),
        ('not_arrested', 'Not Arrested'),
        ('po', 'PO'),
    ]

    fir_no = models.CharField(max_length=50, blank=False)
    police_station = models.ForeignKey(
        'location.PoliceStation', blank=False, related_name='firs', on_delete=models.CASCADE)
    investigation_officer = models.CharField(max_length=255, blank=False)
    accused_name = models.CharField(max_length=255, blank=False)
    accused_status = models.CharField(max_length=50,
                                      choices=ACCUSED_STATUS_CHOICES, blank=False)
    challan_to_court_limitation_period = models.PositiveSmallIntegerField(
        blank=False)

    def __str__(self):
        return self.fir_no

    class Meta:
        verbose_name_plural = 'FIRs'
        unique_together = ['fir_no', 'police_station']


class FIRStatus(models.Model):

    CURRENT_STATUS_CHOICES = [
        ('under_investigation', 'Under Investigation'),
        ('challan_filed', 'Challan Filed'),
        ('untraced', 'Untraced'),
        ('cancelled', 'Cancelled'),
    ]

    LOCATION_CHOICES = [
        ('ps', 'Police Station'),
        ('dsp', 'DSP Office'),
        ('sp', 'SP Office'),
        ('ssp', 'SSP Office'),
        ('court', 'Court'),
    ]

    fir = models.ForeignKey(
        'tracking.FIR', related_name='firs', on_delete=models.CASCADE, blank=False)
    current_status = models.CharField(
        max_length=50, choices=CURRENT_STATUS_CHOICES, blank=False)

    location = models.CharField(
        max_length=255, choices=LOCATION_CHOICES)

    date_of_action = models.DateField(blank=False)

    is_active = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return f'{self.fir.fir_no}--{self.current_status}'

    class Meta:
        verbose_name_plural = 'FIR Statuses'
