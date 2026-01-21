phonebook = {
    "Harry": "9876543210",
    "Sam": "9123456789",
    "John": "9987654321",
    "Sarah": "9111222333"
}

def search(name):
    """Search for a contact in the phonebook"""
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook")

def add(name, number):
    """Add a new contact to the phonebook"""
    if name in phonebook:
        print(f"{name} already exists in phonebook")
    else:
        phonebook[name] = number
        print(f"{name} added successfully with number {number}")

def delete(name):
    """Delete a contact from the phonebook"""
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted successfully")
    else:
        print(f"{name} not found in phonebook")

def display():
    """Display all contacts"""
    print("\n--- Phonebook ---")
    for name, number in phonebook.items():
        print(f"{name}: {number}")
    print()

# Test the functions
print("Initial Phonebook:")
display()

print("Searching for 'Sam':")
search("Sam")

print("\nSearching for 'Mike' (doesn't exist):")
search("Mike")

print("\nAdding 'Mike' to phonebook:")
add("Mike", "9555666777")

print("\nPhonebook after adding Mike:")
display()

print("Deleting 'John' from phonebook:")
delete("John")

print("\nPhonebook after deletion:")
display()

print("Trying to delete 'John' again (doesn't exist):")
delete("John")
