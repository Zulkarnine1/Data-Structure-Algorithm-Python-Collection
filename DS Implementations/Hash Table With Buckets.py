class ZulkarsHashTable:
    # Initializing with size
    def __init__(self, size):
        # Initializing size and allocating memory
        self.size = size
        self.data = [None] * size

    # To set value with key O(1)
    def set_value(self, key, val):
        # Hashing key to index
        hash = self.generate_hash(key)
        if (self.data[hash] == None):
            # Opening address to store multiple buckets
            self.data[hash] = []
        # Pushing bucket in bucket list
        self.data[hash].append([key, val])

    # To get value with key
    # Most cases O(1) but for collision O(n)
    def get_value(self, key):
        # Hashing key to index
        hash = self.generate_hash(key)
        # Getting buckets of the address
        buckets = self.data[hash]
        # Looking through buckets to get key matching bucket
        for bucket in buckets:
            if (bucket[0] == key):
                return bucket

    # To get hash size
    # Most cases O(1) but for collision O(n)
    def get_hashsize(self):
        return len(self.data)

    # To generate hash from key === O(1)
    # Hash function is not considered to be time consuming as it just hashes the key
    def generate_hash(self, key):
        # Hash fucntion uses ord func to get char value and adds it up
        index = 0
        for char in key:
            index += ord(char)
        return index % self.size

    # Returns all the keys in the Hash Table
    # O(n*a) as we have to loop through n items and if an address contains a buckets, that will have to be looped as well
    def get_keys(self):
        keysArray = []
        for i in range(len(self.data)):
            # If there is a bucket and not a None
            if self.data[i] != None:
                if len(self.data[i]) == 1:
                    keysArray.append(self.data[i][0][0])
                else:
                    # If multiple buckets, looping through each
                    for bucket in self.data[i]:
                        keysArray.append(bucket[0])
        return keysArray




table = ZulkarsHashTable(100)
table.set_value("abc",10)
table.set_value("cba",20)
table.set_value("xyz",50)
table.set_value("mno",11)
print(table.get_value("cba"))
print(table.get_keys())


