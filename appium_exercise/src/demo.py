#!/usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver

desired_caps={
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appActivity": ".view.WelcomeActivityAlias",
  "appPackage": "com.xueqiu.android",
	"noReset": True
}

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.click()
el4.send_keys("阿里巴巴")
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView")
el5.click()

