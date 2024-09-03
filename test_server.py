import requests

response = requests.get("http://furkan-deneme-bdamabgybcd0huge.westeurope-01.azurewebsites.net/")
print(response.json())