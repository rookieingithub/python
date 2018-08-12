# -- coding : utf-8 --

import os
import time
from selenium import webdriver
from selenium.webdriver.support import ui

class WebDriver() :

    def __init__(self) :
        # 设置为无头模式
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        # 取消了无头模式
        options = None
        self.driver = webdriver.Firefox(options=options)

    def exit_web(self,wtime) :
        # time.sleep(wtime)
        if input("enter to exit : ") or True :
            # self.driver.close()
            self.driver.quit()

    def visit_web(self,website) :
        self.driver.get(website)

    def edit_web(self,xpath = None,sdstr = "") :
        ui.WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_xpath(xpath))
        self.driver.find_element_by_xpath(xpath).send_keys(sdstr)

    def click_web(self, xpath = None) :
        # 等待内容可见,总共10s时间内,每500ms搜索一次页面,直到元素释加载出来
        ui.WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_xpath(xpath))
        self.driver.find_element_by_xpath(xpath).click()
        # windows_num = driver.window_handles.index(driver.current_window_handle)
        self.driver.switch_to_window(self.driver.window_handles[len(self.driver.window_handles)-1])

    # 查找一组元素
    def search_elements(self,xpath) :
        # 很多时候找不到元素,但xpath路径没问题时,有可能是页面没加载出来,所以最好加上等待
        ui.WebDriverWait(self.driver,10).until(lambda driver: driver.find_element_by_xpath(xpath))
        result_list = self.driver.find_elements_by_xpath(xpath)
        return result_list
    
    def build_driver(self) :
        pass


t1 = WebDriver()
# t1.build_driver()
# 最大化浏览器
t1.driver.maximize_window()
# 1.打开起始网站
t1.visit_web("https://www.bilibili.com/")
# 2.这里刷新页面,是为了消除弹窗(只针对b站)
t1.driver.refresh()
t1.edit_web('//*[@id="banner_link"]/div/div/form/input',"南瓜")
t1.click_web('/html/body/div[2]/div[1]/div[2]/div/div/form/button')
result_list = t1.search_elements('/html/body/div[2]/div[2]/div[2]/div/div[2]/ul[4]/li[position()<9]/a/div')
print(result_list)
curwindow = t1.driver.current_window_handle

for result in result_list[:3] :
    try :
        result.click()
        next_windownum = t1.driver.window_handles.index(t1.driver.current_window_handle) + 1
        t1.driver.switch_to_window(t1.driver.window_handles[next_windownum])
        print(t1.driver.current_url)
        t1.click_web('/html/body/div[2]/div/div[6]/div[1]/div[2]/div[1]/div/div[1]/div[3]/div[1]/i[1]')
        time.sleep(1)
        t1.driver.switch_to_window(curwindow)
    except :
        print("goback old bilibili version")
        t1.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/a').click()
        t1.click_web('/html/body/div[2]/div/div[6]/div[1]/div[2]/div[1]/div/div[1]/div[3]/div[1]/i[1]')
        time.sleep(1)
        t1.driver.switch_to_window(curwindow)


# t1.driver.switch_to_window(curwindow)
# t1.click_web('/html/body/div[2]/div[2]/div[2]/div/div[2]/ul[4]/li[1]/a/div')
# t1.click_web('/html/body/div[2]/div/div[6]/div[1]/div[2]/div[1]/div/div[1]/div[3]/div[1]/i[1]')

t1.exit_web(10)
