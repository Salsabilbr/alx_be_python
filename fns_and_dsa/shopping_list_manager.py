shopping_list = []
def display_menu():
    print("\nShopping List Manager")
print("1. Add Item")
print("2. Remove Item")
print("3. View List")
print("4. Exit")
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(item, "added to the shopping list")
def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(item, "removed from the shopping list")
    else:
        print(item, "not found in the shopping list")
        def view_list():
    print("Current Shopping List:")
    for item in shopping_list:
        print("-", item)
        if __name__ == "__main__":
    main()
