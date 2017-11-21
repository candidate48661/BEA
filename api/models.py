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
        self.longitude = 0;
        self.latitude = 0;