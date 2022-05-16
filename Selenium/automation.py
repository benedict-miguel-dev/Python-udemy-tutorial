from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')
print('Selenium Easy Demo' in chrome_browser.title)
# Closes the initial warm up message
close = chrome_browser.find_element_by_partial_link_text('No, thanks')

print(close)
