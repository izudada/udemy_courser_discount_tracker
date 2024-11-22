from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configure options
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the course page
    driver.get("https://www.udemy.com/course/javascript-data-structures-algorithms/")

    # Wait for the element to be visible
    wait = WebDriverWait(driver, 30)
    discount_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-purpose='discount-percentage']"))
    )

    # Extract the spans
    values = [span.text for span in discount_element.find_elements(By.TAG_NAME, "span") if span.text.strip()]
    print("Discount Values:", values)

    # Fallback to JavaScript
    if not values:
        values = driver.execute_script("""
            let container = document.querySelector("div[data-purpose='discount-percentage']");
            if (!container) return [];
            return Array.from(container.getElementsByTagName("span")).map(span => span.textContent.trim());
        """)
        print("Discount Values via JS:", values)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
