# A Package object which is made for each unique package ID and holds all necessary package information
class Package:

    # Time Complexity = O(1), where n = number of packages
    def __init__(self, package_id, address, city, zip_code, deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status

    # Returns a formatted string for each package so repeated printing of packages creates a easy-to-read visualization.
    # Time Complexity = O(1), where n = number of packages
    def __str__(self):
        package_id = str(self.package_id)
        address = self.address
        city = self.city
        zip_code = self.zip_code
        deadline = self.deadline
        weight = self.weight
        status = self.status

        # The numbers are decided using the longest possible string in each field
        if len(package_id) != 2:
            package_id += " "
        if len(status) != 21:
            status += " "*(21-len(status))
        if len(deadline) != 8:
            deadline += " "*(8-len(deadline))
        if len(address) != 38:
            address += " "*(38-len(address))
        if len(city) != 16:
            city += " "*(16-len(city))

        return "Package ID: %s | Status: %s | Deadline: %s | Address: %s | City: %s | Zip Code: %s | Weight: %s" % (package_id, status, deadline, address, city, zip_code, weight)
