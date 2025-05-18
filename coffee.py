class Coffee:
    def __init__(self,name):
        if isinstance(name, str) and len(name)>=3:
            self._name = name
        else:
            raise ValueError("Coffee name must be at least 3 char long")
        
    @property
    def name(self):
        return self._name