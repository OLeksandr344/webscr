import requests
def check_page_availability(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Сторінка доступна")
    else:
        print("Сторінка недоступна")
# Приклад виклику функції
check_page_availability("https://www.data.gov")

