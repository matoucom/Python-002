# -*- coding: utf-8 -*-
# 使用 requests 或 Selenium 模拟登录石墨文档 https://shimo.im

from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    time.sleep(1)

    browser.find_element_by_xpath('//a[contains(@href,"login")]').click()

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('15055495@qq.com')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('123123123')
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    time.sleep(3)
except Exception as e:
    print(e)
finally:
    browser.close()
    # pass