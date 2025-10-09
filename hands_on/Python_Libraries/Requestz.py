import requests
response = requests.get('https://www.autogiz.com/ke/car-prices/')  # Send a request to the Chief Elder of Autogizclear
print(f"The Chief Elder says: {response.status_code}")  # Ask the elder for their 200 OK) 
print(response.text)  # Ask the elder for their wisdom (the content of the response)   