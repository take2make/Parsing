from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
"sudo apt-get install chromium-chromedriver"
DRIVER_PATH = "/usr/lib/chromium-browser/chromedriver"


def save_html(data, file='page.html'):
	with open(file, 'w') as file:
		file.write(data)

def get_players(driver):
	table = driver.find_elements_by_xpath('//td[@class=" "]')
	players = np.array([player.text for player in table])
	return players.reshape(-1,5)

def get_html(driver, url):
	driver.get(url)
	response = driver.page_source
	save_html(response)
	return response

if __name__=="__main__":
	options = Options()
	options.headless = True

	driver = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
	driver.implicitly_wait(30)
	url = "https://app.gamifer.com/leaderboard/nashi_krashe/"
	get_html(driver, url)
	players = get_players(driver)
	
	print(players[0][1])
	driver.quit()