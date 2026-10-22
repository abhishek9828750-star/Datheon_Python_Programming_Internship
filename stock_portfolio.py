
import csv

portfolio = []

print("Stock Portfolio Performance Tracker")

while True:
    name = input("Enter stock name (or done to finish): ")

    if name.lower() == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per share: "))

        if quantity <= 0 or price < 0:
            print("Enter valid values.")
            continue

        portfolio.append({
            "Stock": name,
            "Quantity": quantity,
            "Price": price,
            "Total Value": quantity * price
        })

    except ValueError:
        print("Please enter valid numbers.")

total = sum(item["Total Value"] for item in portfolio)

print("\nPortfolio Summary")
for item in portfolio:
    print(item["Stock"], ":", item["Total Value"])

print("Total Portfolio Value:", total)

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Stock", "Quantity", "Price", "Total Value"]
    )
    writer.writeheader()
    writer.writerows(portfolio)

print("Portfolio saved successfully!")
