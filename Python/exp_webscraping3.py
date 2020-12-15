import mechanicalsoup

url = "http://olympus.realpython.org/login"

browser = mechanicalsoup.Browser()
page = browser.get(url)
html = page.soup

form = html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, page.url)
print(profiles_page.url)