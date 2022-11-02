# The Truck object stores what packages each truck is holding, the time, location, and miles traveled.

class Truck:

    # Time Complexity = O(1), where n = number of packages
    def __init__(self, loaded_packages, current_time):
        self.loaded_packages = loaded_packages
        self.current_time = current_time
        self.current_location = "hub"
        self.miles_traveled = 0.0

    # Used in the main function to load the trucks after their first trip.
    # Time Complexity = O(1), where n = number of packages
    def prepare_truck(self, packages, time):
        self.loaded_packages = packages
        self.current_time = time

    # Used after the truck moves to a different location, used to track total time/miles.
    # Time Complexity = O(1), where n = number of packages
    def add_miles_time_location(self, miles, time, location):
        self.miles_traveled += miles
        self.current_time = time
        self.current_location = location
