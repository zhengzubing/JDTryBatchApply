# 京东试用批量申请脚本

![label1](https://img.shields.io/badge/爬虫-京东试用-green)   ![label1](https://img.shields.io/badge/chrome-selenium-blue) ![label1](https://img.shields.io/badge/京东试用批量申请脚本-v1.0-blue)  

## 使用方法

### 环境

Chrome, 与Chrome对应版本的chromedriver, Python3, selenium库

### 运行步骤

1)安装运行环境：
 安装Chrome浏览器,下载对应版本的chromedriver, 将chromedriver.exe文件添加到Chrome的安装路径,将chromedriver安装路径添加进系统环境变量,安装Python, 为Python添加selenium库。

2)运行 GetCookies.py,会弹出浏览器窗口并自动跳转到京东登录页面,以任何一种方式登录,登录成功后会自动跳转页面,此时无需任何操作,程序会自动结束运行。程序运行完毕会在同级目录生成cookies.json文件。

3)运行 MainProgram.py, 程序将利用上一步获取的cookies自动登录京东试用,并自动申请试用。

注：不用每次都运行 GetCookies.py, 一次获取cookies后能使用多日,直至cookies过期,在此期间仅运行步骤3就可自动登录并申请试用
