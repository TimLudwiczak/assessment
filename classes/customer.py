# Write you Customer Class here
import csv

class Customer():
    customers = []

    def __init__(self, _id, first_name, last_name, _account_type, _current_video_rentals):

        self._id = _id
        self._account_type = _account_type
        self.first_name = first_name
        self.last_name = last_name
        self._current_video_rentals = _current_video_rentals
    
    @property
    def id(self):
        return self._id
    
    @classmethod
    def create_customer_id(cls, _id, first_name, last_name, _account_type):
        return cls(_id, first_name, last_name, _account_type)
    
    @classmethod
    def load_customers(cls, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer = cls.create_customer(row['id'], row['first_name'], row['last_name'], row['account_type'])
                cls.customers.append(customer)
            cls.customers = list(reader)
        return cls.customers

Customer.load_customers('customers.csv')
