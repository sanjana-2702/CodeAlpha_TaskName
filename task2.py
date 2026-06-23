# Hardcoded stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 130,
    "MSFT": 330
}

total = 0

# Input from user
stock_name = input("Enter Stock Name: ").upper()
quantity = int(input("Enter Quantity: "))

# Check if stock exists
if stock_name in stocks:
    total = stocks[stock_name] * quantity
    print("Total Investment Value =", total)
else:
    print("Stock not found!")

# Optional: Save result in a text file
file = open("portfolio.txt", "w")
file.write("Stock Name: " + stock_name + "\n")
file.write("Quantity: " + str(quantity) + "\n")
file.write("Total Investment Value: " + str(total))
file.close()