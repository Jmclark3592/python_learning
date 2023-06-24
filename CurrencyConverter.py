#currency converted

import re

currencies = {
    'USD' : 1,
    'EUR' : 1.09,
    'GBP' : 1.27
}

print("Available currencies: USD, EUR, GBP")
cash_query = input("Enter what currency you wish to convert to, your current currency and how much of the currency you have: ")

fragmented = cash_query.split()

