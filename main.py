import pandas as pd


df = pd.read_csv("hotels.csv",dtype={"id":str})
print(df)

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id'] == self.hotel_id,'name'].squeeze()
    def check_availablity(self):
        available = df.loc[df['id'] == self.hotel_id,'available'].squeeze()
        if available == 'yes':
            return True
        else:
            return False
    def book(self):
        df.loc[df['id'] == self.hotel_id,'available'] = 'no'
        df.to_csv('hotels.csv',index=False)

class ReservationTicket:
    def __init__(self,customer_name,hotel):
        self.customer_name = customer_name
        self.hotel = hotel
    def generate_ticket(self):
        return f"""
        Thank you for your reservation!
        Here are your booking details:
        Name :{self.customer_name}
        Hotel :{self.hotel.hotel_name}
        """


hotel_id = input("enter hotel_id which you want to book :")
hotel = Hotel(hotel_id)
if hotel.check_availablity():
    name = input("Enter name :")
    hotel.book()
    reservationticket = ReservationTicket(name,hotel)
    print(reservationticket.generate_ticket())
else:
    print("room is not available")