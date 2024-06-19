# Write you Customer Class here
class Customer():
    def __init__(self, _id, first_name, last_name, _account_type):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = _account_type
        self._current_video_rentals = []
    
    @property
    def id(self):
        return self.id
    
    @staticmethod
    def create_customer_id(_id, first_name, last_name, account_type):
        return {'id': _id, 'first_name': first_name, 'last_name': last_name, 'account_type': account_type}

    @classmethod
    def add_customer(cls, customers):
        if customers.id in cls.customers:

    