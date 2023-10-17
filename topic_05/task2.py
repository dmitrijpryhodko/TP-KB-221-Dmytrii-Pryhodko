import requests
response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")
for currency in response.json():
    if currency["cc"] == "EUR":
        euro = currency["rate"]
    elif currency["cc"] == "USD":
        usd = currency["rate"]
    elif currency["cc"] == "PLN":
        pln = currency["rate"]
amount = float(input("Введіть кількість валюти: "))
currtype = input("Введіть тип валюти (EUR, USD, PLN): ").upper()
if currtype == "EUR":
    converted_amount = amount * euro
    currname = "євро"
elif currtype == "USD":
    converted_amount = amount * usd
    currname = "доларів США"
elif currtype == "PLN":
    converted_amount = amount * pln
    currname = "польських злотих"
else:
    print("Некоректний ввід")
print(f"{amount} {currname} дорівнює {converted_amount:.2f} гривням.")

