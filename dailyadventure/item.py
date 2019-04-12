

class Item:
    
    def __init__(self, id, name=None, description=None, sprite=None):
        self.id = id
        if name is None:
            self.name = id.capitalize().replace('_', ' ')
        else:
            self.name = name
        description = description
        sprite = sprite
