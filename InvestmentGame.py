#Hoofdcode voor de InvestmentGame, vanuit deze code worden alle andere codes aangeroepen.
import pandas as pd
from InvestmentGame.order import Order
from InvestmentGame.User import User
from InvestmentGame.retrieve_data import get_price
from InvestmentGame.balance_changes import update_balance
df = pd.read_csv("InvestmentGame/data_modified.csv")

#Aanroepen van de user

user = input("Do you already have an account? (y/n)")
if user == "n":
    user_name = input("What is your name?")
    currency = input("What is your preferred currency?")
    balance = int(input("What is your starting balance?"))
    user = User(user_name, currency, balance)
    userlist = {"user_name": user_name, 'currency': currency, 'balance': balance}
    df = df.append(userlist, ignore_index=True)
    df.set_index('user_name', inplace=True)
    print(df)
    df.to_csv("InvestmentGame/data_modified.csv")
elif user == "y":
    user_name = input("Please provide your user_name.")
    retrieve_user_info = df[df['user_name'] == user_name]
    user_name = retrieve_user_info.iloc[0]["user_name"]
    currency = retrieve_user_info.iloc[0]["currency"]
    balance = retrieve_user_info.iloc[0]["balance"]
    user = User(user_name, currency, balance)
else:
    print("Invalid input, please check your input.")


ordertype = ""
order_id = 0
wantorder = input("You want to make an order? (y/n)")
if wantorder == "y":
    ordertype = input("Do you want to place a buy or a sell order?")
    order_id = order_id + 1
    if ordertype == "buy":
        time = input("What is the date of the order? Please provide in the following format YYYY-MM-DD")
        amount = input("How many stocks do you want to buy?")
        symbol = input("What is the symbol of the stock you want to buy?")
        status = "open"
        price = get_price(symbol, time).values
        value = int(price) * int(amount)
        order = Order(order_id, time, amount, symbol, status, ordertype, price, value)
        user.add_portfolio(symbol, amount)
        user.update_orderlist(wantorder, order_id, ordertype, symbol, time, amount, price, value)
        # df = df.loc[user_name, 'orders'] = ['5']
        # df = df.loc[user_name, 'portfolio'] = ['5']
        print(df)
        print("New Balance: " + str(update_balance(ordertype, balance, value)))
        print(user.orders)
        print(user.portfolio)
    elif ordertype == "sell":
        time = input("What is the date of the order? Please provide in the following format YYYY-MM-DD")
        amount = input("How many stocks do you want to sell?")
        symbol = input("What is the symbol of the stock you want to sell?")
        status = "open"
        price = get_price(symbol, time).values
        value = int(price) * int(amount)
        order = Order(order_id, time, amount, symbol, status, ordertype, price, value)
        user.add_portfolio(symbol, amount)
        user.update_orderlist(wantorder, order_id, ordertype, symbol, time, amount, price, value)
        print("New Balance: " + str(update_balance(ordertype, balance, value)))
        print(user.orders)
        print(user.portfolio)
    else:
        print ("This is not an valid ordertype")
elif wantorder == "n":
    print("Maybe next time")
else:
    print("This is not a valid answer")

