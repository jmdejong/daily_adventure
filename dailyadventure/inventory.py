
from .items import get_item

class Inventory:
    
    def __init__(self, items=None):
        if items is None:
            items = {}
        elif isinstance(items, list):
            items = {item: 1 for item in items}
        elif not isinstance(items, dict):
            raise TypeError("unknown type for inventory item list")
        
        self.items = {get_item(name): num for name, num in items.items()}
    
    def add(self, item, amount=1):
        self.items[item] = self.items.get(item, 0) + amount
    
    def has(self, item, amount=1):
        return self.items.get(item, 0) >= amount
    
    def remove(self, item, amount=1):
        self.items[item] = self.items.get(item, 0) - amount
    
    def view(self):
        return [(item.name, num) for item, num in self.items.items()]
    
    def save(self):
        return {item.id: num for item, num in self.items.items()}
