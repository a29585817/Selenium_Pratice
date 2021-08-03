from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver = "Your driver Path"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
mail = driver.find_element_by_name("email")
name.send_keys("Meng Chien")
l_name.send_keys("Lin")
mail.send_keys("a0919149590@gmail.com")
botton = driver.find_element_by_tag_name("button")
botton.send_keys(Keys.ENTER)