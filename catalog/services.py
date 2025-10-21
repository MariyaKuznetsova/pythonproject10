from .models import Product


def get_products_by_category(category):
    return Product.object.filter(category=category)
