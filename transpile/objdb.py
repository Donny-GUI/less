
import atexit
import luaparser.ast as last
import os
import hashlib
import pickle
import os



class ObjectDatabase:
    def __init__(self, file_path=None):
        """
        Initialize the ObjectDatabase. Optionally load from a file.
        """
        self.file_path = file_path
        self.node = None
        self.result = None
        self._store = {}
        if self.file_path:
            self.load(self.file_path)
        self._interval= 250
        self._c = 0
        atexit.register(self.show_database)

    def check_node(self):
        return self.get_hash(self.node)

    def set_node(self, node):
        self.node = self._generate_hash(node)
    
    def set_result(self, result):
        self.result = result
        self._store[self.node] = self.result
        self._c+=1
        if self._c == self._interval:
            self.save_to_file(self.file_path)
            self._c=0

    def _load_result(self, hash_):
        return self._store[hash_]
        

    def _generate_hash(self, obj):
        """
        Generate a unique hash for a given object using SHA-256.
        """
        obj_bytes = pickle.dumps(obj)
        return hashlib.sha256(obj_bytes).hexdigest()

    def save(self, node, result):
        """
        Save an object in the database. The node will be hashed, and the node hash will be used as the key to the hashed object.
        """
        self.set_node(node)
        self.set_result(result)
        return self.node

    def get(self, node):
        nodehash = self._generate_hash(node)
        return self.get_hash(nodehash)

    def get_hash(self, obj_hash):
        """
        Retrieve an object from the database using its hash.
        """
        return self._store.get(obj_hash, None)

    def delete(self, obj_hash):
        """
        Remove an object from the database using its hash.
        """
        if obj_hash in self._store:
            del self._store[obj_hash]
            return True
        return False

    def list_all_hashes(self):
        """
        List all hashes of the objects stored in the database.
        """
        return list(self._store.keys())

    def items(self):
        return self._store.items()

    def keys(self):
        return list(self._store.keys())

    def has_key(self, node):
        h = self._generate_hash(node)
        return h in self.keys()

    def save_to_file(self, file_path):
        """
        Save the entire database to a file.
        """
        with open(file_path, 'wb') as file:
            pickle.dump(self._store, file)

    def load(self, file_path):
        """
        Load the database from a file.
        """
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                self._store = pickle.load(file)
        else:
            self.save_to_file(file_path)
            self.load(file_path)

    def show_database(self):
        items = self._store.items()
        print("total_entries: ", str(len(items)))
        print(items[0:len(items)/20])
        


