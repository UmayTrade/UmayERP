from django.db import models

class CariKart(models.Model):
    isim = models.CharField(max_length=255) # Örn: Ayşe Kocatepe
    telefon = models.CharField(max_length=20, blank=True)
    borc_bakiyesi = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.isim

class Satis(models.Model):
    cari = models.ForeignKey(CariKart, on_delete=models.CASCADE)
    toplam_tutar = models.DecimalField(max_digits=15, decimal_places=2)
    alinan_nakit = models.DecimalField(max_digits=15, decimal_places=2)
    tarih = models.DateTimeField(auto_now_add=True)

    @property
    def kalan_borc(self):
        return self.toplam_tutar - self.alinan_nakit