from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


Youtube_Tranding_Url = "https://www.youtube.com/feed/trending"
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

def get_videos(driver):
  VIDEO_DIV_TAG ='ytd-video-renderer'
  print('Fatching the page')
  driver.get(Youtube_Tranding_Url)
  print('get video divs')
  video_divs = driver.find_elements(By.TAG_NAME,VIDEO_DIV_TAG)
  return video_divs
  
if __name__ == "__main__":
  print("Creating driver")
  driver = get_driver()
  videos = get_videos(driver)
  print(f'Found {len(videos)} Videos')

  print("Parsing the 1st video")
# title, url , thumbnail_url, channel, views, uploadded,discription
  video = videos[0]
  title_tag = video.find_element(By.ID,'video-title')
  title = title_tag.text
  video_url = title_tag.get_attribute('href')
  print(title,video_url)
  

  
  

  

