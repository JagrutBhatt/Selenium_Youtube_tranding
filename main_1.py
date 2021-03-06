import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import os
import json

Youtube_Tranding_Url = "https://www.youtube.com/feed/trending"


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def get_videos(driver):
    VIDEO_DIV_TAG = 'ytd-video-renderer'
    print('Fatching the page')
    driver.get(Youtube_Tranding_Url)
    print('get video divs')
    video_divs = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
    return video_divs


def parse_video(video):
    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text

    video_url = title_tag.get_attribute('href')

    thumbnail_Tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_Tag.get_attribute('src')

    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_div.text

    discription = video.find_element(By.ID, 'description-text').text

    return {
        'title': title,
        'Video_url': video_url,
        'thumbnail_url': thumbnail_url,
        'channel_name': channel_name,
        'discription': discription
    }

def send_email(body):
  gmail_user = 'emailformpython@gmail.com'

  try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    

    SENDER_EMAIL = 'emailformpython@gmail.com'
    RECIVER_EMAIL = 'emailformpython@gmail.com', 'jagrutmbhatt@gmail.com'
    subject = 'Top-10 Tranding videos on youtube'
    

    email_text = f"""
    From: {SENDER_EMAIL}
    To: {RECIVER_EMAIL}
    Subject: {subject}
    {body}
    """ 

    gmail_password = os.environ['GMAIL_PASSWORD']

    server_ssl.login(SENDER_EMAIL, gmail_password)
    server_ssl.sendmail(SENDER_EMAIL, RECIVER_EMAIL , email_text)
    server_ssl.close()

  except:
      print ('Something went wrong...')


if __name__ == "__main__":
    print("Creating driver")
    driver = get_driver()
    videos = get_videos(driver)
    print(f'Found {len(videos)} Videos')

    print("Parsing the top 10 video")
    # title, url , thumbnail_url, channel, views, uploadded,discription
    video = videos[0]
    video_data = [parse_video(video) for video in videos[:10]]

    print("save data to csv file using pandas")
    video_df = pd.DataFrame(video_data)
    print(video_df)

    video_df.to_csv('tranding.csv', index=None)

    print('send an email with result')

    body = json.dumps(video_data,indent = 4)
    send_email(body)
