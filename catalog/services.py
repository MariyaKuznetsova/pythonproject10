from django.core.cache import cache

from config.settings import CACHES
from .models import Product

class ProductService:

    @staticmethod
    def get_products_from_cache():
        if not CACHES:
            return Product.objects.all()
        key = "products_list"
        products_cache = cache.get(key)
        if products_cache is not None:
            return products_cache
        products_cache = Product.objects.all()
        cache.set(key, products_cache)
        return products_cache


