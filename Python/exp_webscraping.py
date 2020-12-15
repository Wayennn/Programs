from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

tag = {"title":"", "head":"", "html":"", "body":""}
for i in tag:
    tag_startindex = html.find("<" + i + ">") + len("<" + i +">")
    tag_endindex = html.find("</" + i + ">")
    tag[i] = html[tag_startindex:tag_endindex]

for i, j in tag.items():
    print(i + " is " + j)