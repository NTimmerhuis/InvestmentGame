from InvestmentGame.order import Order
order_nr = 1
ordertype = ""
order = input("You want to make an order? (y/n)")
if order == "y":
    while ordertype not in ("buy","sell"):
        ordertype = input("buy or sell order?")
        if ordertype == "buy":
            newbuyorder = input("Time, price, amount, fund_name, status")
            newbuyorder= newbuyorder.split(",")
            newbuyorder.append(ordertype)
            order_nr = Order(newbuyorder)
            order_nr += 1
        elif ordertype == "sell":
            newsellorder = input("ID, price, amount, fund_name")
        else:
            print ("This is not an valid ordertype")
elif order == "n":
    print("Maybe next time")
else:
    print("This is not a valid answer")

