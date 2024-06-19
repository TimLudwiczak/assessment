# Write your independent Customer account type classes here
from classes.customer import Customer

class Customer_sx:
    max_rental = 1
    def rent(self, rating):
        return len(self._current_video_rentals) < self.max_rental

class Customer_px:
    max_rental = 3
    def can_rent(self, rating):
        if rating == "R":
            return False
        return len(self.rentals) < self.max_rental

class Customer_sf:
    max_rental = 1
    def rent(self, rating):
        return len(self._current_video_rentals) < self.max_rental
   
class Customer_pf:
    max_rental = 3
    def can_rent(self, rating):
        if rating == "R":
            return False
        return len(self.rentals) < self.max_rental