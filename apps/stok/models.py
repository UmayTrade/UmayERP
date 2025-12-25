from django.db import models

class Urun(models.Model):
    urun_adi = models.CharField(max_length=200)
    stok_miktari = models.IntegerField(default=0)
    alis_fiyati = models.DecimalField(max_digits=12, decimal_places=2)
    satis_fiyati = models.DecimalField(max_digits=12, decimal_places=2)
    kritik_esik = models.IntegerField(default=5)

    def __str__(self):
        return self.urun_adi

    def stok_durumu(self):
        if self.stok_miktari <= self.kritik_esik:
            return "KRİTİK: Eyüp'ü ara!"
        return "Normal"