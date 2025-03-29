from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep the Chrome browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

string_url = "https://pixe.la/v1/users/zoyamomin/graphs/graph2"

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(string_url)

# Wait for the element to be present
try:
    image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='svg-load-area-0']/svg/rect"))
    )
    print("Element found:", image)
except:
    print("Element not found")

# Close the driver if needed
# driver.quit()

