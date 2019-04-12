
from .item import Item


class ItemSpace:
    
    def __init__(self, data):
        for id, item in data.items():
            setattr(self, id, item)

def _make_items(data):
    itemdict = {}
    for id, attributes in data.items():
        item = Item(id, *attributes)
        itemdict[id] = item
    return itemdict

_itemdata = {
    "dagger": (),
    "warrior_diploma": (),
    "wooden_sword": ()
}


_conversion = {
    #"dagger": "copper_dagger",
    "warrior diploma": "warrior_diploma",
    "wooden sword": "wooden_sword"
}

itemdict = _make_items(_itemdata)
items = ItemSpace(itemdict)

def get_item(id):
    if id in _conversion:
        id = _conversion[id]
    return itemdict[id]
