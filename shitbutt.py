from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import re

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://ide.geeksforgeeks.org/tryit.php/WXYeMD9tD4')
input()