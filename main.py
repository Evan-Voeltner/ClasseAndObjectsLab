from alarm_clock import AlarmClock
from customer import Customer
from shopping_cart import ShoppingCart
from product import Product

evans_alarm_clock = AlarmClock()

print(evans_alarm_clock.current_time)
evans_alarm_clock.set_alarm()
evans_alarm_clock.toggle_on_off()

evan_the_customer = Customer('Evan')
bread = Product('Bread', 3.99, 'Baked Good')
milk = Product('Milk', 1.99, 'Dairy')
bacon = Product('Bacon', 5.99, 'Meat')

print(evan_the_customer.customer_name)

evan_the_customer.add_new_product(bread)
evan_the_customer.add_new_product(milk)
evan_the_customer.add_new_product(bacon)

evan_the_customer.list_products()

evans_total_cost = evan_the_customer.customer_cart.calculate_total()
print(evans_total_cost)

evan_the_customer.customer_cart.empty_cart()

evan_the_customer.list_products()


