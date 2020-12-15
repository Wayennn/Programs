from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
html = page.read().decode("utf-8")

tags = {"title":""}

for i in tags:
    pattern = "<.*?" + i + ".*?>.*?<.*?/.*?" + i + ".*?>"
    tg = re.search(pattern, html, re.IGNORECASE)
    if tg:
        tags[i] = re.sub("<.*?>", "", tg.group())
    else:
        tags[i] = None

for i, j in tags.items():
    print(i + " is " + str(j))

f1_sindex = html.find("Name:")
f1_eindex = f1_sindex + len("Name:")
f2_sindex = html.find("Favorite Color:")
f2_eindex = f2_sindex + len("Favorite Color:")
print(html[f1_sindex:f1_eindex])
print(html[f2_sindex:f2_eindex])