import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def run_amazon_automation():
    # Setup Chrome driver
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        # (f) Home page load time
        start_home = time.time()
        driver.get("https://www.amazon.in")
        wait.until(EC.presence_of_element_located((By.ID, "nav-logo-sprites")))
        end_home = time.time()
        print(f"[f] Home page load time: {round(end_home - start_home, 2)} seconds")

        # (a) Search for "wireless headphones"
        start_search = time.time()
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
        search_box.clear()
        search_box.send_keys("wireless headphones")
        search_box.send_keys(Keys.RETURN)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-item")))
        end_search = time.time()
        print(f"[a] Search time: {round(end_search - start_search, 2)} seconds")

        # (b) Sort by price (Low to High)
        start_sort_price = time.time()
        sort_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sort by:')]")))
        sort_dropdown.click()
        low_to_high = wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select_1")))
        low_to_high.click()
        time.sleep(3)  # Wait for results to reload
        end_sort_price = time.time()
        print(f"[b] Sort by price time: {round(end_sort_price - start_sort_price, 2)} seconds")


        name = driver.find_element(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span').text
        price = driver.find_element(By.XPATH, '//span[@class="a-price"]/span[@class="a-offscreen"]').get_attribute("textContent")
        print("Name:", name)
        print("Price:", price)
        driver.implicitly_wait(10);
        # (c) Sort by customer review (highest rated)
        start_sort_rating = time.time()
        
        select_element = wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select")))
        Select(select_element).select_by_visible_text("Avg. Customer Review")
    
        end_sort_rating = time.time()
        print(f"[c] Sort by rating time: {round(end_sort_rating - start_sort_rating, 2)} seconds")

        # Extract the FIRST (top-rated) product's NAME and PRICE
        name = driver.find_element(By.XPATH, '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]/span').text
        price = driver.find_element(By.XPATH, '//span[@class="a-price"]/span[@class="a-offscreen"]').get_attribute("textContent")
        print("Name:", name)
        print("Price:", price)

        driver.execute_script("window.scrollBy(0, 500);")
        add_cart_start=time.time();
        # Wait until the "Add to Cart" button is present
        add_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Add to cart' or normalize-space()='Add to cart']")))
        # Now click the button
        add_cart_button.click()
        add_cart_end=time.time();
        print(f"[d] adding to cart time: {round(add_cart_end - add_cart_start, 2)} seconds")
        time.sleep(1);
        
    except Exception as e:
        print(f"Error: {str(e)}")
        driver.save_screenshot("error_screenshot.png")
        print("Screenshot saved as error_screenshot.png")

    finally:
        driver.quit()

if __name__ == "__main__":
    run_amazon_automation()
    