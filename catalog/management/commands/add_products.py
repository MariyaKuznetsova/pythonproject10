from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add catalog to the database'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(name='Бобы', description="Пищевые")

        products = [
            {'name': 'Горох', 'description': 'Содержит большое количество биологически активных соединений.', 'category': category, 'price': 100},
            {'name': 'Фасоль', 'description': 'Аминокислота аргинин необходима для азотистого обмена, снижает в крови уровень глюкозы.', 'category': category, 'price': 80},
            {'name': 'Чечевица', 'description': 'Чечевица богата микроэлементами/', 'category': category, 'price': 30},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Product already exists: {product.name}'))



