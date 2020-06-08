from django.db import models


class DataCbRawit(models.Model):
    no = models.CharField("No", max_length=50, blank=False, null=True)
    bulan = models.CharField("Bulan", max_length=50, blank=False, null=True)
    tahun = models.CharField("Tahun", max_length=50, blank=False, null=True)
    harga = models.CharField("Harga", max_length=50, blank=False, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=False, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=False, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=False, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataCbMerah(models.Model):
    no = models.CharField("No", max_length=50, blank=False, null=True)
    bulan = models.CharField("Bulan", max_length=50, blank=False, null=True)
    tahun = models.CharField("Tahun", max_length=50, blank=False, null=True)
    harga = models.CharField("Harga", max_length=50, blank=False, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=False, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=False, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=False, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataMinMaxCbRawit(models.Model):
    type = models.CharField("Type", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.type


class DataMinMaxCbMerah(models.Model):
    type = models.CharField("Type", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.type


class DataNewMinMaxCbRawit(models.Model):
    newmin = models.CharField("New Min", max_length=50, blank=True, null=True)
    newmax = models.CharField("New Max", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.newmin


class DataNewMinMaxCbMerah(models.Model):
    newmin = models.CharField("New Min", max_length=50, blank=True, null=True)
    newmax = models.CharField("New Max", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.newmin


class DataNormalisasiCbRawit(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataNormalisasiCbMerah(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataWeightCbRawit(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataWeightCbMerah(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataBiasCbRawit(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    bias = models.CharField("Bias", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataBiasCbMerah(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    bias = models.CharField("Bias", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataOutputWeightCbRawit(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    weight = models.CharField("Weight", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataOutputWeightCbMerah(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    weight = models.CharField("Weight", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataMseCbRawit(models.Model):
    mse = models.CharField("MSE", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.mse


class DataMseCbMerah(models.Model):
    mse = models.CharField("MSE", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.mse


class DataDenormalisasiCbRawit(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    denormalisasi = models.CharField("Denormalisasi", max_length=50, blank=True, null=True)
    hasil = models.CharField("Hasil", max_length=50, blank=True, null=True)
    bulan = models.CharField("Bulan", max_length=50, blank=True, null=True)
    tahun = models.CharField("Tahun", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no


class DataDenormalisasiCbMerah(models.Model):
    no = models.CharField("No", max_length=50, blank=True, null=True)
    denormalisasi = models.CharField("Denormalisasi", max_length=50, blank=True, null=True)
    hasil = models.CharField("Hasil", max_length=50, blank=True, null=True)
    bulan = models.CharField("Bulan", max_length=50, blank=True, null=True)
    tahun = models.CharField("Tahun", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.no
