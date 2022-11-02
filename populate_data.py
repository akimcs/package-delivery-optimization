import csv
from hash_table import HashTable
from package import Package
from distances import Distances

# Reads the package csv file and returns a hash table populated with packages
# Time Complexity = O(n), where n = number of packages. Only the operation "for row in opened_file" is n since each row is a package.
def populate_hash_table():
    filled_hash_table = HashTable()       # The 40 is for the total number of packages
    with open('csv/packages_formatted.csv') as package_data:
        opened_file = csv.reader(package_data, delimiter=',')
        for row in opened_file:
            try:
                filled_hash_table.insert(int(row[0]), Package(row[0], row[1], row[2], row[4], row[5], row[6], "at the hub"))
            except ValueError:  # Prevents the first line in the csv file (containing column titles), from being read
                pass
    return filled_hash_table

# Reads the distance csv file and returns a distance object populated with addresses and distances
# Time Complexity = O(1), where n = number of packages. Since more packages does not increase the distance data, this time complexity remains the same.
def populate_distances():
    filled_distance_data = Distances()
    with open('csv/distances_formatted.csv') as distance_data:
        opened_file = csv.reader(distance_data, delimiter=',')
        for row in opened_file:
            temp_distances = []
            for cell in row:
                if not row[0] and cell:     # the csv file was edited so the first row contains address strings and the first cell is empty
                    filled_distance_data.address.append(cell)
                else:
                    try:
                        temp_distances.append(float(cell))
                    except ValueError:      # Prevents an address string from being added to the 2d list of distances
                        pass
            if temp_distances:
                filled_distance_data.travelDistance.append(temp_distances)
    return filled_distance_data
