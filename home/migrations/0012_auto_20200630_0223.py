# Generated by Django 3.0.4 on 2020-06-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_datatestingcbmerah_datatestingcbrawit'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatestingcbmerah',
            name='prediksi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Prediksi'),
        ),
        migrations.AddField(
            model_name='datatestingcbrawit',
            name='prediksi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Prediksi'),
        ),
    ]
