
# importing data

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&outputsize=full&apikey=demo")

# Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
# See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
if response.status_code != 200:
    raise ValueError("Could not retrieve data, code:", response.status_code)

# The service sends JSON data, we parse that into a Python datastructure
raw_data = response.json()

# Let's look at the raw data (it's a lot so let's limit it)
raw_data.keys()

# This we probably don't need
raw_data['Meta Data']


user = input("Do you have a user_id? (Yes/No)")
if user == "Yes":
    user_id = input("Please provide your user_id.")
    #Nu moeten we gaan zoeken in user.py en de informatie over de juiste user ophalen.
elif user == "No":
    user_name = input("What is your name?")
    currency = input("What is your preferred currency?")
    balance = input("What is your starting balance?")
    #Bovenstaande willen we toevoegen aan class users en nieuwe user_id maken, eerst volgende user1, user 2 etc.
else:
    print("Invalid input, please check your input.")

from InvestmentGame.order import Order
from InvestmentGame.user import User
from InvestmentGame.retrieve_data import get_price

ordertype = ""
order = input("You want to make an order? (y/n)")
if order == "y":
    while order True:
        ordertype = input("buy or sell order?")
        if ordertype == "buy":
            neworder = input("order_id, Time, amount, symbol, status")
            neworder= neworder.split(',')
            neworder.append(ordertype)
            price = get_price(neworder[4], neworder[2])
            neworder.append(price)
            order = Order(*neworder)
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

