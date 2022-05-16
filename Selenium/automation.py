from sys import set_coroutine_origin_tracking_depth
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
timeout = 5
chrome_browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
#  chrome_browser.maximize_window()
# Go to the website
chrome_browser.get('https://www.amazon.ca/')
# Make sure that we are in the website 
assert 'Amazon.ca: Low Prices – Fast Shipping – Millions of Items' in chrome_browser.title
# Get the search bar and clear the search bar
search_bar = chrome_browser.find_element(By.ID, 'twotabsearchtextbox')
search_bar.clear()
# Get the search button
search_button =  chrome_browser.find_element(By.ID, 'nav-search-submit-button')  
# Set the text 
search_bar.send_keys('Sending Keys')
# Simulate click search 
search_button.click()
