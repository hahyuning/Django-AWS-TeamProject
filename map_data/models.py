from django.db import models

# Create your models here.
class Map_data(models.Model):
    theme = models.CharField(max_length=100,primary_key=True)
    jong_no_gu = models.CharField(max_length=100)
    jung_gu = models.CharField(max_length=100)
    yong_san_gu = models.CharField(max_length=100)
    seong_dong_gu = models.CharField(max_length=100)
    gwang_jin_gu = models.CharField(max_length=100)
    dong_dae_mun_gu = models.CharField(max_length=100)
    jung_lang_gu = models.CharField(max_length=100)
    seong_bug_gu = models.CharField(max_length=100)
    gang_bug_gu = models.CharField(max_length=100)
    do_bong_gu = models.CharField(max_length=100)
    no_won_gu = models.CharField(max_length=100)
    eun_pyeong_gu = models.CharField(max_length=100)
    seo_dae_mun_gu = models.CharField(max_length=100)
    ma_po_gu = models.CharField(max_length=100)
    yang_cheon_gu = models.CharField(max_length=100)
    gang_seo_gu = models.CharField(max_length=100)
    gu_lo_gu = models.CharField(max_length=100)
    geum_cheon_gu = models.CharField(max_length=100)
    yeong_deung_po_gu = models.CharField(max_length=100)
    dong_jag_gu = models.CharField(max_length=100)
    gwan_ag_gu = models.CharField(max_length=100)
    seo_cho_gu = models.CharField(max_length=100)
    gang_nam_gu = models.CharField(max_length=100)
    song_pa_gu = models.CharField(max_length=100)
    gang_dong_gu = models.CharField(max_length=100)
    seoul = models.CharField(max_length=100)

class Map_info(models.Model):
    loc = models.CharField(max_length=50,primary_key=True)
    kor_loc = models.CharField(max_length=50)
    longi = models.DecimalField(max_digits=30 , decimal_places=15 )
    lati = models.DecimalField(max_digits=30 , decimal_places=15)

