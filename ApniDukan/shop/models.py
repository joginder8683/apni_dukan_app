from django.db import models

class DiscountCode(models.Model):
    with_product=models.IntegerField()
    get_product=models.IntegerField()
    description=models.CharField(max_length=200)

    def __str__(self):
        return str(self.with_product)+"+"+str(self.get_product)

    class Meta:
        db_table = "discount_code"


class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    discount=models.ForeignKey(DiscountCode, on_delete=False,null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"


class Cart(models.Model):
    status=models.BooleanField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = "cart"


class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=False)
    quantity=models.IntegerField()
    cartId=models.ForeignKey(Cart, on_delete=False)

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "cart_item"


# class Order(models.Model):
#     totalprice=models.IntegerField(default=0)
#     discountprice = models.IntegerField(default=0)
#     totaldiscount = models.IntegerField(default=0)
#     status = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.pk)
#
#     class Meta:
#         db_table = "order"
#
#
# class OrderItem(models.Model):
#     product=models.ForeignKey(Product, on_delete=False)
#     quantity=models.IntegerField(default=1)
#     # date = models.DateTimeField(blank=True)
#     orderid=models.ForeignKey(Order,on_delete=False)
#     def __str__(self):
#         return self.product
#
#     class Meta:
#         db_table = "order_item"
#
