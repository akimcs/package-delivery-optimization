from populate_data import populate_distances
import datetime

dist = populate_distances()     # the Distance object which stores the distances between two addresses.

# The Nearest Neighbor Algorithm which delivers all packages inside a given Truck and within a given time limit.
# Time Complexity = O(n), where n = number of packages. The next_location variable is O(n).
def deliver_packages(truck, ht, time_limit):
    for package_id in truck.loaded_packages: # O(1) because max truck packages is 16.
        # Marks all packages as "en route"
        package = ht.search(package_id)
        package.status = "en route"
        ht.insert(package_id, package)

    # Ensures the truck delivers all packages within time limit.
    while truck.loaded_packages and truck.current_time <= time_limit: # O(1) because max truck packages is 16.
        next_location = nearest_address(ht, truck.current_location, truck.loaded_packages)  # O(n)
        # Potential mileage and time are used to ensure the truck does not move and end up past the time limit.
        potential_mileage = dist.find_distance(truck.current_location, next_location)
        potential_arrival_time = truck.current_time + datetime.timedelta(hours=(potential_mileage/18))
        if potential_arrival_time > time_limit:
            return truck        # If the truck can't move any more, then the truck stops and the user is given current information
        else:
            truck.add_miles_time_location(potential_mileage, potential_arrival_time, next_location)     # Truck changes location, mileage, and time if no conditions fail.
        # Once the truck is in a new location, it delivers the packages for this location and marks them delivered and removes from Truck.
        for package_id in truck.loaded_packages:    # O(1)
            package = ht.search(package_id)         # O(n)
            if package.address == truck.current_location:
                truck.loaded_packages.remove(package_id)
                package.status = "delivered at " + truck.current_time.strftime("%H:%M:%S")
                ht.insert(package_id, package)

    # This last section is for when the truck is empty, the truck goes back to the hub.
    potential_mileage = dist.find_distance(truck.current_location, "hub")
    potential_arrival_time = truck.current_time + datetime.timedelta(hours=(potential_mileage / 18))
    if potential_arrival_time <= time_limit:
        truck.add_miles_time_location(potential_mileage, potential_arrival_time, "hub")
    return truck

# The function used to find the address closest to the current location.
# Time Complexity = O(n), where n = number of packages. potential_address = ht.search(package_id).address = O(n)
def nearest_address(ht, current_address, all_package_ids):                  # The parameters are the current location AND all package IDs of possible address delivery locations

    result_address = ht.search(all_package_ids[0]).address                  # Using the first address as a temporary holder.
    min_distance = dist.find_distance(current_address, result_address)      # Again using the first address temporarily but for minimum distance

    for package_id in all_package_ids: # O(1) because only 16 packages in a truck
        potential_address = ht.search(package_id).address # O(n) since HashTable.search()
        distance = dist.find_distance(current_address, potential_address)
        if distance < min_distance:     # If the package address is closer than previously known address, then this new one becomes closest.
            min_distance = distance
            result_address = potential_address

    return result_address
