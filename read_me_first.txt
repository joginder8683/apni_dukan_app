Used Tech:
	Python
	Django
	Django Rest Framework
	PostgreSQL db
	Docker

	
Shop App is created in APNI DUKAN Project where i have written models and the API to 
add/remove product in the cart, apply coupon code to the some of product decided by the
admin(admin can relate any product with any coupon code).

Adding product to datebase functionality is given to the admin and also API is written to do so if admin want to add product by API and 
same admin can do with the COUPON (admin can add coupon by API or directly by admin block)). 

Apart from that user can add product to the Cart as per his/her needs with the help of Rest API and the finally can order the
products added into the cart and in return user will get total cost of products  in a cart,product total after discount and total
discount on the products.

*There is One-To-Many relation of coupon to the Product


About the MODELS:

1.	DiscountCode model is created which maintain the COUPON code with its basic description. (eg.  if you buy X product get Y product free).

2. 	Product model maintains the details about the product and also product has the relation with DiscountCode. and also relation could be
	null. so its upto admin wheather he want to relate any coupon with the product or not.
	
3.	Cart model basically maintains wheather the cart is activated or not. to add the items in the cart we need to activate the cart first

4.	CartItem model handels the product and its quantity (user can increase the quantity of the product user will not have to add the 
    product again and again user can just simply increase the quantity of the product). CartItem has relation with Product and also with the 
	Cart in which he/she want to add those cart items
	
	
	
	
RestAPI Guide:



1.	add coupon API is the basically add the coupon code to db. below is the guide to call the api .


		request_type:- POST        url:-   http://localhost:port/add_coupon/    

		body={
					"with":2,
					"get":2,
					"desc":"cool offer"	
				}	
			
			
		* the api will add the coupon to the db with description "Cool offer" that if user buy 2 product then he will get 2 product free with it



2.	add product API gives admin the functionality to add products to the db. which is also possible by admin pannel.

		request_type:- POST			url:-	http://host:port/add_product/
		
			=> add product without any discount code
		body={
							"name":"product_1",
							"price":1299,
							"desc":"first product added"
				
						}
						
					#===OR===#
					
			=> add product with any discount code
			
		body={
							"name":"product_2",
							"price":1199,
							"desc":"second product added",
							"coupon":1	
						}
						
		* here product_1 is added to the db with some details but without any coupon code later we can add the couponcode in the admin panel
		but if admin want to do that with the api the he/she can do that also. but for that user need to pass coupon(object id) to form data
		while calling the API
		note:- i have shown both the ways above



3.	add product to cart 

		request_type:-	POST		url:-	http://host:port/add_product_in_cart/
		
			=>	add product in new cart
		body={
					"coupon":1,
					"product":1,
					"quantity":5,
					}

				#===OR===#

			=>	add product in existing cart
					
		body={
						"coupon":1,
						"product":1,
						"quantity":5,
						"cart":4
					
					}
		
		* user can add products to the cart. by default product will be added to the new cart but you user want to add product
		to the existing cart then user can do so but for that user have to pass the cart id while calling the API.
		note:- i have shown both the ways above
	

	
4.	order products API

	request_type:-	POST		url:-	http://host:port/order/
	
	body={
			'id':1
		}

	*User have to pass the cart id  and user  will get the total of all products in a cart, product total after discount and total
				discount on the products.




	
	
