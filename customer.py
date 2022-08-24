from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.customer_name = name
        self.customer_cart = ShoppingCart()

    def add_new_product(self, new_product):
        self.customer_cart.add_product_to_cart(new_product)

    def list_products(self):
        for product in self.customer_cart.products_in_cart:
            print(f'{product.name} | {product.price} | {product.category}')