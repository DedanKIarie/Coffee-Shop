class Coffee:
    def __init__(self,name):
        if isinstance(name, str) and len(name)>=3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 char long")
        
    @property
    def name(self):
        return self._name
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def cofees(self):
        return list({order.customer for order in self.orders()})