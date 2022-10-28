from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.python.org/')
field = driver.find_element(By.ID, 'id-search-field')
field.click()
field.send_keys('comprehension')
button = driver.find_element(By.ID, 'submit')
button.click()
text = driver.find_element(
    By.CSS_SELECTOR, '.list-recent-events li:first-child').text

print(text)
