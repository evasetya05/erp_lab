from django.contrib import admin
from post_media.models.channel import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = (
        'judul', 'funnel_stage', 'akun', 'channel',  'for_market', 'tanggal_posting',
        'jenis_konten', 'follower', 'as_at_1minggu_impressions', 'as_at_1minggu_member_reached', 'as_at_1minggu_view',
        'as_at_1minggu_reactions_like', 'as_at_1minggu_comment'
    )
    list_display_links = ('judul',)
    list_filter = ('akun', 'channel')
    search_fields = ['judul']
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Informasi Dasar', {
            'fields': (
                'funnel_stage', 'akun', 'channel', 'for_market', 'kategori_biaya', 'rencana_tanggal_posting', 'tanggal_posting', 'jenis_konten',
                'judul', 'isi_konten'
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
