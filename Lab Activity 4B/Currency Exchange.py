import csv

# Load currency exchange rates from currency.csv
def load_exchange_rates(filename):
    exchange_rates = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            currency, rate = row
            exchange_rates[currency] = float(rate)
    return exchange_rates

# Convert USD to the desired currency
def convert_currency(amount, currency, rates):
    if currency in rates:
        return amount * rates[currency]
    else:
        return None

# Main program
filename = r"C:\Users\User\Documents\GitHub\IT0011-Activities\Lab Activity 4B\currency.csv"
exchange_rates = load_exchange_rates(filename)

# User input
usd_amount = float(input("How much dollar do you have? "))
target_currency = input("What currency you want to have? ").strip().upper()

# Conversion
converted_amount = convert_currency(usd_amount, target_currency, exchange_rates)

# Output result
if converted_amount is not None:
    print(f"\nDollar: {usd_amount} USD")
    print(f"{target_currency}: {converted_amount}")
else:
    print("Currency not found in exchange rates.")
