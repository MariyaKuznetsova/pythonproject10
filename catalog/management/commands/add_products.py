from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(name='Бобы', description="Пищевые")

        products = [
            {'name': 'Горох', 'description': 'Молодой', 'category': category, 'price': 100},
            {'name': 'Фасоль', 'description': 'Молодой', 'category': category, 'price': 80},
            {'name': 'Чечевица', 'description': 'Молодой', 'category': category, 'price': 30},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}'))



