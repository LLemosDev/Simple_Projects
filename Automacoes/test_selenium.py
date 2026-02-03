from selenium import webdriver
from time import sleep
# Use this below when it comes to dynamic pages, when you have to wait until the
# element is clickable 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium uses a Webdriver from your browser to control the tab
browser = webdriver.Chrome() # Open browser

wait = WebDriverWait(browser, 10)

# Full screen
browser.maximize_window()

# Search something in web, Open a website
browser.get("https://www.edx.org/")

# find element in screen
# In find_element() we can specify the search type
# 1 param - specify search type, 2nd - value
button = browser.find_element('id', 'mega-nav-button')

# Click in the element
button.click()

# Search with XPath - more accurate, nodes search 
# Used to search elements without id, class or name or when tailwind appears
topic = wait.until(
    EC.element_to_be_clickable(("xpath", "//a[contains(text(), 'Data analysis & statistics')]")))

topic.click()

# Finding element by href link
course = wait.until(
    EC.element_to_be_clickable(
        ('xpath', "//a[contains(@href, 'harvardx-computer-science-for-databases-using-sql')]")
        ))

course.click()

# Footer button, does'nt appear in screen
button_home = browser.find_element("xpath", "//a[contains(@class, 'mb-6') and .//img[contains(@title, 'edX homepage')]]")

# Scroll to an element. Script is a code in Js
browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", button_home)
wait.until(EC.element_to_be_clickable(button_home))   # Wait js script
button_home.click()

sleep(5)

# Search with Xpath using href and link as param
sign_in = browser.find_element("xpath", "//a[contains(@href, 'https://authn.edx.org/login')]")
sign_in.click()

# Write in forms - Wait the dynamic page
input_name = wait.until(
    EC.element_to_be_clickable(("id", "emailOrUsername")))

input_name.send_keys("TesteUser")

browser.find_element("id", "password").send_keys("senhateste")

# Login button
browser.find_element("id", "sign-in").click()

sleep(10)