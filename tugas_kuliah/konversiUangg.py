"""
    Nama : Pancaran Ratna M
    IF 22 A
    0102522027
"""

def convert_currency(amount, currency):
    if currency == 'rupee':
        return amount * 74.15  # 1 USD = 74.15 INR (as of September 2021)
    elif currency == 'yen':
        return amount * 109.69  # 1 USD = 109.69 JPY (as of September 2021)
    elif currency == 'baht':
        return amount * 33.51   # 1 USD = 33.51 THB (as of September 2021)
    elif currency == 'krw':
        return amount * 1174.50   # 1 USD = 1174.50 KRW (as of September 2021)
    elif currency == 'pesso':
        return amount * 0.0090 # pesso
    else:
        return 'Invalid currency'


amount = float(input("Enter amount in USD: ")) 
currency = input("Enter currency to convert to (rupee/yen/baht/pesso/krw): ")

result = convert_currency(amount, currency)

if isinstance(result, str):
    print(result)
else:
    print(f"{amount} USD is equal to {result} {currency.upper()}")




 