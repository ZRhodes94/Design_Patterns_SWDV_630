"""
Specify the kinds of objects to create using a prototypical instance,
and create new objects by copying this prototype.
"""

import copy


class Reservation:
    def __init__(self, name, phone, days, room_type, reservation_list = None):
        self.name = name
        self.phone = phone
        self.days = days
        self.room_type = room_type
        self.reservation_list = reservation_list
        self.reservation_list = {'reservation_day_1': self} 
        
    def clone(self):
        total_days = self.days
        
        for i in range(self.days-1):
            
            self.days = self.days - 1
            self.reservation_list.update({'reservation_day_'+ str(total_days - self.days + 1): copy.deepcopy(self)})
            
        return self.reservation_list

def main():
    reservation = Reservation("Zachary Rhodes", "314-525-4440", 3, "Standard")
    reservation.clone()
    print(reservation.reservation_list)
    print(reservation.reservation_list['reservation_day_2'].days)

main()
