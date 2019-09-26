#Hoofdcode voor de InvestmentGame, vanuit deze code worden alle andere codes aangeroepen.
import pandas as pd
from InvestmentGame.order import Order
from InvestmentGame.User import User
from InvestmentGame.retrieve_data import get_price
from InvestmentGame.balance_changes import update_balance
df = pd.read_csv("InvestmentGame\data.csv")

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
    userlist = {"user_name": user_name, 'currency': currency, 'balance': balance}
    df = df.append(userlist, ignore_index=True)
    df.set_index('user_name')
    print(df)
    #df2.loc[user_name, 'currency'] = currency

    #print(df2)

else:
    print("Invalid input, please check your input.")


ordertype = ""
wantorder = input("You want to make an order? (y/n)")
if wantorder == "y":
    ordertype = input("buy or sell order?")
    if ordertype == "buy":
        order_id = input("order_id?")
        time = input("time?")
        amount = input("What amount ?")
        symbol = input("what symbol?")
        status = "open"
        price = get_price(symbol, time).values
        value = int(price) * int(amount)
        order = Order(order_id, time, amount, symbol, status, ordertype, price, value)
        new_user.update_portfolio(symbol, amount, ordertype)
        users.append(order)
    elif ordertype == "sell":
        order_id = input("order_id?")
        time = input("time? YYYY-MM-DD")
        amount = input("What amount ?")
        symbol = input("what symbol?")
        status = "open"
        price = get_price(symbol, time).values
        value = int(price) * int(amount)
        order = Order(order_id, time, amount, symbol, status, ordertype, price, value)
        new_user.update_portfolio(symbol, amount, ordertype)
        users.append(order)
    else:
        print ("This is not an valid ordertype")
elif wantorder == "n":
    print("Maybe next time")
else:
    print("This is not a valid answer")

print("New Balance: " + str(update_balance(ordertype, balance, value)))
print(new_user.portfolio)
print(Dataframe)