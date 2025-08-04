from selenium import *
from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service  # pyright: ignore[reportMissingImports] # ✅ Required for Selenium 4+
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Development\\chromedriver.exe"
# Setup the Service object
service = Service(executable_path=chrome_driver_path)
# Pass the service to the driver
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")
search = driver.find_element(By.NAME, "q")
# print(search.tag_name)
# print(search.get_attribute("placeholder"))
logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

documentation = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation.text)

system_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[4]/a')
print(system_link.text)

# driver.close() # only close one tab
driver.quit()   # close the all tabs and app




# | Attribute              | Example Use                                                |
# | ---------------------- | ---------------------------------------------------------- |
# | `By.ID`                | `driver.find_element(By.ID, "main")`                       |
# | `By.NAME`              | `driver.find_element(By.NAME, "q")`                        |
# | `By.CLASS_NAME`        | `driver.find_element(By.CLASS_NAME, "header")`             |
# | `By.TAG_NAME`          | `driver.find_element(By.TAG_NAME, "a")`                    |
# | `By.LINK_TEXT`         | `driver.find_element(By.LINK_TEXT, "Downloads")`           |
# | `By.PARTIAL_LINK_TEXT` | `driver.find_element(By.PARTIAL_LINK_TEXT, "Doc")`         |
# | `By.XPATH`             | `driver.find_element(By.XPATH, "//div[@class='example']")` |
# | `By.CSS_SELECTOR`      | `driver.find_element(By.CSS_SELECTOR, ".python-logo")`     |


# | What You Want        | CSS Selector Syntax   | Example                |
# | -------------------- | --------------------- | ---------------------- |
# | Element by **class** | `.class-name`         | `.python-logo`         |
# | Element by **ID**    | `#id-name`            | `#main-nav`            |
# | Element by **tag**   | `tagname`             | `div`, `a`, `input`    |
# | Nested element       | `div span`, `ul > li` | `div.header span.logo` |
# | Attribute selector   | `[name='q']`          | `input[name='q']`      |
