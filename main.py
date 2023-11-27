import pandas as pd


df = pd.read_csv("hotels.csv",dtype={"id":str})
df_cards = pd.read_csv('cards.csv',dtype=str).to_dict("records")
df_card_security = pd.read_csv('card_security.csv',dtype=str)
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
class SpaHotel(Hotel):
    def spa_book(self):
        pass

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
class SpaReservationTicket:
    def __init__(self,customer_name,hotel):
        self.customer_name = customer_name
        self.hotel = hotel
    def generate_ticket(self):
        return f"""
        Thank you for your SPA reservation!
        Here are your SPA booking details:
        Name :{self.customer_name}
        Hotel :{self.hotel.hotel_name}
        """
class Card:
    def __init__(self,number):
        self.number = number
    def validate_card(self,expiration,cvc,holder):
        card = {'number':self.number,'expiration': expiration, 'cvc': cvc,
                'holder': holder}
        if card in df_cards:
            return True

class SecureCard(Card):
    def authenticate(self,password):
        pwd = df_card_security.loc[df_card_security["number"]==self.number,'password'].squeeze()
        if pwd == password:
            return True
        else:
            return False



hotel_id = input("enter hotel_id which you want to book :")
hotel = SpaHotel(hotel_id)
if hotel.check_availablity():
    card = SecureCard("1234")
    if card.validate_card("12/26","123","JOHN WATTS"):
        if card.authenticate("mypass"):
            name = input("Enter name :")
            hotel.book()
            reservationticket = ReservationTicket(name,hotel)
            print(reservationticket.generate_ticket())

            spa = input("Do you want to book a spa package? ")
            if spa == "yes":
                hotel.spa_book()
                spa_ticket =SpaReservationTicket(name,hotel)
                print(spa_ticket.generate_ticket())


        else:
            print("card authentication failed")
    else:
        print("There was problem with your payment")
else:
    print("room is not available")