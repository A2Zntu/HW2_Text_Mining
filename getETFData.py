from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time as time

# not used (yet)
import os
import requests as re
from bs4 import BeautifulSoup
from lxml import etree

chromedriver = "./driver/chromedriver"
input_file_name = "ETF_names.txt"
base_url_search = "https://www.moneydj.com/funddj/ya/yFundSearch.djhtm?a="
base_url_detail = "https://www.moneydj.com/funddj/yp/yp011000.djhtm?a="
xpath_search = '//*[@id="article"]/p/table/tbody/tr[2]/td[1]/a'
xpath_detail = '//*[@id="article"]/form/table/tbody/tr[20]/td[2]/a[2]'

def strQ2B(ustring):
# 全形轉半形
# source from https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/373914/
	rstring = ""
	for uchar in ustring:
		inside_code=ord(uchar)
		

		inside_code-=0xfee0
		
		if inside_code<0x0020 or inside_code>0x7e:
			rstring  += uchar
		else:
			rstring  += chr(inside_code)
	return rstring

def waiting(browser,xpath):
	# wait the browser to load JS and track whether the browser is time out (ex : server crash will cause browser time out)
	delay = 3 # seconds
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
		return myElem
	except TimeoutException:
		print("Loading took too much time!")	
		return None



dir_path = os.path.dirname(os.path.realpath(__file__))

ETF_name_list = []
# load data file
dataFile = open(input_file_name,"r",encoding = 'utf8')
for line in dataFile:
	ETF_name_list.append(strQ2B(line.replace("\n","")))


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : dir_path +  "\\prospectus\\"}
chromeOptions.add_experimental_option("prefs",prefs)


browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
nameCodeDict = {}
for name in ETF_name_list:
	browser.get(base_url_search + name)

	returnElem = waiting(browser,xpath_search)
	if returnElem != None:
		print("success load {}".format(name))
		ETF_url = returnElem.get_attribute("href")
		ETF_code = ETF_url.split("=")[-1]

		print(ETF_code)
		nameCodeDict[name] = ETF_code
	else:
		print("QQ")



for name in nameCodeDict:
	browser.get(base_url_detail + nameCodeDict[name])

	# returnElem = waiting(browser,xpath_detail)
	time.sleep(0.5)
	a = browser.find_element_by_xpath("//*[contains(text(), '公開說明書')]").get_attribute("href")
	if a != None:
		browser.get(a)


