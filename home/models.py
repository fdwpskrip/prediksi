from django.db import models


class Data(models.Model):
    bulan = models.CharField("Bulan", max_length=50, blank=True, null=True)
    tahun = models.CharField("Tahun", max_length=50, blank=True, null=True)
    harga = models.CharField("Harga", max_length=50, blank=True, null=True)
    produksi = models.CharField("Produksi (KW)", max_length=50, blank=True, null=True)
    ketersediaan = models.CharField("Ketersediaan (TON)", max_length=50, blank=True, null=True)
    permintaan = models.CharField("Permintaan (TON)", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.bulan