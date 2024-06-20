# Write your independent Customer account type classes here
from classes.customer import Customer

class Customer_sx(Customer):
    max_rental = 1
    def __init__(self, id, name):
        super().__init__(id, name)
        self.account_type = 'sx'
    def rent(self):
        return len(self._current_video_rentals) < self.max_rental

class Customer_px(Customer):
    max_rental = 3
    def __init__(self, id, name):
        super().__init__(id, name)
        self.account_type = 'px'
        return len(self.rentals) < self.max_rental

class Customer_sf:
    max_rental = 1
    def __init__(self, id, name):
        super().__init__(id, name)
        self.account_type = 'sf'
    def can_rent(self, rating):
        if rating == "R":
            return False
    def rent(self, rating):
        return len(self._current_video_rentals) < self.max_rental
   
class Customer_pf:
    max_rental = 3
    def __init__(self, id, name):
        super().__init__(id, name)
        self.account_type = 'pf'
    def can_rent(self, rating):
        if rating == "R":
            return print('Cannot rent R Movies')
        return len(self.rentals) < self.max_rental