
from .item import Item


class ItemSpace:
    
    def __init__(self, data):
        for id, item in data.items():
            setattr(self, id, item)

def _make_items(data):
    itemdict = {}
    for d in data:
        if isinstance(d, str):
            item = Item(d)
        else:
            item = Item(*d)
        itemdict[item.id] = item
    return itemdict

_itemdata = [
    "coins",
    "dagger",
    "warrior_diploma",
    "wooden_sword",
    "firewood",
    "stick"
]


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
