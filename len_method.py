class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def put(self, key, data):
        hash_value = self.hash_function(key,len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data #replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
            while self.slots[next_slot] != None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot, len(self.slots))

            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                self.data[next_slot] = data #replace
    def hash_function(self, key, size):
         return key % size
    def rehash(self, old_hash, size):
         return (old_hash + 1) % size


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
            else:
                self.slots[next_slot] = None

    '''implementing the __len__ method'''

    def __len__(self):
        count = 0
        for value in self.slots:
        	 if value != None:
        	 	 count += 1
        return count

def __delitem__(self, key):
	return self.delete(key)
def __getitem__(self, key):
    return self.get(key)
def __setitem__(self, key, data):
    self.put(key, data)
h=HashTable()
h.put(54,"cat")
h.put(26,"dog")
h.put(93,"lion")
h.put(17,"tiger")
h.put(77,"bird")
h.put(31,"cow")
h.put(44,"goat")
h.put(55,"pig")
h.put(20,"chicken")
print(h.slots)
print(f'The length of the list is: {len(h)}\nexcluding the "None"')
