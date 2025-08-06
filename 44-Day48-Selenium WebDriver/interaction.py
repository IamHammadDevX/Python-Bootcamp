from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service  # pyright: ignore[reportMissingImports] # ✅ Required for Selenium 4+
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\\Development\\chromedriver.exe"
# Setup the Service object
service = Service(executable_path=chrome_driver_path)
# Pass the service to the driver
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")

# visitors = driver.find_element(By.CSS_SELECTOR, "#articlecount li a")
# visitors.click()
# print(visitors.text)

# all_portals = driver.find_element(By.LINK_TEXT, "Wikipedia")
# all_portals.click()
# print(all_portals.text)

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Form Filling automation
fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Ahmed")
fname.send_keys(Keys.TAB)
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("DevX")
lname.send_keys(Keys.TAB)
email = driver.find_element(By.NAME, "email")
email.send_keys("abc@gmail.com")
email.send_keys(Keys.TAB)
sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()





input("Press Enter to close the browser...")
driver.quit()