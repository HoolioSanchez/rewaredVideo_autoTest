import os
import copy
import sys
import unittest
from appium import webdriver

from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '12.1'
desired_caps['automationName'] = 'xcuitest'
desired_caps['deviceName'] = 'iPhone 7'
desired_caps['bundleId'] = 'com.ironsrcmobile.Iron'
desired_caps['showIOSLog'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def clickShowRV(waitTime):
    driver.implicitly_wait(waitTime)

    driver.find_element_by_accessibility_id('Show').click()
    clickClose(3000)

clickShowRV(5000)

def clickClose(waitTime):
    driver.implicitly_wait(waitTime)
    driver.find_element_by_accessibility_id('Close Advertisement')
