from django.contrib import admin
from .models import CariKart, Satis

@admin.register(CariKart)
class CariAdmin(admin.ModelAdmin):
    list_display = ('isim', 'borc_bakiyesi')
    search_fields = ('isim',)

@admin.register(Satis)
class SatisAdmin(admin.ModelAdmin):
    list_display = ('cari', 'toplam_tutar', 'tarih')
    list_filter = ('tarih',)