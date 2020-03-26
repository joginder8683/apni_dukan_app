from .models import Product,DiscountCode,CartItem,CartItem,Cart

class Shopping():
    def __init__(self,data):
        self.data=data

    def add_coupon(self):
        try:
            DiscountCode(with_product=self.data['with'],get_product=self.data['get'],description=self.data['desc']).save()
            return {"Status":True,"data":"Discount code added successfully buy {} and get {}".format(self.data['with'],self.data['get'])}
        except Exception as ae:
            return {"Status":False,"msg":ae}

    def add_product(self):
        try:
            if 'coupon' in self.data.keys():
                discount=DiscountCode.objects.get(id=self.data['coupon'])
                product=Product(name=self.data['name'],description=self.data['desc'],price=self.data['price'],discount=discount).save()
            else:
                product = Product(name=self.data['name'], description=self.data['desc'],
                                  price=self.data['price']).save()



            return {"Status":True,"data":self.data['name']+ " added succesfully"}
        except Exception as ae:
            return {"Status":False,"msg":ae}


    def add_product_in_cart(self):
        try:
            if 'cart' in self.data.keys():
                cart=Cart.objects.get(pk=self.data['cart'])
            else:
                cart=Cart.objects.create(status=True)
            
            discountcode=DiscountCode.objects.get(pk=self.data['coupon'])
            
            product=Product.objects.get(pk=self.data['product'])
            product.discount=discountcode
            product.save()
            product=Product.objects.get(pk=self.data['product'])
            
            CartItem(product=product,quantity=self.data['quantity'],cartId=cart).save()
            return {"Status":True,"data":"products added to Cart : "+str(cart.id)}
        except Exception as ae:
            return {"Status":True,"msg":ae}


    def create_order(self):
        try:
            cart_items=CartItem.objects.filter(cartId=self.data['id'])
            price={
                "discount_price" : 0,
                "total_price":0}


            for item in cart_items:
                count=item.quantity
                on_product=item.product.discount.with_product
                get_product=item.product.discount.get_product
                price['total_price']+=count*item.product.price
                price['discount_price'] +=count*item.product.price
                if count>on_product:
                    count+=get_product
                    price['total_price']+=get_product*item.product.price

            price['total_discount']=price['total_price']-price['discount_price']

            return {"Status":True,"data":price}
        except Exception as ae:
            return {"Status":True,"msg":ae}

