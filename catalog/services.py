from django.core.cache import cache

from config.settings import CACHES
from .models import Product

class ProductService:

    @staticmethod
    def get_products_by_category(category):
        return Product.object.filter(category=category)


