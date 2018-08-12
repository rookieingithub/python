# -- coding : utf-8 --

import os
import time
from selenium import webdriver

class WebDriver() :

    def __init__(self) :
        # self.driver = webdriver.Edge()
        self.driver = webdriver.Firefox()

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
        self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles)-1])

    def build_driver(self) :
        pass


try :
    t1 = WebDriver()
    t1.build_driver()
    # 1.打开起始网站
    t1.visit_web("https://www.bilibili.com/")
    # 2.这里刷新页面,是为了消除弹窗(只针对b站)
    t1.driver.refresh()
    t1.edit_web('//*[@id="banner_link"]/div/div/form/input',"南瓜")
    t1.click_web('/html/body/div[2]/div[1]/div[2]/div/div/form/button')
    t1.click_web('/html/body/div[2]/div[2]/div[2]/div/div[2]/ul[4]/li[1]/a/div/div[1]/img')

    t1.exit_web(10)
except :
    print("error exit")
    t1.exit_web(10)