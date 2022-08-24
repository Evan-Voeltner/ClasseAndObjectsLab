class ShoppingCart:
    def __init__(self):
       self.products_in_cart = []

    def calculate_total(self):
        total = 0
        for product in self.products_in_cart:
            total += product.price
        return total

    def add_product_to_cart(self, given_product):
        self.products_in_cart.append(given_product)

    def empty_cart(self):
        self.products_in_cart = []