from bs4 import BeautifulSoup
import requests

#page = requests.get("https://www.setopati.com/")
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")


# print(page)
# print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
