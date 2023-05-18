import requests
def fetch_robots_txt(url):
    robots_url = url + "/robots.txt"
    response = requests.get(robots_url)
    print(response.text)
fetch_robots_txt("https://en.wikipedia.org")