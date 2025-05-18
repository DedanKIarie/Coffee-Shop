from customer import Customer
from coffee import Coffee
from order import Order
# resets order
Order.all.clear()
print("Testign customer")

c1 = Customer("Alvin")
assert c1.name == "Alvin"

try:
    Customer("")
except ValueError:
    pass
else:
    raise AssertionError("Empty name should raise")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Expresso")
o1 = c1.create_order(coffee1, 4.5)
o2 = c1.create_order(coffee2, 3.0)

assert len(c1.orders()) == 2
assert coffee1 in c1.coffees() and coffee2 in c1.coffees()

top = Customer.most_aficionado(coffee1)
assert top == c1

print ("Customer testing is good")