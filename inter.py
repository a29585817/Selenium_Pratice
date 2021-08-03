from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "Your driver Path"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_element_by_css_selector("#articlecount a")
# articles.click()

all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)