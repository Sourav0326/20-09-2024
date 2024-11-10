def list_countries():
    return "india", "USA", "Germany", "Australia"


def capital_of(country):
    capitals = {
        "india": "New delhi",
        "USA": "Washington, D.C.",
        "Germany": "Berlin",
        "Australia": "Canberra"
    }
    return capitals.get(country,"unknown")


countries = list_countries()

for country in countries:
    capital = capital_of(country)
    print(f"the capital of {country} is {capital}.")
