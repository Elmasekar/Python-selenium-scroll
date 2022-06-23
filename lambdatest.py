import os
import unittest
import sys
from selenium import webdriver

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class FirstSampleTest(unittest.TestCase):

	# setUp runs before each test case
	def setUp(self):
		desired_caps = {
			'LT:Options': {
				"user": username,
				"accessKey": access_key,
				"build": "Python-Selenium-Sample",
				"name": "Python-Selenium-Test",
				"platformName": "Windows 11",
				"selenium_version": "4.0.0"
			},
			"browserName": "Chrome",
			"browserVersion": "latest",
		}

		self.driver = webdriver.Remote(
			command_executor="http://hub.lambdatest.com:80/wd/hub",
			desired_capabilities=desired_caps)


# tearDown runs after each test case

	def tearDown(self):
		self.driver.quit()

	def scroll_bottom():
		"""
		Verify scrolling to bottom
		:return: None
		"""
		driver.get('https://www.lambdatest.com/')
		driver.maximize_window()
		sleep(2)
		success = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(5)
		assert success == True
	
	def scroll_infinite():
		"""
		Verify infinite scroll
		:return: None
		"""
		SCROLL_PAUSE_TIME = 0.5

		# Get scroll height
		last_height = driver.execute_script("return document.body.scrollHeight")

		#controls how many times scrolled to bottom
		scroll_pass = 0

		#change to True for infinite scroll
		while scroll_pass < 10:
			# Scroll down to bottom
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# Wait to load page
			time.sleep(SCROLL_PAUSE_TIME)

			# Calculate new scroll height and compare with last scroll height
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height
			scroll_pass+=1
	


if __name__ == "__main__":
	unittest.main()
