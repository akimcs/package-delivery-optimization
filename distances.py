# the Distance object is a data structure consisting of 2 lists, used to retrieve the distance between two addresses.
class Distances:

    # Time Complexity = O(1), where n = number of packages. Since the number of packages does not affect the distances data.
    def __init__(self):
        self.address = []           # a list of address strings
        self.travelDistance = []    # a 2d list of floats representing the miles between two addresses

    # Finds the distance between two addresses
    # Time Complexity = O(1), where n = number of packages. Since the number of packages does not affect the distances data.
    def find_distance(self, first_address, second_address):
        # finds the indexes of the addresses from the first list and uses those indexes to find the corresponding distance in the 2d list.
        return self.travelDistance[self.address.index(first_address)][self.address.index(second_address)]
