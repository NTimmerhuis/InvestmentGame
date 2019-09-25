
#Deze code maakt een update van de balance van de user.

def update_balance(ordertype, balance, value):
    if ordertype == "sell":
        return balance + value
    elif ordertype == "buy":
        return balance - value
    else:
        print("Ordertype is unknown.")


