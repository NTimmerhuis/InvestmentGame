


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

from InvestmentGame.order import Order
from InvestmentGame.User  import User
from InvestmentGame.retrieve_data import get_price

ordertype = ""
order = input("You want to make an order? (y/n)")
if order == "y":
    while order not in ("buy", "sell"):
        ordertype = input("buy or sell order?")
        if ordertype == "buy":
            neworder = input("order_id, Time, amount, symbol, status")
            neworder= neworder.split(',')
            neworder.append(ordertype)
            price = get_price(neworder[3], neworder[1])
            neworder.append(price)
            order = Order(*neworder)
            User.orders.append(order)
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

