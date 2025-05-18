from customer import Customer
from coffee import Coffee
from order import Order
# resets order
Order.all.clear()
print("Testign customer")

c1 = Customer("Alvin")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Expresso")
o1 = c1.create_order(coffee1, 4.5)
o2 = c1.create_order(coffee2, 3.0)