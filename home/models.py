from django.db import models


class DataCbRawit(models.Model):
    bulan = models.CharField("Bulan", max_length=50, blank=True, null=True)
    tahun = models.CharField("Tahun", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.bulan


class DataCbMerah(models.Model):
    bulan = models.CharField("Bulan", max_length=50, blank=True, null=True)
    tahun = models.CharField("Tahun", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.bulan


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
