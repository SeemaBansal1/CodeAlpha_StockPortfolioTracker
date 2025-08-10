# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 410,
    "GOOG": 140,
    "AMZN": 130
}

def main():
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: ${price}")

    portfolio = {}
    while True:
        stock = input("Enter stock symbol (e.g., AAPL) or press Enter to finish: ").upper()
        if stock == "":
            break
        if stock not in STOCK_PRICES:
            print("Invalid stock symbol. Please choose from the available stocks.")
            continue
        
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty < 0:
                print("Quantity can't be negative.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty

    # Calculate total investment
    total_investment = 0
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        investment = qty * STOCK_PRICES[stock]
        print(f"{stock}: {qty} x ${STOCK_PRICES[stock]} = ${investment}")
        total_investment += investment

    print(f"\nTotal Investment: ${total_investment}")

    # OPTIONAL: Save to file
    save = input("Would you like to save your portfolio to a file? (y/n): ").lower()
    if save == "y":
        filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ")
        try:
            with open(filename, "w") as f:
                f.write("Stock,Quantity,Price,Investment\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock},{qty},{STOCK_PRICES[stock]},{qty * STOCK_PRICES[stock]}\n")
                f.write(f"\nTotal Investment,,,{total_investment}\n")
            print(f"Portfolio saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
