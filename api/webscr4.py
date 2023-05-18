import requests
def get_global_covid_data():
    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
def get_country_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
global_data = get_global_covid_data()
if global_data:
    print("Global COVID-19 Data:")
    print(f"Cases: {global_data['cases']}")
    print(f"Deaths: {global_data['deaths']}")
    print(f"Recovered: {global_data['recovered']}")
country = "Ukraine"
country_data = get_country_covid_data(country)
if country_data:
    print(f"\nCOVID-19 Data for {country}:")
    print(f"Cases: {country_data['cases']}")
    print(f"Deaths: {country_data['deaths']}")
    print(f"Recovered: {country_data['recovered']}")
    print(f"Active Cases: {country_data['active']}")
