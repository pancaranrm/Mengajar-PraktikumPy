def currency_converter(amount, currency):
    rates = {'USD': 1, 'INR': 74.97, 'JPY': 110.84, 'THB': 32.99, 'KRW': 1174.50}
    converted_amount = round(amount / rates[currency], 2)
    return converted_amount

# ga pake if else

amount = float(input("Enter the amount to convert: "))
currency = input("Enter the currency (USD, INR, JPY, THB, KRW): ")

converted_amount = currency_converter(amount, currency)

print(f"{amount:.2f} {currency} is equal to {converted_amount:.2f} USD.")
