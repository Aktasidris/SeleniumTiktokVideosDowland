from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
from urllib.request import urlopen
from selenium.webdriver.common.by import By

#enter your tags and run the code wait to complate dowland videos
tags = "#party#night"
print("STEP 1: Open Chrome browser")
driver = webdriver.Chrome()
driver.get("https://www.tiktok.com")# Change the tiktok link
time.sleep(1)

searchbar = driver.find_element(By.CLASS_NAME, "e14ntknm3")
searchbar.send_keys(tags)
clickbutton = driver.find_element(By.CLASS_NAME, "e14ntknm7")
clickbutton.click()
time.sleep(3)
def downloadVideo(link, id):
    cookies = {
        '_gid': 'GA1.2.398338000.1693434852',
        '__cflb': '0H28v8EEysMCvTTqtuFFMWyYEmbm6aBg9NhdQ6RhJ5b',
        '_gat_UA-3524196-6': '1',
        '_ga': 'GA1.2.1912221511.1693434852',
        '_ga_ZSF3D6YSLC': 'GS1.1.1693434851.1.1.1693435103.0.0.0',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/tr',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/tr',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Opera GX";v="101", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Campaign 34)',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'tr',
        'tt': 'a1J4UzFk',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    dowlandsoup = BeautifulSoup(response.text,"html.parser")
    dowlandlink = dowlandsoup.a["href"]
    mp4File = urlopen(dowlandlink)
    with open(f"videos/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

soup = BeautifulSoup(driver.page_source, "html.parser")
videos = soup.find_all("div",{"class": "e1cg0wnj1"})
print(len(videos))
for index,video in enumerate(videos):
    downloadVideo(video.a["href"],index)
    time.sleep(10)
# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
# to 60 seconds, just enough time for you to complete the captcha yourself.

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break