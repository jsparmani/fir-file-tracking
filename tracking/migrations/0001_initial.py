# Generated by Django 2.2.5 on 2020-02-15 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FIR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fir_no', models.CharField(max_length=50)),
                ('investigation_officer', models.CharField(max_length=255)),
                ('accused_name', models.CharField(max_length=255)),
                ('accused_status', models.CharField(choices=[('arrested', 'Arrested'), ('not_arrested', 'Not Arrested'), ('po', 'PO')], max_length=50)),
                ('challan_to_court_limitation_period', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'FIRs',
            },
        ),
        migrations.CreateModel(
            name='FIRStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('under_investigation', 'Under Investigation'), ('challan_filed', 'Challan Filed'), ('untraced', 'Untraced'), ('cancelled', 'Cancelled')], max_length=50)),
                ('location', models.CharField(choices=[('ps', 'Police Station'), ('dsp', 'DSP Office'), ('sp', 'SP Office'), ('ssp', 'SSP Office'), ('court', 'Court')], max_length=255)),
                ('date_of_action', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('fir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firs', to='tracking.FIR')),
            ],
            options={
                'verbose_name_plural': 'FIR Statuses',
            },
        ),
    ]
