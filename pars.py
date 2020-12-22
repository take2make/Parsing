from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
import air
"sudo apt-get install chromium-chromedriver"
DRIVER_PATH = "/usr/lib/chromium-browser/chromedriver"


def save_html(data, file='page.html'):
	with open(file, 'w') as file:
		file.write(data)

def get_players(driver):
	table = driver.find_elements_by_xpath('//table[@class="jss111 TableLeaderBoard__Table-sc-1j1prh2-0 eXxEgQ"]')[0]
	#save_html(table.get_attribute('innerHTML'), file="table.html")
	table = table.text.split("\n")
	table = np.array([row.split(" ") for row in table])
	return table.reshape(-1, 6)[1:]

def get_html(driver, url):
	driver.get(url)
	response = driver.page_source
	#save_html(response)
	return response

if __name__=="__main__":
	options = Options()
	options.headless = True

	driver = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
	driver.implicitly_wait(10)
	air.clean_table()
	url = "https://app.gamifer.com/leaderboard/nashi_krashe/"
	get_html(driver, url)
	players = get_players(driver)
	air.load_table(players)

	driver.quit()