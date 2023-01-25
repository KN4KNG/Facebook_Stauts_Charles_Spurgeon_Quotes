#supported in Win10 Whereas the working directory is C:\Selenium
#cookies must be exported to start and at each cookie expiration
#cookies name: facebook_cookies.pkl saved in selenium directory

from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import requests
from bs4 import BeautifulSoup
import random

# send a GET request to the website
response = requests.get("https://www.brainyquote.com/authors/charles-spurgeon-quotes")

# parse the HTML content of the website
soup = BeautifulSoup(response.content, "html.parser")

# find all the quote elements
quote_elements = soup.find_all("a", class_="oncl_q")

# select a random quote element
random_quote = random.choice(quote_elements)

# extract the text from the quote element
quote_text = random_quote.get_text()

# print the quote text
#print(quote_text)

driver = webdriver.Chrome()
# first visit home page
url = "https://www.facebook.com"
driver.get(url)

# delete the current cookies
driver.delete_all_cookies()

# add cookies from pickled-txt or a txt file
cookies = pickle.load(open("facebook_cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

# visit again and you shall see your account logged in
url = "https://www.facebook.com"
driver.get(url)

sleep(2)

element = driver.find_element_by_xpath("//div[@class='x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe xi81zsa']//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6']")
element.click()

string = (quote_text + ' - Charles Spurgeon')

sleep(2)

element = driver.find_element_by_xpath("//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
element.send_keys(string)

sleep(2)

element = driver.find_element_by_xpath("//div[@aria-label='Post']//div[@class='x6s0dn4 x78zum5 xl56j7k x1608yet xljgi0e x1e0frkt']")
element.click()
