
def convert_currency(amount, currency):
    if currency == 'rupee':
        return amount * 74.15  # 1 USD = 74.15 INR (as of September 2021)
    elif currency == 'yen':
        return amount * 109.69  # 1 USD = 109.69 JPY (as of September 2021)
    elif currency == 'baht':
        return amount * 33.51   # 1 USD = 33.51 THB (as of September 2021)
    elif currency == 'krw':
        return amount * 1174.50   # 1 USD = 1174.50 KRW (as of September 2021)
    else:
        return 'Invalid currency'

amount = float(input("Enter amount in USD: "))
currency = input("Enter currency to convert to (rupee/yen/bah/krw): ")

result = convert_currency(amount, currency)

if isinstance(result, str):
    print(result)
else:
    print(f"{amount} USD is equal to {result} {currency.upper()}")
    
    # klo ke Indo b 0.005557763 rupee
# klo ke yen 0.0090231608 
