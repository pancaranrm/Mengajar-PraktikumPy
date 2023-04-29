"""
    Nama : Pancaran Ratna M
    NIM : 0102522027
    IF-22'A
    Tugas : Konversi mata uang
"""

def currency_converter(amount, from_currency, to_currency):
    '''
    Convert amount from one currency to another.
    Supported currencies: USD, INR, JPY, THB
    '''
    # Conversion rates as of 2021-09-01
    conversion_rates = {'USD': 1, 'INR': 0.014, 'JPY': 0.0091, 'THB': 0.031}

    # Convert from_currency to USD
    amount_in_usd = amount / conversion_rates[from_currency]

    # Convert from USD to to_currency
    converted_amount = amount_in_usd * conversion_rates[to_currency]

    return converted_amount

# Example usage:
usd_amount = 100
inr_amount = currency_converter(usd_amount, 'USD', 'INR')
jpy_amount = currency_converter(usd_amount, 'USD', 'JPY')
thb_amount = currency_converter(usd_amount, 'USD', 'THB')

print(f'{usd_amount} USD = {inr_amount:.2f} INR')
print(f'{usd_amount} USD = {jpy_amount:.2f} JPY')
print(f'{usd_amount} USD = {thb_amount:.2f} THB')
