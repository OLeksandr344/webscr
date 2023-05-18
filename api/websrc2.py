import requests
def get_datasets_count():
    url = "https://catalog.data.gov/api/3/action/package_list"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dataset_count = len(data["result"])
        print(f"Кількість наборів даних на data.gov: {dataset_count}")
get_datasets_count()



