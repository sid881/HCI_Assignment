import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder

# Utility function to calculate screen coordinates from percentage
def get_percentage_position(screen_width, screen_height, x_percent, y_percent):
    return (
        int(screen_width * (x_percent / 100)),
        int(screen_height * (y_percent / 100))
    )

# Perform a universal tap on a specific screen coordinate
def perform_tap(driver, x, y):
    actions = ActionBuilder(driver)
    finger = actions.add_pointer_input("touch", "finger")
    finger.create_pointer_move(duration=0, x=x, y=y, origin="viewport")
    finger.create_pointer_down(button=0)
    finger.create_pointer_up(button=0)
    actions.perform()

# Main test function to automate Amazon mobile app interactions
def run_amazon_app():
    # Desired capabilities for the Appium server
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "Android Emulator")
    options.set_capability("appPackage", "in.amazon.mShop.android.shopping")
    options.set_capability("appActivity", "com.amazon.mShop.home.HomeActivity")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("noReset", True)

    # Initialize Appium driver
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    try:
        # Get dynamic screen size
        screen_size = driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']

        # [a] Search for 'wireless headphones'
        start_search = time.time()
        search_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("in.amazon.mShop.android.shopping:id/chrome_search_hint_view")'))
        )
        search_bar.click()

        # Wait for search input to appear, type and press Enter
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID,
            "in.amazon.mShop.android.shopping:id/rs_search_src_text"))
        )
        search_input.send_keys("wireless headphones")
        driver.press_keycode(66)  # Keycode 66 = Enter
        end_search = time.time()
        print(f"[a] Search completed in {round(end_search - start_search, 2)} seconds")

        # [b] Sort by lowest price
        lowest_price_filter_start = time.time()
        
        # Open filters section
        filter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("s-all-filters")'))
        )
        filter_button.click()
        time.sleep(5)

        # Scroll down using swipe gesture to reveal "Sort by" option
        start_x, start_y = get_percentage_position(screen_width, screen_height, 24, 81)
        end_x, end_y = get_percentage_position(screen_width, screen_height, 24, 19)
        for _ in range(3):
            driver.swipe(start_x, start_y, end_x, end_y, 600)

        # Tap on "Sort by"
        low_price_filter = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Sort by")'))
        )
        low_price_filter.click()

        # Tap on "Price: Low to High" using coordinates
        lowtohigh_x, lowtohigh_y = get_percentage_position(screen_width, screen_height, 66, 24)
        perform_tap(driver, lowtohigh_x, lowtohigh_y)

        time.sleep(10)

        # Submit the filters
        submit_x, submit_y = get_percentage_position(screen_width, screen_height, 80, 91)
        perform_tap(driver, submit_x, submit_y)

        time.sleep(5)
        lowest_price_filter_time_end = time.time()
        print(f"[b] Lowest priced headphone filter completed in {round(lowest_price_filter_time_end - lowest_price_filter_start - 20, 2)} seconds")

        # [c] Sort by highest rated
        highest_rated_start_time = time.time()

        # Reopen filter section
        filter_x, filter_y = get_percentage_position(screen_width, screen_height, 13, 19)
        perform_tap(driver, filter_x, filter_y)

        # Scroll again
        for _ in range(3):
            driver.swipe(start_x, start_y, end_x, end_y, 600)

        # Tap on "Sort by"
        sortby_filter = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Sort by")'))
        )
        sortby_filter.click()

        # Tap on "Avg. Customer Review"
        avg_review_x, avg_review_y = get_percentage_position(screen_width, screen_height, 49, 32)
        perform_tap(driver, avg_review_x, avg_review_y)

        time.sleep(5)

        # Submit the filters
        submit_x, submit_y = get_percentage_position(screen_width, screen_height, 80, 91)
        perform_tap(driver, submit_x, submit_y)

        time.sleep(3)
        highest_rated_end_time = time.time()
        print(f"[c] Highest rated headphone filter completed in {round(highest_rated_end_time - highest_rated_start_time - 8, 2)} seconds")

        # [d] Add top-rated item to cart
        add_to_cart_start = time.time()

        # Scroll slightly to reveal the item
        end_y = get_percentage_position(screen_width, screen_height, 24, 60)[1]
        driver.swipe(start_x, start_y, end_x, end_y, 600)

        time.sleep(3)

        # Tap on first product
        final_tap_x, final_tap_y = get_percentage_position(screen_width, screen_height, 69, 83)
        perform_tap(driver, final_tap_x, final_tap_y)

        time.sleep(3)
        add_to_cart_end = time.time()
        print(f"[d] Add to cart completed in {round(add_to_cart_end - add_to_cart_start - 6, 2)} seconds")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

# Entry point
if __name__ == "__main__":
    run_amazon_app()
