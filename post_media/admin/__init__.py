from django.contrib import admin

from post_media.admin.blog import BlogAdmin
from post_media.admin.ig import IGAdmin
from post_media.admin.linkedin import LinkedInAdmin


from post_media.models import blog, ig, linkedin


admin.site.register(BlogAdmin, IGAdmin, LinkedInAdmin)
