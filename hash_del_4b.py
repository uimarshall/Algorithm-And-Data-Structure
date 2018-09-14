#4bi
"""
Deleting an item from a hash table using chaining for collision resolution
--------------------------------------------------------------------------
To delete an item from a hash table that uses chaining for collision resolution,
the hash value of the item is first derived using the modulo division.
Since the chaining method places multiple items on a single slot (Implemented
with a list), a sequential search is done on the slot and item deleted when found
"""
#4bii
"""
Deleting an item from a hash table using open adressing for collision resolution
--------------------------------------------------------------------------------
To delete an item from a hash table that uses the open addressing method for
collision resolution, the hash value ofthe item is first derived using
the modulo division. If the slot is occupied already with another item, a
sequential search is done until the item is found and then deleted. This is so
since items that have their slots already occupied are placed in the next empty
slot after them.
"""
#4biii
"""

"""

#==============================================================================
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, data):
        hash_value = self.hash_function(key,len(self.slots))

        if self.slots[hash_value] == None: #Empty slot
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key: #for value replacement
                self.data[hash_value] = data
            else:
                #if some other key value is in this position, run this(look for another slot)
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data #replace

    def delete(self, key):
        hash_value = self.hash_function(key,len(self.slots))

        if self.slots[hash_value] == key: #Item in original slot
            self.slots[hash_value] = None
            self.data[hash_value] = None
        else:
            #if key not found in original slot, do a search for it
            next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] != key:
                next_slot = self.rehash(hash_value, len(self.slots))
            if self.slots[next_slot] == key:
                self.slots[next_slot] = None
                self.data[next_slot] = None
                #next_slot = self.rehash(hash_value, len(self.slots))
            else:
                self.slots[next_slot] = None
                self.data[next_slot] = None

    def __len__(self):
        slot_counter = 0
        for slot in range(self.size):
            if self.slots[slot] != None:
                slot_counter += 1
        return slot_counter

    def __contains__(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        #data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                #data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
            if position == start_slot:
                stop = True
        return found
#==============================================================================
    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
            if position == start_slot:
                stop = True
        return data
#=========================================================================
h = HashTable()

h.put(54, "cat")
h.put(26, "dog")
h.put(93, "lion")
h.put(17, "tiger")
h.put(77, "bird")
h.put(31, "cow")
h.put(44, "goat")
h.put(55, "pig")
h.put(20, "chicken")

print(f'The original list contains 44: {h.slots}')
print(h.__contains__(44))
print(f'The length of the list before deletion is: {h.__len__()}')
h.delete(44)
print("\n")
print(f'The list after Deletion does not contain 44: {h.slots}')
print(f'The length of the list after deletion is: {h.__len__()}')
