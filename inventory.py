
"""
default inventory
"""
inv = {
    "arrow":12,
    "gold coin": 42,
    "rope": 1,
    "torch":6,
    "dagger":1
    }

"""
STEP1
inventory display
"""
s = sum(inv.values())
def display_inventory(**loot):
    print("Inventory: ")
    for k, v in loot.items():
        print("%s %s" % (v, k))
    print("Total number of items: ", "%d" % (s))

"""
STEP2
dictionary representing the player’s inventory and the added_items parameter is a list like dragon_loot.

"""

def add_to_inventory(inventory, added_items):
    added_items_dict = {}
    for item in added_items:
        x = added_items.count(item)
        if item not in added_items_dict:
            added_items_dict[item] = 1
        else:
            added_items_dict[item] = x

    for k, v in added_items_dict.items():
        if k in inventory:
            x = inventory[k]
            inventory[k] = v + x
        else:
            inventory[k] = v
    inv = inventory
    return inv

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  #a vanquished dragon’s loot
inv = add_to_inventory(inv, dragon_loot)
s = sum(inv.values())
display_inventory(**inv)

""" STEP3 """
count_n = "count"
it_n = "item name"
def print_table(order=None):
    print("Inventory: ")
    print("{:>10}{:>10}".format(count_n,it_n))
    print('   -------------------')
    if order is None:
        for k, v in inv.items():
            print("{:>10}{:>10}".format(inv[k], k))
    elif order is "ascending":
        for k in sorted(inv, key = inv.get, reverse = False):
            print("{:>10}{:>10}".format(inv[k], k))
    elif order is "descending":
        for k in sorted(inv, key = inv.get, reverse = True):
            print("{:>10}{:>10}".format(inv[k], k))
    print('   -------------------')
    print("Total number of items: ", "%d" % (s))

print_table()
print_table("descending")
print_table("ascending")

"""
STEP4
 line of file convert to dict, merge 2 dictionares
"""

import csv
def import_inventory(filename):
    filename = "inv1.csv"
    file = open(filename, encoding='utf-8', mode ='r')
    reader = csv.reader(file)
    import_inventory_list = list(reader)
    for i in range(1, len(import_inventory_list)):
        if import_inventory_list[i][0] in inv:
            inv[import_inventory_list[i][0]] = inv[import_inventory_list[i][0]]+int(import_inventory_list[i][1])
        else:
            inv[import_inventory_list[i][0]] = int(import_inventory_list[i][1])
import_inventory("inv1.csv")
s = sum(inv.values())
display_inventory(**inv)

"""
STEP5
export all inventory items to a file
"""
def export_inventory(filename=None):
    if filename is None:
        with open("export_inventory.csv", encoding='utf-8', mode ='w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in inv.items()]
    else:
        with open(filename, encoding='utf-8', mode ='w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in inv.items()]
export_inventory()
