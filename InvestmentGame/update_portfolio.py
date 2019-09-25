def update_portfolio(ordertype,number,symbol)
    if ordertype == "buy":
            #add stock to the portfolio
        fund_symbol = symbol
        fund_name = "MSFT"
        aantal = number
        value = number*price

        return portfolio = Portfolio(fund_symbol, fund_name, aantal, value)

    elif ordertype == "sell":
            #remove stock from the portfolio

    else:
        return "Order type not known"

