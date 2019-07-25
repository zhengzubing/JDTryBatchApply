#!/usr/bin/env python
# coding=utf-8
#此脚本为京东试用批量申请主程序，通过cookies缓存登录京东账户，并进行试用商品的申请。
from selenium import webdriver
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#-----------------登录京东--------------------------------
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('headless') #该语句注释掉则显示浏览器运行界面，取消注释则不显示
chromeOptions.add_argument('window-size=1200x600')
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('https://passport.jd.com/new/login.aspx') #必须首先加载网站(最好是获取cookies的网址)，这样selenium才知道cookie是属于哪个网站的
with open("cookies.json",'r') as load_f:
    load_dict = json.load(load_f)
cookies = load_dict
print("成功从文件读取到cookies:",cookies)
driver.delete_all_cookies()
for k,v in cookies.items():
    # 添加cookies
    print(k,v)
    driver.add_cookie({'name': k, 'value': v})
driver.get('https://try.jd.com/')
time.sleep(3)
driver.get('http://try.jd.com/activity/getActivityList')
time.sleep(5)

for j in range(1,250):#遍历274页商品，可根据实际情况调整
    items = driver.find_elements_by_class_name("link")#获取当前页面所有商品列表
    titles = driver.find_elements_by_class_name("p-name")#获取商品的标题    
    for i in range(len(items)):
        title= titles[i].text#输出商品标题
        items[i].click()#点击商品，进入申请页面
        handles = driver.window_handles
        handle = driver.current_window_handle#获取当前页面标识
        for newhandle in handles:
            if newhandle!=handle:
                driver.switch_to.window(newhandle)
        #-------------------------------------------------
        try:#如果商品未申请，显示“申请试用”，try正常执行
            time.sleep(1)
            driver.find_element_by_link_text('申请试用').click()
            time.sleep(1)
            driver.find_element_by_link_text('关注并申请').click()
            time.sleep(2)
            handle = driver.current_window_handle#获取当前页面标识
            #--------从申请页面切换页面至商品列表页---------------
            for newhandle in handles:
                if newhandle!=handle:
                    driver.close()
                    driver.switch_to.window(newhandle)
        except:#如果已经申请过，则无法找到“申请试用”，try无法正常执行，执行except
            handle = driver.current_window_handle
            for newhandle in handles:
                if newhandle!=handle:
                    driver.close()
                    driver.switch_to.window(newhandle)
        print("已自动申请：%s" % title) 
    driver.find_element_by_class_name('ui-pager-next').click()#点击下一页



