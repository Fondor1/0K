__author__ = 'rakai'

from guildwars2api.v2.client import GuildWars2API
# import sqlite3


class Item:

    def __init__(self, item):
        for k, v in item.items():
            setattr(self, k, v)


if __name__ == '__main__':

    # rayal's key: 81668F5F-5866-8F41-81B8-6DF706417B5993297C30-5BAE-44E3-8715-5F94D84AFD8A
    apiv2 = GuildWars2API(api_key='81668F5F-5866-8F41-81B8-6DF706417B5993297C30-5BAE-44E3-8715-5F94D84AFD8A')

    # List if ids
    bank_materials = [item['id'] for item in apiv2.bank_materials.get_all()]
    bank_items = [item['id'] for item in apiv2.bank.get_all() if item is not None]
    bank_all = bank_materials + bank_items

    # Convert those ids to Items
    # This should work but fails because it tries to look up a non-existing item id
    items = [Item(item) for item in apiv2.items.get(ids=bank_materials)]
    print(list(item.name for item in items))

    # all_recipes = list(apiv2.recipes_search(input=bank_items+bank_materials))
