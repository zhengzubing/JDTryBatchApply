# 京东试用批量申请脚本
![label1](https://img.shields.io/badge/%E7%88%AC%E8%99%AB-%E4%BA%AC%E4%B8%9C%E8%AF%95%E7%94%A8-green&?link=http://https://github.com/zhengzubing/Crawler)
## 使用方法
1. 环境 ： chrome, 对应版本的chromedriver, python, selenium库
2. 运行步骤 ： 
1）运行GetCookies.py，会弹出浏览器窗口并自动跳转到京东登录页面，以任何一种方式登录，登录成功后会自动跳转页面，此时无需任何操作，程序会自动结束运行。程序运行完毕会在同级目录生成cookies.json文件。
		
2）运行MainProgram.py, 程序将利用步骤一中获取的cookies自动登录京东试用，并自动申请试用。

注：不用每次都运行GetCookies.py, 一次获取cookies后能使用多日，直至cookies过期，在此期间仅运行步骤二就可自动登录并申请试用

## 原理
1. 后续跟新
