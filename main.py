import requests
from bs4 import BeautifulSoup
# to create headless browser
import selenium


Youtube_Tranding_Url = "https://www.youtube.com/feed/trending"

response = requests.get(Youtube_Tranding_Url)

print('status code',response.status_code)

with open('tranding.html','w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text,'html.parser')

print('Page title',doc.title.text)

#find all video divs
video_divs = doc.find_all('div', class_ = "ytd-video-renderer")

print(F'Found {len(video_divs)} Videos')
