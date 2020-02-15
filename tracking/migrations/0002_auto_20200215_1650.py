# Generated by Django 2.2.5 on 2020-02-15 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fir',
            name='police_station',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='firs', to='location.PoliceStation'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='fir',
            unique_together={('fir_no', 'police_station')},
        ),
    ]