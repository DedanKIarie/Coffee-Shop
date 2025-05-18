from customer import Customer
from coffee import Coffee
from order import Order

Order.all.clear()

print("Coffee tests")

c1 = Coffee("Latte")
assert c1.name == "Latte"
try:
    Coffee("ab")
except ValueError:
    pass
else:
    raise AssertionError("Short name should raise")

cust1 = Customer("Alvin")
cust2 = Customer("Beth")
Order.all.clear()
Order(cust1, c1, 5.0)
Order(cust2, c1, 3.0)

assert len(c1.orders()) == 2

customers = c1.coffees()
assert cust1 in customers and cust2 in customers

assert c1.num_orders() == 2

assert abs(c1.average_price() - 4.0) < 1e-6

print("Coffee tests passed")