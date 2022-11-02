# A self-adjusting data structure used to store packages using their package ID
class HashTable():

    # Time Complexity = O(1), where n = number of packages. Since only 2 lists are being made.
    def __init__(self):
        self.num_of_packages = 40
        self.table = [[]]*self.num_of_packages    # The hash table size is 40, the smallest size to prevent collisions.

    # Inserts the package into the hash table
    # Time Complexity = O(n), where n = number of packages. Due to hash chaining, the linked list must be iterated through.
    def insert(self, key, value):
        linked_list = self.table[hash(key) % self.num_of_packages]
        nose_already_exists = False
        for node in linked_list:
            if node[0] == key:
                node[1] = value
                nose_already_exists = True
        if not nose_already_exists:
            node = [key, value]
            linked_list.append(node)

    # Searches the hash table for a package and returns that package.
    # Time Complexity = O(n), where n = number of packages. Due to hash chaining, the linked list must be iterated through.
    def search(self, key):
        linked_list = self.table[hash(key) % self.num_of_packages]
        result_node = None
        for node in linked_list:
            if node[0] == key:
                result_node = node[1]
        return result_node

    # Returns a list of all packages in the hash table
    # Time Complexity = O(n), where n = number of packages. The function iterates through all packages.
    def all_packages(self):
        package_list = []
        for package in range(1, self.num_of_packages+1):
            package_list.append(self.search(package))
        return package_list
