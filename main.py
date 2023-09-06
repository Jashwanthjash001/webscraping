import requests
from bs4 import BeautifulSoup

url = "https://whatweekisit.com/"

response = requests.get(url)
class example1():
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    from pdb import set_trace
    set_trace()

    page_title = soup.title.string
    print("Page Title:", page_title)

    links = soup.find_all("a")
    for link in links:
        print("Link:", link.get("href"))
else:
    print("Failed to retrieve the web page. Status Code:", response.status_code)
