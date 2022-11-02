"""
Name: Austin Kim
My entire program's time complexity is O(n^2) because although my deliver_packages() algorithm is O(n), it is only
because I manually load each truck. If I were to use the worst case and have each truck load only 1 package, then the
deliver_packages() function would run n times, meaning O(n*n) = O(n^2).
All time complexities in this project are written in big-O (worst case).
"""

from populate_data import populate_hash_table
from truck import Truck
from algorithm import deliver_packages
from datetime import datetime

# Time Complexity = O(n^2).
def console_ui():
    user_input = input("\n-Enter a time in 24-hour format on or after 08:00:00 (ex: '13:00:00'): ")
    user_input_time = datetime.strptime(user_input, '%H:%M:%S')

    ht = populate_hash_table()          # O(n), explained in populate_data.py
    # The packages are manually loaded for each truck and trip
    packages_truck1trip1 = [13, 14, 15, 16, 19, 20, 1, 34]
    packages_truck1trip2 = [6, 25, 28, 32, 24, 26, 2, 33]
    packages_truck2trip1 = [29, 30, 31, 37, 40, 3, 18, 36, 38, 21, 4, 5, 7, 8, 10, 17]
    packages_truck2trip2 = [9, 11, 12, 22, 23, 27, 35, 39]
    # All times in the program are stored in datetime instead of strings
    eight_am = datetime.strptime("08:00:00", '%H:%M:%S')
    nine_thirty_five_am = datetime.strptime("09:35:00", '%H:%M:%S')
    ten_twenty_am = datetime.strptime("10:20:00", '%H:%M:%S')
    # The 2 trucks are loaded with packages and expected delivery start of 8am.
    truck1 = Truck(packages_truck1trip1, eight_am)
    truck2 = Truck(packages_truck2trip1, eight_am)

    # The truck 1 and 2 only become "en route" if time is 8am or later
    if user_input_time >= eight_am:
        truck1 = deliver_packages(truck1, ht, user_input_time)
        truck2 = deliver_packages(truck2, ht, user_input_time)

    # Truck 1 is only loaded for trip 2 if the time limit is 9:35am or later
    if user_input_time >= nine_thirty_five_am:
        truck1.prepare_truck(packages_truck1trip2, nine_thirty_five_am)
        truck1 = deliver_packages(truck1, ht, user_input_time)

    # Truck 2 is only loaded for trip 2 if the time limit is 10:20am or later
    # The address for package 9 is only corrected at 10:20am.
    if user_input_time >= ten_twenty_am:
        incorrect_package = ht.search(9)
        incorrect_package.address = "410 S State St"
        incorrect_package.city = "Salt Lake City"
        incorrect_package.zip_code = "84111"
        ht.insert(9, incorrect_package)
        truck2.prepare_truck(packages_truck2trip2, ten_twenty_am)
        truck2 = deliver_packages(truck2, ht, user_input_time)

    # Prints the list of all packages and also the final mileage of entire trip of both trucks.
    for package in ht.all_packages():
        print(package)
    print("\n-Total mileage traveled by all trucks (as of " + user_input + "): "+ str(truck1.miles_traveled + truck2.miles_traveled))

console_ui()
