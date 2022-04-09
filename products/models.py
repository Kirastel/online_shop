from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    type = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    generation = models.CharField(
        max_length=10,
        default=None
    )
    version = models.CharField(
        max_length=10,
        blank=True
    )
    storage = models.CharField(
        max_length=10,
        blank=True
    )
    color = models.CharField(
        max_length=10,
        blank=True
    )
    availability = models.CharField(
        choices=[('In', 'In stock'), ('Out', 'Out stock')],
        max_length=10,
        default='In stock'
    )
    short_description = models.CharField(
        blank=True,
        null=True,
        default=None,
        max_length=300
    )
    description = models.CharField(
        blank=True,
        null=True,
        default=None,
        max_length=2000
    )
    price = models.DecimalField(
        default=0.0,
        null=True,
        max_digits=7,
        decimal_places=2
    )
    old_price = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        help_text='Ввод старой цены для отображения скидки на товар'
    )
    append_date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        null=True
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.type} {self.generation} {self.color} {self.storage} '

    def availability_color(self):
        if self.availability == 'In stock':
            return '<font color="green">In stock</font>'
        elif self.availability == 'Out stock':
            return '<font color="red">Out stock</font>'


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        null=True,
        on_delete=models.CASCADE,
        related_name='IMAGE'
    )
    image = models.ImageField(
        upload_to='photos/',
        default='default.jpg'
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return f'Фотографии {self.product} '



