class Contact:
    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size: int):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        """Simple hash using character ordinals summed and modded by size."""
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key: str, number: str):
        """Insert or update a contact in the hash table."""
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        if self.data[index] is None:
            self.data[index] = new_node
            return

        current = self.data[index]
        while current:
            if current.key == key:
                current.value.number = number
                return
            if current.next is None:
                break
            current = current.next

        current.next = new_node

    def search(self, key: str):
        """Search for a contact by name and return Contact or None."""
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        """Display hash table structure for debugging."""
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            if node is None:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()  

if __name__ == "__main__":
    table = HashTable(10)
    print("Initial table:")
    table.print_table()

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")

    print("\nAfter adding John and Rebecca:")
    table.print_table()

    contact = table.search("John")
    print("\nSearch result:", contact)

    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")

    print("\nAfter testing collisions:")
    table.print_table()

    table.insert("Rebecca", "999-444-9999")

    print("\nAfter updating Rebecca:")
    table.print_table()

    print("\nSearch for Chris:", table.search("Chris")) 



# """
# Design Memo

# A hash table is a good choice for this project because it can store and find contacts very quickly. When you use a list, the computer has to look at every item to find the one you want. This takes more time as the list grows. A hash table uses a hash function to turn the contact name into a number that points directly to where the contact is stored. This means that adding or searching for a contact is usually much faster than using a list. Fast lookups are important for devices with limited memory or processing power.

# In this program, each contact name is used as a key and each phone number is stored as the value. The hash function adds the number values of the letters in the name and then uses the remainder when divided by the table size to choose a position. Sometimes two names will hash to the same index, which is called a collision. To handle collisions, the table uses a linked list so more than one contact can be stored at the same index without losing data. This method is called separate chaining and it keeps the table organized even when many contacts are added.

# If a contact with the same name is added again, the program updates the number instead of creating a new one. A hash table is a good choice when speed matters more than keeping the data in order. Engineers often use hash tables for phonebooks, caches, and small databases that need fast searching and updating.
# """
 