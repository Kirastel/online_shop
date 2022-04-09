from django.db.models.signals import post_save
from django.db import models
from products.models import Product


class Order(models.Model):
    status_choice = [
        ('no', 'in processed'),
        ('yes', 'order completed')
    ]

    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    update_time = models.DateTimeField(
        auto_now_add=False,
        auto_now=True
    )
    total_price = models.FloatField(
        default=0.0,
        null=True
    )
    first_name = models.CharField(
        max_length=20
    )
    last_name = models.CharField(
        max_length=20
    )
    company = models.CharField(
        blank=True,
        max_length=20
    )
    country = models.CharField(
        max_length=20
    )
    adress = models.CharField(
        max_length=20
    )
    zip = models.PositiveIntegerField(
        blank=True
    )
    city = models.CharField(
        max_length=40
    )
    province = models.CharField(
        max_length=40
    )
    phone = models.CharField(
        max_length=15
    )
    email = models.EmailField()
    comment = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    status = models.CharField(
        choices=status_choice,
        default='no',
        max_length=20
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        null=True,
        on_delete=models.SET_NULL
    )
    product_order = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.SET_NULL
    )
    number = models.PositiveIntegerField(
        default=1
    )
    price = models.DecimalField(
        default=0.0,
        null=True,
        max_digits=10,
        decimal_places=2
    )
    total_price = models.DecimalField(
        default=0.0,
        null=True,
        max_digits=7,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = 'Products on order'

    def __str__(self):
        return f'Заказ № {self.id}: {self.order}'


    def save(self, *args, **kwargs):
        price_per_item = self.product_order.price
        self.price_per_item = price_per_item
        self.total_price = self.number * price_per_item
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class Contact(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False
    )
    first_name = models.CharField(
        max_length=200
    )
    last_name = models.CharField(
        max_length=200
    )
    subject = models.CharField(
        max_length=200
    )
    text = models.TextField(
        max_length=800
    )

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f'{self.id} - {self.date}, {self.first_name} {self.last_name}'
