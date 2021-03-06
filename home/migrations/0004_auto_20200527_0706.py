# Generated by Django 3.0.4 on 2020-05-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200327_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBiasCbMerah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=50, null=True, verbose_name='No')),
                ('bias', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bias')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='DataBiasCbRawit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=50, null=True, verbose_name='No')),
                ('bias', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bias')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='DataNormalisasiCbMerah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=50, null=True, verbose_name='No')),
                ('harga', models.CharField(blank=True, max_length=50, null=True, verbose_name='Harga')),
                ('produksi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Produksi (KW)')),
                ('ketersediaan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ketersediaan (TON)')),
                ('permintaan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Permintaan (TON)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='DataNormalisasiCbRawit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=50, null=True, verbose_name='No')),
                ('harga', models.CharField(blank=True, max_length=50, null=True, verbose_name='Harga')),
                ('produksi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Produksi (KW)')),
                ('ketersediaan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ketersediaan (TON)')),
                ('permintaan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Permintaan (TON)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='DataWeightCbMerah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=50, null=True, verbose_name='No')),
                ('harga', models.CharField(blank=True, max_length=50, null=True, verbose_name='Harga')),
                ('produksi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Produksi (KW)')),
                ('ketersediaan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ketersediaan (TON)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='DataWeightCbRawit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=50, null=True, verbose_name='No')),
                ('harga', models.CharField(blank=True, max_length=50, null=True, verbose_name='Harga')),
                ('produksi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Produksi (KW)')),
                ('ketersediaan', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ketersediaan (TON)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.RenameModel(
            old_name='Data',
            new_name='DataCbMerah',
        ),
        migrations.RenameModel(
            old_name='cbMerah',
            new_name='DataCbRawit',
        ),
    ]
