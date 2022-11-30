# --*-- coding:utf-8 --*--
# @FileName      : t.py
# @DateTime      : 2022/11/28 16:12
# @Author        : SXS
# @Email         : sxs1316@outlook.com
# @description   : 
# @Version       : 

# 导入模板
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

d = {
    "appium:appPackage": "com.youdao.dict",
    "appium:appActivity": ".activity.DictSplashActivity",
    "appium:deviceName": "xiaomi5",
    "appium:platformVersion": "11",
    "platformName": "Android",
    "appium:noReset": True
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', d)

# 设置缺省等待时间
driver.implicitly_wait(10)

# 进入单词本列表
driver.find_element(By.XPATH, '//android.view.ViewGroup[@content-desc="单词本"]').click()

# 进入单词本

driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="3039词"]').click()

driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="卡片学习"]').click()

for i in range(1, 3040):
    b = driver.find_element(By.XPATH,
                            f'//android.widget.ImageView[@content-desc="{i}/3039"]/android.widget.Button/android.view.View[1]/android.view.View').get_attribute(
        'content-desc')
    driver.swipe(start_x=900, start_y=1200, end_x=200, end_y=1200, duration=100)
    print(b)
