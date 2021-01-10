#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import allure


def test_login(browser):
    with allure.step("step1：打开登录首页"):
        browser.get("http://ip:6009/admin/login/?next=/admin/")
    with allure.step("step2：输入账号：admin"):
        browser.find_element_by_name("username").send_keys("admin")
    with allure.step("step2：输入密码：123456"):
        browser.find_element_by_name("password").send_keys("123456")
    # 故意断言失败，看是否会截图
    assert browser.title == "悠悠"