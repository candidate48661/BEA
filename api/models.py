import json

class AccountModel:
    def __init__(self, account_type, account_number, name, first_name, address, birthdate):
        # We will automatically generate the new id
        self.id = 0
        self.type = account_type
        self.number = account_number
        self.name = name
        self.first_name = first_name
        self.address = address
        self.birthdate = birthdate
        #We will automatically generate next 2 parameters based on client address.
        self.longitude = 0
        self.latitude = 0

    @classmethod
    def fromData(self, entries):
        id = entries["id"]
        type = entries["type"]
        number = entries["number"]
        name = entries["name"]
        first_name = entries["first_name"]
        address = entries["address"]
        birthdate = entries["birthdate"]
        longitude = entries["longitude"]
        latitude = entries["latitude"]
        result = AccountModel(type, number, name, first_name, address, birthdate)
        result.id = id
        result.latitude = latitude
        result.longitude = longitude
        return result
