#Hoofdcode voor de InvestmentGame, vanuit deze code worden alle andere codes aangeroepen.

from InvestmentGame.order import Order
from InvestmentGame.User import User

#Aanroepen van de user
#Wat nog kan worden toegevoegd is een echte database waar alle users in worden opgeslagen.
#Op dit moment begint de code elke keer weer met een lege lijst met users. Dit is voor later, niet nodig op dit moment.
#Daarom altijd n invullen op de eerste vraag.

users = []
user = input("Do you have a user_id? (y/n)")
if user == "y":
    user_id = input("Please provide your user_id.")
    #Hier moet later een database gekoppeld worden om user_id op te zoeken en de gegevens op te halen.
elif user == "n":
    user_name = input("What is your name?")
    currency = input("What is your preferred currency?")
    balance = int(input("What is your starting balance?"))
    new_user = User(user_name, currency, balance)
    users.append(new_user)
else:
    print("Invalid input, please check your input.")

<<<<<<< HEAD
=======
from InvestmentGame.order import Order
from InvestmentGame.user import User
from InvestmentGame.retrieve_data import get_price
>>>>>>> master

ordertype = ""
order = input("You want to make an order? (y/n)")
if order == "y":
    while order True:
        ordertype = input("buy or sell order?")
        if ordertype == "buy":
<<<<<<< HEAD
            newbuyorder = input("order_id, Time, price, amount, fund_name, status")
            newbuyorder = newbuyorder.split(',')
            newbuyorder.append(ordertype)
            order = Order(*newbuyorder)
=======
            neworder = input("order_id, Time, amount, symbol, status")
            neworder= neworder.split(',')
            neworder.append(ordertype)
            price = get_price(neworder[4], neworder[2])
            neworder.append(price)
            order = Order(*neworder)
>>>>>>> master
            User.order.append(order)
        elif ordertype == "sell":
            neworder = input("order_id, Time, amount, symbol, status")
            neworder = neworder.split(',')
            neworder.append(ordertype)
            order = Order(*newbuyorder)
            User.order.append(order)
        else:
            print ("This is not an valid ordertype")
elif order == "n":
    print("Maybe next time")
else:
    print("This is not a valid answer")

