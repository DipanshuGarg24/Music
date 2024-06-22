from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from new import  *

class Scrapper:
    def __init__(self):
        option = Options()
        option.add_argument("--headless")
        self.driver = webdriver.Chrome(options=option)
        self.audioScrap = AudioScrap()
    def FetchLinks(self,keyword):
        search_url = f"https://www.youtube.com/results?search_query={keyword}"
        self.driver.get(search_url)
        time.sleep(3)

        #
        links = []
        video_elements = self.driver.find_elements(by="id",value="video-title")
        # print(video_elements)
        c = 0
        for element in video_elements:
            x = element.get_attribute("href")
            if x:
                y = element.get_attribute("title")
                x = self.audioScrap.stream_audio(x)
                z = [x, y]
                links.append(z)


        return links

    def close(self):
        self.driver.quit()


# keyword = "shma kahe parwane se dur chla jaye song"
# scrapper= Scrapper()
# video_links = scrapper.FetchLinks(keyword)
#
# if video_links:
#     print("YouTube Video Links:")
#     for link in video_links:
#         print(link)
