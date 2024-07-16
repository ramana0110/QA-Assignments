from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open Amazon's homepage
driver.get("https://www.amazon.com")

# Allow the page to load
time.sleep(20)

# Search for a specific product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

# Allow search results to load
time.sleep(2)

# Extract information about the first 5 search results
results = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")[:5]

# Function to extract product details
def extract_product_info(result):
    try:
        title = result.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
    except:
        title = "Title not available"

    try:
        price = result.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
    except:
        price = "Price not available"

    try:
        rating = result.find_element(By.XPATH, ".//span[@class='a-icon-alt']").get_attribute("innerHTML")
    except:
        rating = "Rating not available"

    try:
        reviews = result.find_element(By.XPATH, ".//span[@class='a-size-base']").text
    except:
        reviews = "Reviews not available"

    return {
        "title": title,
        "price": price,
        "rating": rating,
        "reviews": reviews
    }

# Print extracted information in a structured format
for i, result in enumerate(results, start=1):
    product_info = extract_product_info(result)
    print(f"Product {i}:")
    print(f"Title: {product_info['title']}")
    print(f"Price: {product_info['price']}")
    print(f"Rating: {product_info['rating']}")
    print(f"Number of Reviews: {product_info['reviews']}")
    print("-" * 40)

# Close the driver
driver.quit()
