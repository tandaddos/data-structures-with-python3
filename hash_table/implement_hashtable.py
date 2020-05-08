class MyHashTable:
    '''
    Implements a hash table using list/array of lists.
        Python list is  an array, accessed via numeric index.
        The data structure is:
            hashtable = [ [value list_1], [value_list_2], ..... ]
            hashtable[ hashed_key_1 ] ==> [ value_list_1 ]

            hashed_key_n = hash of a user key
            value_list_n is a list of user data (can be anything)
            Typically, value_list_n can also include the non-hashed user key
                - which could be useful for doing re-hash in case of collisions
    '''

    def __init__(self, size=256):
        # init table and pre-fill with empty value lists
        # this way, later on, we don't have to use 'table.append()' method
        # when adding new entries to the table.
        # The entries themselves, i.e. the value lists, are empty though, so
        # still have to use 'value_list.append()' to add user data.
        self.tablesize = size
        self.hashtable = [[] for _ in range(self.tablesize)]

    def hash(self, key):
        return hash(key)

    def set(self, key, value):
        # will use default built-in hash function
        hashkey = self.hash(key) % self.tablesize

        # get value_list corresponding to this hashkey
        val_list = self.hashtable[hashkey]

        if not val_list:
            val_list.append([key, value])
            # print(f'{self.hashtable} \n')
            return

        # retrieve index and value from value list
        # we decide to also save the user key
        for i, kv in enumerate(val_list):
            k, v = kv
            if k == key:
                # existing value in value list
                val_list[i] = [key, value]
                break
            else:
                # print(f'(appending {key} {value} ...')
                val_list.append([key, value])
                break

        # print(f'{self.hashtable} \n')

        return

    def get(self, key):
        hashkey = self.hash(key) % self.tablesize
        val_list = self.hashtable[hashkey]
        for i, kv in enumerate(val_list):
            k, v = kv
            if k == key:
                return v
        return None

    def clear(self):
        # don't make the table itself empty
        # only make the value lists empty
        for val_list in self.hashtable:
            val_list.clear()
        # print(f'{self.hashtable} \n')

    def delete(self, key):
        hashkey = self.hash(key) % self.tablesize
        val_list = self.hashtable[hashkey]
        for i, kv in enumerate(val_list):
            k, v = kv
            if k == key:
                # print(f'deleting {k}, {v}')
                # print(f'before: {val_list} \n')
                del val_list[i: i + 1]
                # print(f'after: {val_list} \n')
                # print(f'whole table: {self.hashtable} \n')
                return

    def keys(self):
        # get keys of the table itself
        keys_in_table = []
        for i, sublists in enumerate(self.hashtable):
            for key, val in sublists:
                keys_in_table.append(key)
        return keys_in_table

    def __str__(self):
        return ''.join(str(self.hashtable))


if __name__ == "__main__":
    print(f'CREATING HASH TABLE ...')
    ht = MyHashTable(3)
    print(ht)

    # set some values
    print(f'POPULATING TABLE ...')
    ht.set('drink', 'wine')
    ht.set('snack', 'chips')
    ht.set('main_course', 'steak')
    ht.set('condiments', ['ketchup', 'pickles'])
    print(ht)

    print(f'TABLE KEYS ARE ....')
    print(ht.keys())

    # see those values
    mydrink = ht.get('drink')
    mysnack = ht.get('snack')
    mycourse = ht.get('main_course')
    print(f'SEE THE POPULATED TABLE ...')
    print(f'drink ==> {mydrink}')
    print(f'drink ==> {mysnack}')
    print(f'drink ==> {mycourse}')

    # # change a value
    print(f'CHANGING MY DRINK ....')
    ht.set('drink', 'beer')
    mydrink = ht.get('drink')
    print(f'drink ==> {mydrink}')

    # # delete a value
    print(f'REMOVING MY SNACK ....')
    ht.delete('snack')
    print(f'NEW TABLE KEYS ARE ....')
    print(ht.keys())
    print(ht)

    # # clear table
    print(f'CLEARING ALL ....')
    ht.clear()

    print(f'FINAL ==> {ht}')
