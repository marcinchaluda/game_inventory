# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.
import operator


def display_inventory(inventory = {}):
    """Display the contents of the inventory in a simple way."""
    for item_key, item_value in inventory.items():
        key_value_pair =  f'{item_key}: {item_value}'  
        print(key_value_pair)    

def add_to_inventory(inventory = {}, added_items = []):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory.keys():
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory


def remove_from_inventory(inventory = {}, removed_items = []):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item in inventory.keys():
            inventory[item] = inventory[item] - 1
            if inventory[item] <= 0:
                inventory.pop(item)
    return inventory


def print_table(inventory = {}, order = None):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """
    table_borders = ['-----------------', '|']
    print(table_borders[0])
    print('item name ' + table_borders[1] + ' count')
    print(table_borders[0])
    if order == 'count,asc':
        inventory = dict(sorted(inventory.items(), key = operator.itemgetter(1)))
    elif order == 'count,desc':
        inventory = dict(sorted(inventory.items(), key = operator.itemgetter(1), reverse = True))

    for item_key, item_value in inventory.items():
            print(f'{item_key:>10}' + table_borders[1] + f'{item_value:>6}')
    print(table_borders[0])


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass

def main():
    user_items = {'gold coins': 45, 'arrow': 12, 'torch': 6, 'dagger': 2, 'rope': 1, 'ruby': 1}
    display_inventory(user_items)
    user_items = add_to_inventory(user_items, ['gold coins', 'dupa', 'dupa'])
    print(user_items)
    user_items = remove_from_inventory(user_items, ['rope', 'cycki', 'gold coins', 'gold coins'])
    print(user_items)
    print_table(user_items)
    print_table(user_items, 'count,asc')
    print_table(user_items, 'count,desc')

if __name__ == '__main__':
    main()