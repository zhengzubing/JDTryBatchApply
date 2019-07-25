#!/usr/bin/env python
# coding=utf-8
#
#此脚本为*获取京东登录cookies脚本*
#环境： chrome 、chromedriver 、selenium 
#注意：cookies有一定的时限，过期后需要重新运行此脚本已获取新的cookies
#运行此文件请到该文件所在的目录运行（即将工作空间切换到该文件所在路径，不然可能找不到cookies.json的写入路径），若找不到cookies.json请查看控制台输出
#此文仅供技术交流，任何由此产生的法律问题概不负责

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json #用于将dict写入文件
import  os

##############################
#参数配置区：
login_page_url='https://passport.jd.com/new/login.aspx' #此页面为京东登录页面，需保证此网址正常访问
cookies_save_path ="cookies.json" 
print("cookies.json文件保存在",os.getcwd(),"目录下")
##############################

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(login_page_url) #打开登录界面
print("已经打开登录页面，请在浏览器中*手动登录*（可扫码登录），登录成功后无需进行任何操作，程序将自动结束运行")
#driver.delete_all_cookies() #清空登录前的cookies
time.sleep(15) #花15s等待用户手动登录
while driver.current_url == login_page_url:  #判断是否成功登录(登录成功会跳转页面)，否则继续等待
    time.sleep(10)
#获取cookies保存到本地
time.sleep(5)
cookies = driver.get_cookies()
cookie_dict = {}
for cookie in cookies: #筛选数据，获取到的cookies中只有name与value两项有用
    if 'name' in cookie.keys() and 'value' in cookie.keys():
        cookie_dict[cookie['name']] = cookie['value']
print("成功获取到cookies:     ",cookie_dict)
jsObj = json.dumps(cookie_dict) #转换为json串方便保存
print("获取到的cookies为：    ",jsObj)
f = open(cookies_save_path,'w') #将获取到的cookies保存到cookies.txt文件中 
f.write(jsObj)  
f.close()
driver.close()
driver.quit()