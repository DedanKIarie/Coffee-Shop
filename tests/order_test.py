from customer import Customer
from coffee import Coffee
from order import Order

Order.all.clear()

print("Order tests")

c = Customer("Alvin")
coffee = Coffee("Latte")


o = Order(c, coffee, 3.5)
assert o.customer == c
assert o.coffee == coffee
assert o.price == 3.5


try:
    Order("not a customer", coffee, 3.0)
except TypeError:
    pass
else:
    raise AssertionError("Non-customer should raise")

try:
    Order(c, "not coffee", 3.0)
except TypeError:
    pass
else:
    raise AssertionError("Non-coffee should raise")

try:
    Order(c, coffee, 20.0)
except ValueError:
    pass
else:
    raise AssertionError("Out of range price should raise")

try:
    Order(c, coffee, "cheap")
except ValueError:
    pass
else:
    raise AssertionError("Non-float price should raise")

print("Order tests passed")
