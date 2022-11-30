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
    "appium:platformVersion": "7.1.3",
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

x = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ScrollView'

x += '/android.view.View'

while 1:
    d = driver.find_elements(By.XPATH,x)
    for i in d:
        dc = i.get_attribute('content-desc')
        print(dc)
    driver.swipe(start_x=450, start_y=2280, end_x=450, end_y=250, duration=1000)
