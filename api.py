__author__ = 'rakai'

from guildwars2api.v2.client import GuildWars2API


class Item:

    def __init__(self, item):
        for k, v in item.items():
            setattr(self, k, v)


if __name__ == '__main__':

    # rayal's key: 81668F5F-5866-8F41-81B8-6DF706417B5993297C30-5BAE-44E3-8715-5F94D84AFD8A
    apiv2 = GuildWars2API(api_key='81668F5F-5866-8F41-81B8-6DF706417B5993297C30-5BAE-44E3-8715-5F94D84AFD8A')

    # Test item:
    # i = {'icon': 'https://render.guildwars2.com/file/65A0C7367206E6CE4EC7C8CBE07EABAE0191BFBA/561548.png', 'details': {'infusion_slots': [], 'weight_class': 'Medium', 'type': 'Helm', 'defense': 97, 'suffix_item_id': 24696, 'infix_upgrade': {'attributes': [{'attribute': 'Healing', 'modifier': 60}, {'attribute': 'Power', 'modifier': 43}, {'attribute': 'Toughness', 'modifier': 43}]}, 'secondary_suffix_item_id': ''}, 'id': 123, 'restrictions': [], 'flags': ['Activity', 'Wvw', 'Dungeon', 'Pve', 'SoulBindOnUse'], 'vendor_value': 330, 'description': '', 'game_types': ['Activity', 'Wvw', 'Dungeon', 'Pve'], 'rarity': 'Exotic', 'name': "Zho's Mask", 'type': 'Armor', 'level': 80, 'default_skin': 95}
    # item = Item(i)

    bank_materials = list(apiv2.bank_materials.get_all())

    for material in bank_materials:
        # Very slow
        print('item:', apiv2.items.get(id=material['id'])['name'], 'quantity:', material['count'])