from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

html = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text().replace("\n\n", ""))
print(soup.find_all("img"))
image1, image2 = soup.find_all("img")

print("HTML tag is " + image1.name + ", attribute value is " + image1["src"])
print("Title is " + soup.title.string)