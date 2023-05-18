import requests
def get_route(start_location, end_location, api_key):
    url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={start_location}&to={end_location}"
    response = requests.get(url)
    data = response.json()
    print("Початкова точка:", data["route"]["locations"][0]["latLng"])
    print("Кінцева точка:", data["route"]["locations"][1]["latLng"])
    for movement in data["route"]["legs"][0]["maneuvers"]:
        print(movement["narrative"])
start_location = "Kherson"
end_location = "Simferopol"
api_key = "If1fMm4WXPMjNzAFjUbQd0ie2I3BxVVG"
get_route(start_location, end_location, api_key)


