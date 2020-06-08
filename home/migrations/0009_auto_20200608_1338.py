# Generated by Django 3.0.4 on 2020-06-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200605_0457'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacbmerah',
            name='no',
            field=models.CharField(max_length=50, null=True, verbose_name='No'),
        ),
        migrations.AddField(
            model_name='datacbrawit',
            name='no',
            field=models.CharField(max_length=50, null=True, verbose_name='No'),
        ),
        migrations.AlterField(
            model_name='datacbmerah',
            name='bulan',
            field=models.CharField(max_length=50, null=True, verbose_name='Bulan'),
        ),
        migrations.AlterField(
            model_name='datacbmerah',
            name='harga',
            field=models.CharField(max_length=50, null=True, verbose_name='Harga'),
        ),
        migrations.AlterField(
            model_name='datacbmerah',
            name='ketersediaan',
            field=models.CharField(max_length=50, null=True, verbose_name='Ketersediaan (TON)'),
        ),
        migrations.AlterField(
            model_name='datacbmerah',
            name='permintaan',
            field=models.CharField(max_length=50, null=True, verbose_name='Permintaan (TON)'),
        ),
        migrations.AlterField(
            model_name='datacbmerah',
            name='produksi',
            field=models.CharField(max_length=50, null=True, verbose_name='Produksi (KW)'),
        ),
        migrations.AlterField(
            model_name='datacbmerah',
            name='tahun',
            field=models.CharField(max_length=50, null=True, verbose_name='Tahun'),
        ),
        migrations.AlterField(
            model_name='datacbrawit',
            name='bulan',
            field=models.CharField(max_length=50, null=True, verbose_name='Bulan'),
        ),
        migrations.AlterField(
            model_name='datacbrawit',
            name='harga',
            field=models.CharField(max_length=50, null=True, verbose_name='Harga'),
        ),
        migrations.AlterField(
            model_name='datacbrawit',
            name='ketersediaan',
            field=models.CharField(max_length=50, null=True, verbose_name='Ketersediaan (TON)'),
        ),
        migrations.AlterField(
            model_name='datacbrawit',
            name='permintaan',
            field=models.CharField(max_length=50, null=True, verbose_name='Permintaan (TON)'),
        ),
        migrations.AlterField(
            model_name='datacbrawit',
            name='produksi',
            field=models.CharField(max_length=50, null=True, verbose_name='Produksi (KW)'),
        ),
        migrations.AlterField(
            model_name='datacbrawit',
            name='tahun',
            field=models.CharField(max_length=50, null=True, verbose_name='Tahun'),
        ),
    ]
