import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from wb_pro.items import WbProItem
import random


class WbSpiderSpider(scrapy.Spider):
    name = "wb_spider"
    allowed_domains = ["weibo.com"]
    start_urls = ["https://weibo.com/"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = webdriver.ChromeOptions()
        options.add_argument('--dns-server=8.8.8.8')
        self.browser = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'),
                                        options=options)

    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(2)
        scroll_distance = 12000
        self.browser.execute_script("window.scrollBy(0, " + str(scroll_distance) + ");")
        count = 0
        stop = 250
        use_set = set()
        items = WbProItem()
        bug = 0
        while True:
            data_items = self.browser.find_elements(By.XPATH, "//*[@id='scroller']/div[1]/div")
            for data in data_items:
                try:
                    # regain link element
                    detail_link = data.find_element(By.XPATH, ".//a[@class='ALink_default_2ibt1']")
                    # click on detail
                    detail_link.click()
                    time.sleep(3)
                    user = self.browser.find_element(By.XPATH, '//div[@class="ProfileHeader_name_1KbBs"]').text.strip()
                    print(user)
                    if user in use_set:
                        self.logger.info("already exist")
                        bug += 1
                    else:
                        fansCount = self.browser.find_element(By.XPATH,
                                                              '//div[@class="woo-box-flex woo-box-alignCenter ProfileHeader_h4_gcwJi"]/a[1]/span/span').text.strip()
                        followCount = self.browser.find_element(By.XPATH,
                                                                '//div[@class="woo-box-flex woo-box-alignCenter ProfileHeader_h4_gcwJi"]/a[2]/span/span').text.strip()
                        transferCount = self.browser.find_element(By.XPATH,
                                                                  '//div[@class="woo-box-flex woo-box-alignCenter ProfileHeader_h4_gcwJi"]/a[3]/span/span').text.strip()
                        self.logger.info(f"{user}, {fansCount}, {followCount}, {transferCount}")
                        use_set.add(user)
                        items['user'] = user
                        items['fansCount'] = fansCount
                        items['followCount'] = followCount
                        items['transferCount'] = transferCount
                        yield items
                        count += 1
                        self.browser.back()
                        time.sleep(2)
                        time.sleep(round(random.uniform(1, 3), 1))
                        if count == stop or bug == 10:
                            break
                except Exception as e:
                    pass

        self.browser.quit()
