#Hoofdcode voor de InvestmentGame, vanuit deze code worden alle andere codes aangeroepen.

<<<<<<< HEAD
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
=======


#
# user = input("Do you have a user_id? (Yes/No)")
# if user == "Yes":
#     user_id = input("Please provide your user_id.")
#     #Nu moeten we gaan zoeken in user.py en de informatie over de juiste user ophalen.
# elif user == "No":
#     user_name = input("What is your name?")
#     currency = input("What is your preferred currency?")
#     balance = input("What is your starting balance?")
#     #Bovenstaande willen we toevoegen aan class users en nieuwe user_id maken, eerst volgende user1, user 2 etc.
# else:
#     print("Invalid input, please check your input.")
>>>>>>> master

<<<<<<< HEAD
=======
from InvestmentGame.order import Order
from InvestmentGame.User  import User
from InvestmentGame.retrieve_data import get_price
>>>>>>> master

ordertype = ""
order = input("You want to make an order? (y/n)")
if order == "y":
    while order not in ("buy", "sell"):
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
            price = get_price(neworder[3], neworder[1])
            neworder.append(price)
            order = Order(*neworder)
<<<<<<< HEAD
>>>>>>> master
            User.order.append(order)
=======
            User.orders.append(order)
>>>>>>> master
        elif ordertype == "sell":
            neworder = input("order_id, Time, amount, symbol, status")
            neworder = neworder.split(',')
            neworder.append(ordertype)
            price = get_price(neworder[3], neworder[1])
            order = Order(*neworder)
            User.orders.append(order)
        else:
            print ("This is not an valid ordertype")
elif order == "n":
    print("Maybe next time")
else:
    print("This is not a valid answer")

