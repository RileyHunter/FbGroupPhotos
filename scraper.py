from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import os
import re

chrome_options = Options()
chrome_options.set_capability('unhandledPromptBehavior', 'ignore')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://facebook.com')
current_url = None
group_re = re.compile('https:\/\/www.facebook\.com\/groups\/[\d]+')
while True:
	if driver.current_url != current_url:
		print(f'Detected navigation to {driver.current_url}')
		current_url = driver.current_url
		print(group_re.search(current_url))
		if group_re.search(current_url) is not None:
			break

media_url = current_url + '/media'
driver.get(media_url)
root_xpath = '//div[contains(@style, "min-width: 168")]/div/div/div/a'
WebDriverWait(driver, 20).until(EC.visibility_of_any_elements_located((By.XPATH, root_xpath)))
root_elements = driver.find_elements(By.XPATH, root_xpath)
hrefs = []
print(f'Found {len(root_elements)}')
for el in root_elements:
	print('an href?')
	href = el.get_attribute('href')
	hrefs.append(href)

img_xpath = '//div[contains(@style, "transform: translate(0px, 0px) scale(1);")]/div/img'
image_folder = './captures'
if not os.path.exists(image_folder):
	os.mkdir(image_folder)
for index, href in enumerate(hrefs):
	driver.get(href)
	src = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, img_xpath))).get_attribute('src')
	urllib.request.urlretrieve(src, f'{image_folder}/{index}.png')

