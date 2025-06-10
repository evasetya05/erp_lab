from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


from django_ledger.settings import DJANGO_LEDGER_GRAPHQL_SUPPORT_ENABLED

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_ledger.urls', namespace='django_ledger')),
     path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# GraphQl API Support...
try:
    if DJANGO_LEDGER_GRAPHQL_SUPPORT_ENABLED:
        from django_ledger.contrib.django_ledger_graphene.api import schema
        from django_ledger.contrib.django_ledger_graphene.views import DjangoLedgerOAuth2GraphQLView

        urlpatterns += [
            path('api/v1/graphql/', DjangoLedgerOAuth2GraphQLView.as_view(graphiql=settings.DEBUG, schema=schema)),
            path('api/v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
        ]

except ImportError:
    pass
