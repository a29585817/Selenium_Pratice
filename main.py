from selenium import webdriver

chrome_driver = "Your driver Path"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.python.org/")

event = driver.find_elements_by_css_selector(".event-widget li a")
event_name = [e.text for e in event]
event_time = driver.find_elements_by_css_selector(".event-widget li time")
event_date = [x.text for x in event_time]
event_sheet = {x: {"time": event_date[x], "name": event_name[x]}for x in range(len(event_date))}
print(event_sheet)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)

# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]')
# print(bug_link.text)

# driver.close()
driver.quit()