exchanges = {
    "USD": {"EUR": 0.85, "GBP": 0.73},
    "EUR": {"USD": 1.18, "GBP": 0.86},
    "GBP": {"USD": 1.37, "EUR": 1.16}
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    if from_currency in exchanges and to_currency in exchanges[from_currency]:
        rate = exchanges[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount

    return "Currency conversion not supported."

amount_str = input("Enter the amount (e.g., $100.00): ")
from_currency = input("Enter the source currency (e.g., USD, EUR, GBP): ").upper()
to_currency = input("Enter the target currency (e.g., USD, EUR, GBP): ").upper()

try:
    # Extract the numeric part of the amount string and convert it to float
    amount = float(amount_str.replace('$', ''))
except ValueError:
    print("Invalid amount format.")
    exit(1)

if from_currency not in exchanges or to_currency not in exchanges:
    print("Invalid currency code.")
else:
    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount_str} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
