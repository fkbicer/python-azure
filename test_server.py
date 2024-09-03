import requests

# Azure App Service URL'nizi buraya yapıştırın
url = "https://furkan-deneme-bdamabgybcd0huge.westeurope-01.azurewebsites.net"

# GET isteği gönderin
response = requests.get(url)

# Yanıtı ekrana yazdırın
print(response.status_code)  # HTTP durum kodunu yazdırır
print(response.json())       # JSON yanıtını yazdırır (eğer JSON ise)