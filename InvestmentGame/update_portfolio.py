def update_portfolio(ordertype,number,symbol):
    if ordertype == "buy":
            #add stock to the portfolio
        user.portfolio[symbol] += number
            return user.portfolio

    elif ordertype == "sell":
            #remove stock from the portfolio
        user.portfolio[symbol] -= number

    else:
        return "Order type not known"