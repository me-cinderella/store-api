from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ManyToManyField(Category)
    created_by = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Coupon(models.Model):
    code = models.CharField(max_length=50)
    amount = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Cart(models.Model):
    user = models.ForeignKey(User)
    items = models.ManyToManyField(Product)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Address(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateFielauto_now=Trued()


class ShippingState(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Shipping(models.Model):
    method = models.CharField(
        choices=(
            DEBIT = 'DB', _('Debito')
            CREDIT = 'CR', _('Credito')
            WEBPAY = 'WP', _('Web Pay')
            TRANSFER = 'TR', _('Transferencia bancaria')
            PAYPAL = 'PP', _('Paypal')
        )
    )
    address = models.ForeignKey(Address)
    price = models.IntegerField()
    state = models.ForeignKey(ShippingState)


class CreditCard(models.Model):
    cc = models.CharField(max_length=50)
    cc_num = models.CharField(max_length=50)
    holder_name = models.CharField(max_length=50)
    expire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class PaymentState(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Payment(models.Model):
    creditCard = models.ForeignKey(CreditCard)
    amount = models.IntegerField()
    state = models.ForeignKey(PaymentState)
    created_date = models.DateField(auto_now_add=True)


class OrderState(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


class Order(models.Model):
    user = models.ForeignKey(User)
    cart = models.ManyToManyField(Cart)
    shippin = models.ManyToManyField(Shipping)
    coupon = models.ForeignKey(Coupon)
    state = models.ForeignKey(OrderState)
    total_amount = models.IntegerField()
    trasaction_date = models.DateField()


class ProductReview(models.Model):
    reviwer = models.ForeignKey(User)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order)
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    rating = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)


    