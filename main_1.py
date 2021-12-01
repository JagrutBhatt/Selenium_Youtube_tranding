from selenium import webdriver
from selenium.webdriver.chrome.options import Options

Youtube_Tranding_Url = "https://www.youtube.com/feed/trending"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')



driver = webdriver.Chrome(options=chrome_options)

driver.get(Youtube_Tranding_Url)

print('Page title:',driver.title)