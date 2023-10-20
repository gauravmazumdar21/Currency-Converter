import requests
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Set API Endpoint, access key, and required parameters
# API Provider https://app.abstractapi.com/
access_key = "c9d4029c333b4ee3b049aedea1027865"
from_currency = input("Enter the currency you want to convert from: ")
to_currency = input("Enter the currenct you want to convert to: ")
amount = input("Enter Ammount: ")

response = requests.get(f"https://exchange-rates.abstractapi.com/v1/live/?api_key={access_key}&base={from_currency}&target={to_currency}")

# Get the JSON data from the response
info = json.loads(response.content)

# conversion result
converted_currency = float(amount) * float(info['exchange_rates'][to_currency])

print(amount, from_currency, "is equal to", converted_currency, to_currency)