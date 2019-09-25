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


ordertype = ""
order = input("You want to make an order? (y/n)")
if order == "y":
    while ordertype not in ("buy","sell"):
        ordertype = input("buy or sell order?")
        if ordertype == "buy":
            newbuyorder = input("order_id, Time, price, amount, fund_name, status")
            newbuyorder = newbuyorder.split(',')
            newbuyorder.append(ordertype)
            order = Order(*newbuyorder)
            User.order.append(order)
        elif ordertype == "sell":
            newsellorder = input("ID, price, amount, fund_name")
        else:
            print ("This is not an valid ordertype")
elif order == "n":
    print("Maybe next time")
else:
    print("This is not a valid answer")

