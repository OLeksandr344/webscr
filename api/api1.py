import requests
api_key = "9K64VypSpD92XQ8LBTyjAzjE3KIdkXaUPybZZbrn"
park_code = "yell"
url = f"https://developer.nps.gov/api/v1/parks?parkCode={park_code}&api_key={api_key}"
response = requests.get(url)
data = response.json()
total_results = int(data["total"])
if total_results > 0:
    park = data["data"][0]
    park_name = park["fullName"]
    park_description = park["description"]
    park_hours = park["operatingHours"][0]["standardHours"]
    park_directions = park["directionsInfo"]
    park_url = park["url"]
    print(f"Park Name: {park_name}")
    print(f"Description: {park_description}")
    print("Operating Hours:")
    for day, hours in park_hours.items():
        print(f"{day}: {hours}")
    print(f"Directions: {park_directions}")
    print(f"Website: {park_url}")

