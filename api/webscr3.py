import requests
def get_latest_dataset_name():
    url = "https://catalog.data.gov/api/3/action/package_search"
    params = {
        "sort": "metadata_created desc",
        "rows": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["result"]["count"] > 0:
            latest_dataset = data["result"]["results"][0]
            dataset_name = latest_dataset["title"]
            print(f"Ім'я останнього доданого набору даних: {dataset_name}")
get_latest_dataset_name()
