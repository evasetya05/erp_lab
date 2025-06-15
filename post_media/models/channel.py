from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


from datetime import date
from django.utils.timezone import now
from post_media.models.for_market import Market


class Channel(models.Model):

     # Foreign Key ke model Market  
    
    AKUN_CHOICES = [
        ('personal', 'Personal'),
        ('sdmportabel', 'sdmportabel'),
        ('datatech', 'DataTech'),
    ]

    akun = models.CharField(
        max_length=20,
        choices=AKUN_CHOICES,
        verbose_name="akun"
    )

    for_market = models.ForeignKey(Market, on_delete=models.CASCADE)
    CHANNEL_CHOICES = [
        ('blog', 'Blog'),
        ('ig', 'Instagram'),
        ('thread', 'Thread'),
        ('linkedin', 'linkedin'),
    ]

    channel = models.CharField(
        max_length=20,
        choices=CHANNEL_CHOICES,
        verbose_name="channel"
    )

    FUNNEL_STAGE_CHOICES = [
        ('awareness', 'Awareness'),
        ('interest', 'Interest'),
        ('desire', 'Desire'),
        ('action', 'Action'),
        ('retention', 'Retention'),
    ]

    funnel_stage = models.CharField(
        max_length=20,
        choices=FUNNEL_STAGE_CHOICES,
        verbose_name="Funnel Stage"
    )

    kategori_biaya = models.CharField(max_length=100, verbose_name="Kategori Biaya")
    tanggal_posting = models.DateTimeField(default=now)
    rencana_tanggal_posting = models.DateField(null=True, blank=True)  # kalau bisa null, supaya fleksibel
    jenis_konten = models.CharField(max_length=100, verbose_name="Jenis Konten")
    judul = models.CharField(max_length=100, verbose_name="judul")
    isi_konten = RichTextUploadingField(verbose_name="isi konten", blank=True, default="")


    
    # As At 6-12 Jam
    as_at_6_12_jam_impressions = models.PositiveIntegerField(default=0, verbose_name="Impressions (6-12 Jam)")
    as_at_6_12_jam_member_reached = models.PositiveIntegerField(default=0, verbose_name="Member Reached (6-12 Jam)")
    as_at_6_12_jam_view = models.PositiveIntegerField(default=0, verbose_name="View (6-12 Jam)")
    as_at_6_12_jam_email_send = models.PositiveIntegerField(default=0, verbose_name="Email Send (6-12 Jam)")
    as_at_6_12_jam_email_open_rate = models.FloatField(default=0.0, verbose_name="Email Open Rate (6-12 Jam)")
    as_at_6_12_jam_reactions_like = models.PositiveIntegerField(default=0, verbose_name="Reactions / Like (6-12 Jam)")
    as_at_6_12_jam_comment = models.PositiveIntegerField(default=0, verbose_name="Comment (6-12 Jam)")
    as_at_6_12_jam_repost_share = models.PositiveIntegerField(default=0, verbose_name="Repost / Share (6-12 Jam)")
    
    # As At 24 Jam
    as_at_24_jam_impressions = models.PositiveIntegerField(default=0, verbose_name="Impressions (24 Jam)")
    as_at_24_jam_member_reached = models.PositiveIntegerField(default=0, verbose_name="Member Reached (24 Jam)")
    as_at_24_jam_view = models.PositiveIntegerField(default=0, verbose_name="View (24 Jam)")
    as_at_24_jam_email_send = models.PositiveIntegerField(default=0, verbose_name="Email Send (24 Jam)")
    as_at_24_jam_email_open_rate = models.FloatField(default=0.0, verbose_name="Email Open Rate (24 Jam)")
    as_at_24_jam_reactions_like = models.PositiveIntegerField(default=0, verbose_name="Reactions / Like (24 Jam)")
    as_at_24_jam_comment = models.PositiveIntegerField(default=0, verbose_name="Comment (24 Jam)")
    as_at_24_jam_repost_share = models.PositiveIntegerField(default=0, verbose_name="Repost / Share (24 Jam)")
    
    # As At 3 Hari (72 Jam)
    as_at_3hari_impressions = models.PositiveIntegerField(default=0, verbose_name="Impressions (3 Hari)")
    as_at_3hari_member_reached = models.PositiveIntegerField(default=0, verbose_name="Member Reached (3 Hari)")
    as_at_3hari_view = models.PositiveIntegerField(default=0, verbose_name="View (3 Hari)")
    as_at_3hari_email_send = models.PositiveIntegerField(default=0, verbose_name="Email Send (3 Hari)")
    as_at_3hari_email_open_rate = models.FloatField(default=0.0, verbose_name="Email Open Rate (3 Hari)")
    as_at_3hari_reactions_like = models.PositiveIntegerField(default=0, verbose_name="Reactions / Like (3 Hari)")
    as_at_3hari_comment = models.PositiveIntegerField(default=0, verbose_name="Comment (3 Hari)")
    as_at_3hari_repost_share = models.PositiveIntegerField(default=0, verbose_name="Repost / Share (3 Hari)")
    
    # As At 1 Minggu (168 Jam)
    as_at_1minggu_impressions = models.PositiveIntegerField(default=0, verbose_name="Impressions (1 Minggu)")
    as_at_1minggu_member_reached = models.PositiveIntegerField(default=0, verbose_name="Member Reached (1 Minggu)")
    as_at_1minggu_view = models.PositiveIntegerField(default=0, verbose_name="View (1 Minggu)")
    as_at_1minggu_email_send = models.PositiveIntegerField(default=0, verbose_name="Email Send (1 Minggu)")
    as_at_1minggu_email_open_rate = models.FloatField(default=0.0, verbose_name="Email Open Rate (1 Minggu)")
    as_at_1minggu_reactions_like = models.PositiveIntegerField(default=0, verbose_name="Reactions / Like (1 Minggu)")
    as_at_1minggu_comment = models.PositiveIntegerField(default=0, verbose_name="Comment (1 Minggu)")
    as_at_1minggu_repost_share = models.PositiveIntegerField(default=0, verbose_name="Repost / Share (1 Minggu)")
    
    # Durasi
    lama_jam = models.PositiveIntegerField(default=0, verbose_name="Lama (Jam)")
    follower = models.PositiveIntegerField(default=0, verbose_name="Follower")
    discovery = models.PositiveIntegerField(default=0, verbose_name="Discovery")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.judul} - {self.rencana_tanggal_posting}"
