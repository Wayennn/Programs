from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# you can delete this portion so that you will see the actual browser being opened
options = Options()
options.headless = True

# the chrome driver, please edit the path so that it points to where your chrome driver is located
chromedriver_address = r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_address, options=options)

# the url of the website you want to visit
driver.get("https://www.messenger.com/")

#login credentials
email_address = "nwariston@gmail.com" # type here the entire string of your username
password = "KY50TSKYF0TG" # type here the entire string of your password

# this is how the program gets the input fields and types in your credentials, submitting them right after
email = driver.find_element_by_id("email")
email.send_keys(email_address)
passw = driver.find_element_by_id("pass")
passw.send_keys(password)
passw.submit()

fbid = "https://www.messenger.com/t/"

# this is the fbid of the person you want to send messages to, copy paste from the url on the search bar
fbidname = "altair.egos"
fbid += fbidname

# this finds the thumbnail of the person you want to send messages to
# the thumbnail must be within the topmost 5 chat thumbnails for the program to find it
# or else, it raises an "ElementNotFound" exception
driver.find_element_by_xpath("//a[@data-href='{}']".format(fbid)).click()
# I suggest, you chat sir arvin first to bring your conversation up top

# this is how the program looks for the typing field
try:
    int(fbidname)
    tm = "Type a message, @name..."
except ValueError:
    tm = "Type a message..."

# this works only for personal messages, not in group chats, the label is different
type_message = driver.find_element_by_xpath("//div[@aria-label='{}']".format(tm))

type_message.click()

# everything that follows is self explanatory

primes = []
with open("Files\primes-to-1000k.txt", "r") as file:
    for lines in file.readlines():
        primes.append(int(lines))

type_message.send_keys("Hello Altair\n")
time.sleep(5) # I put sleep time to make sure that messenger won't acuse me of hacking behavior
for i in primes:
    type_message.click()
    type_message.send_keys(str(i) + "\n")
    time.sleep(2)
    
time.sleep(10)
driver.close() #always, always close the driver