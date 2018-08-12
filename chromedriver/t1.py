# -- coding : utf-8 --

import os
import time
from selenium import webdriver

class chrome_driver() :

    def __init__(self) :
        self.driver = webdriver.Edge(executable_path=r"D:\tools\application\MicrosoftWebDriver.exe")

    def exit_web(self,wtime) :
        if input() :
            # self.driver.close()
            self.driver.quit()

    def visit_web(self,website) :
        self.driver.get(website)
        print(self.driver.current_url)

    def edit_web(self,xpath = None,sdstr = "") :
        self.driver.find_element_by_xpath(xpath).send_keys(sdstr)

    def click_web(self, xpath = None) :
        print(self.driver.current_url)
        self.driver.find_element_by_xpath(xpath).click()
        # windows_num = driver.window_handles.index(driver.current_window_handle)
        self.driver.switch_to_window(self.driver.window_handles[-1])

    def build_driver(self) :
        # self.driver = webdriver.Chrome(executable_path=r"D:\tools\application\chromedriver.exe")
        # self.driver = webdriver.Edge(executable_path=r"D:\tools\application\MicrosoftWebDriver.exe")
        pass

# t1 = chrome_driver()
# t1.build_driver()
# t1.visit_web("https://search.bilibili.com/all?keyword=%E5%8D%97%E7%93%9C&from_source=banner_search")
# t1.edit_web('//*[@id="banner_link"]/div/div/form/input',"南瓜")
# t1.click_web('//*[@id="banner_link"]/div/div/form/button')
# t1.edit_web('//*[@id="search-keyword"]',"南瓜")
# t1.click_web('//*[@id="server-search-app"]/div[2]/div/div[2]/a')
# t1.click_web('//*[@id="server-search-app"]/div[2]/div[1]/div[2]/ul/li[9]')

# t1.click_web('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul[4]/li[1]/div/div[1]/a')

# t1.exit_web(10)

try :
    t1 = chrome_driver()
    t1.build_driver()
    t1.visit_web("https://www.bilibili.com/")
    t1.edit_web('//*[@id="banner_link"]/div/div/form/input',"南瓜")
    t1.click_web('//*[@id="banner_link"]/div/div/form/button')
    t1.click_web('//*[@id="server-search-app"]/div[2]/div[1]/div[2]/ul/li[9]')
    # t1.click_web('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul[4]/li[1]/div/div[1]/a')
    # t1.click_web('//*[@id="bilibiliPlayer"]/div[1]/div[2]/div[7]/video')

    t1.exit_web(50)
except :
    t1.exit_web(10)