from django.contrib import admin
from models.ig import IG

@admin.register(IG)
class IGAdmin(admin.ModelAdmin):
    list_display = (
        'judul', 'funnel_stage', 'for_who', 'kategori_biaya', 'rencana_tanggal_posting',
        'jenis_konten', 'lama_jam', 'follower', 'discovery', 'created_at'
    )
    list_display_links = ('judul',)
    list_filter = ('funnel_stage', 'kategori_biaya', 'jenis_konten', 'rencana_tanggal_posting',)
    search_fields = ('judul', 'tujuan', 'metode_pengukuran')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Informasi Dasar', {
            'fields': (
                'funnel_stage', 'for_who', 'kategori_biaya', 'rencana_tanggal_posting', 'tanggal_posting', 'jenis_konten',
                'tujuan', 'judul', 'metode_pengukuran'
            )
        }),
        ('Performance 6-12 Jam', {
            'fields': (
                'as_at_6_12_jam_impressions', 'as_at_6_12_jam_member_reached', 'as_at_6_12_jam_view',
                'as_at_6_12_jam_email_send', 'as_at_6_12_jam_email_open_rate',
                'as_at_6_12_jam_reactions_like', 'as_at_6_12_jam_comment', 'as_at_6_12_jam_repost_share',
            )
        }),
        ('Performance 24 Jam', {
            'fields': (
                'as_at_24_jam_impressions', 'as_at_24_jam_member_reached', 'as_at_24_jam_view',
                'as_at_24_jam_email_send', 'as_at_24_jam_email_open_rate',
                'as_at_24_jam_reactions_like', 'as_at_24_jam_comment', 'as_at_24_jam_repost_share',
            )
        }),
        ('Performance 3 Hari', {
            'fields': (
                'as_at_3hari_impressions', 'as_at_3hari_member_reached', 'as_at_3hari_view',
                'as_at_3hari_email_send', 'as_at_3hari_email_open_rate',
                'as_at_3hari_reactions_like', 'as_at_3hari_comment', 'as_at_3hari_repost_share',
            )
        }),
        ('Performance 1 Minggu', {
            'fields': (
                'as_at_1minggu_impressions', 'as_at_1minggu_member_reached', 'as_at_1minggu_view',
                'as_at_1minggu_email_send', 'as_at_1minggu_email_open_rate',
                'as_at_1minggu_reactions_like', 'as_at_1minggu_comment', 'as_at_1minggu_repost_share',
            )
        }),
        ('Data Lainnya', {
            'fields': ('lama_jam', 'follower', 'discovery')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
