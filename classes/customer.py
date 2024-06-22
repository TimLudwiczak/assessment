# Write you Customer Class here
import csv
import os

class Customer():
    customers = []
    def __init__(self, _id, first_name, last_name, account_type, current_video_rentals = None):

        self._id = _id
        self._account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self.current_video_rentals = current_video_rentals if current_video_rentals is not None else []
    
    @property
    def id(self):
        return self._id
    @property
    def account_type(self):
        return self._account_type
    @property
    def current_video_rentals(self):
        return self._current_video_rentals
    
    @current_video_rentals.setter
    def _current_video_rentals(self, vid_rentals):
        if not isinstance(vid_rentals , list):
            return ValueError('Current Video Rentals should only be a list')
        self._current_video_rentals = vid_rentals
    
    @classmethod
    def create_customer(cls, _id, first_name, last_name, account_type, current_video_rentals=None):
        if isinstance(current_video_rentals, str):
            current_video_rentals = current_video_rentals.split('/') if current_video_rentals else []
        return cls(_id, first_name, last_name, account_type, current_video_rentals)
    
    @classmethod
    def load_customers(cls, csv_file):
        script_dir = os.path.dirname(__file__)

        relative_path = os.path.join(script_dir, '..', 'data', csv_file)

        with open(relative_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer = cls.create_customer(
                    row['id'],
                    row['first_name'],
                    row['last_name'],
                    row['account_type'],
                    row.get('current_video_rentals', '').split('/') if 'current_video_rentals' in row else []
                )
                cls.customers.append(customer)
        return cls.customers
customers = Customer.load_customers('customers.csv')

for customer in customers:
    print(f'ID: {customer.id}, Name: {customer.first_name} {customer.last_name}, Account Type: {customer._account_type}, Rentals: {customer._current_video_rentals}')
