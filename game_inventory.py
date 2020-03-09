# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.

user_items = {'gold_coins': 45, 'arrow': 12, 'torch': 6, 'dagger': 2, 'rope': 1, 'ruby': 1}

def display_inventory(inventory = {}):
    """Display the contents of the inventory in a simple way."""
    for item_key, item_value in inventory.items():
        key_value_pair =  f'{item_key}: {item_value}'  
        print(key_value_pair)    

display_inventory(user_items)
def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    pass


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    pass


def print_table(inventory, order):
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    """

    pass


def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
