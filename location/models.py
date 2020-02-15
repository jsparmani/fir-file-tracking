from django.db import models


class District(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class SubDivision(models.Model):

    district = models.ForeignKey(
        District, related_name='districts', on_delete=models.CASCADE, blank=False)

    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}--{self.district.name}'


class PoliceStation(models.Model):

    sub_division = models.ForeignKey(
        SubDivision, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name}--{self.sub_division.name}'
