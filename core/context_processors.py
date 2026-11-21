from django.conf import settings


def product_variant(request):
    return {
        'ENABLE_REPORTS': settings.ENABLE_REPORTS,
        'ENABLE_NOTIFICATIONS': settings.ENABLE_NOTIFICATIONS,
        'PRODUCT_NAME': settings.PRODUCT_NAME,
        'ACTIVE_VARIANT': settings.ACTIVE_VARIANT_NAME,
    }
