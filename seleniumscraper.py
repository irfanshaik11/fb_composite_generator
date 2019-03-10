from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import pickle
import time

import sys
sys.path.append("/Users/HabibullahShaik/Desktop/FaceGrab-master/chromedriver")

url = "https://www.facebook.com/irfan.shaik.3344/friends_all"

driver = webdriver.Chrome("/Users/HabibullahShaik/Desktop/FaceGrab-master/chromedriver")

driver.get("https://www.facebook.com")

print("Please Navigate to Friends' List")
time.sleep(30)    # pause 5.5 seconds
print("Downloading Friends List")
driver.implicitly_wait(30)

for i in range(1): #repeats the operation 1 times
    driver.refresh()
    with open("friendslist" + str(i+1) + ".txt", "w") as f:
        f.write(driver.page_source)

driver.quit()