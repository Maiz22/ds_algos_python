class HashTable:
    """
    Class represeting a hash table in python to get a better 
    understanding of the unerlying logic of a hash map.
    """
    def __init__(self, max_size:int) -> None:
        """
        Takes a given max_size and creates a data list, which
        is the basic of any hash map.
        """
        self.data_list = [None] * max_size

    def get_valid_index(self, key) -> int:
        """
        Takes a key and creates an index by using pythons hash 
        function. Implements linear probing to avoid collision.
        """
        idx = hash(key) % len(self.data_list)
        while True:
            key_value_pair = self.data_list[idx]
            if not key_value_pair:
                return idx
            k, v = key_value_pair
            if k == key:
                return idx
            idx+=1
            if idx == len(self.data_list):
                idx = 0

    def __getitem__(self, key):
        """
        By overwriting the getitem method elements can be accessed
        like sequences. Returns the corresponding value to the key
        or None if no value at key.
        """
        idx = self.get_valid_index(key)
        key_value_pair = self.data_list[idx]
        return key_value_pair[1] if key_value_pair else None
    
    def __setitem__(self, key, value) -> None:
        """
        By overwriting the setitem method a key, value pair can 
        be added like in a sequence.
        """
        idx = self.get_valid_index(key)
        self.data_list[idx] = key, value

    def __iter__(self):
        """
        Allows our array to be accessed like an iterator.
        """
        return (x for x in self.data_list if x is not None)
    
    def __len__(self):
        """
        Overwriting the len function to return the length of 
        our hash table by iterating threw self using the previously
        implemented iterator.
        """
        return len([x for x in self])
    

if __name__ == "__main__":
    new_hash_table = HashTable(max_size=1024)
    new_hash_table["a"] = 1
    new_hash_table["b"] = 2
    new_hash_table["c"] = 3
    print(len(new_hash_table))
    for k, v in new_hash_table:
        print(f"key: {k}, value: {v}")