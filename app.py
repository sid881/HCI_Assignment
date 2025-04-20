
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder

def get_percentage_position(screen_width, screen_height, x_percent, y_percent):
    """Convert percentage positions to actual coordinates"""
    return (
        int(screen_width * (x_percent / 100)),
        int(screen_height * (y_percent / 100))
    )

def perform_tap(driver, x, y):
    """Universal tap function using W3C actions"""
    actions = ActionBuilder(driver)
    finger = actions.add_pointer_input("touch", "finger")
    finger.create_pointer_move(duration=0, x=x, y=y, origin="viewport")
    finger.create_pointer_down(button=0)
    finger.create_pointer_up(button=0)
    actions.perform()

def run_amazon_app():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "Android Emulator")
    options.set_capability("appPackage", "in.amazon.mShop.android.shopping")
    options.set_capability("appActivity", "com.amazon.mShop.home.HomeActivity")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("noReset", True)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    try:
        # Get dynamic screen dimensions
        screen_size = driver.get_window_size()
        screen_width = screen_size['width']
        screen_height = screen_size['height']


        # (a) Search for 'wireless headphones'
        start_search = time.time()
        search_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("in.amazon.mShop.android.shopping:id/chrome_search_hint_view")'))
        )
        search_bar.click()

        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID,
            "in.amazon.mShop.android.shopping:id/rs_search_src_text"))
        )
        search_input.send_keys("wireless headphones")
        driver.press_keycode(66)
        end_search = time.time()
        print(f"[a] Search completed in {round(end_search - start_search, 2)} seconds")
      
        lowest_price_filter_start=time.time();
        # Open filters
        filter_button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("s-all-filters")'))
        )
        filter_button.click()

        time.sleep(10);
        # Dynamic swipe (80% to 20% vertical position)
        start_x, start_y = get_percentage_position(screen_width, screen_height, 24, 81)
        end_x, end_y = get_percentage_position(screen_width, screen_height, 24,19 )
        for _ in range(3):
            driver.swipe(start_x, start_y, end_x, end_y, 600)

        # Sort by price
        low_price_filter = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Sort by")'))
        )
        low_price_filter.click();
        # Dynamic tap (center of screen - adjust percentages as needed)
        lowtohigh_x, lowtohigh_y = get_percentage_position(screen_width, screen_height, 66, 24)
        perform_tap(driver, lowtohigh_x, lowtohigh_y)
        
        time.sleep(10)
        # Final action (example: 90% width, 85% height - adjust as needed)
        submit_x, submit_y = get_percentage_position(screen_width, screen_height, 80, 91)
        perform_tap(driver, submit_x, submit_y)
        
        time.sleep(5)
        lowest_price_filter_time_end=time.time();
        print(f"[b] lowest priced headphone completed in {round(lowest_price_filter_time_end - lowest_price_filter_start-25, 2)} seconds")

        highest_rated_start_time=time.time();
        filter_x, filter_y = get_percentage_position(screen_width, screen_height,13 , 19)
        perform_tap(driver, filter_x, filter_y)
        

        start_x, start_y = get_percentage_position(screen_width, screen_height, 24, 81)
        end_x, end_y = get_percentage_position(screen_width, screen_height, 24,19 )
        for _ in range(3):
            driver.swipe(start_x, start_y, end_x, end_y, 600)

        sortby__filter = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Sort by")'))
        )
        sortby__filter.click()

        avg_review_x, avg_review_y = get_percentage_position(screen_width, screen_height, 49, 32)
        perform_tap(driver, avg_review_x, avg_review_y)

        time.sleep(5)
        # Final action (example: 90% width, 85% height - adjust as needed)
        submit_x, submit_y = get_percentage_position(screen_width, screen_height, 80, 91)
        perform_tap(driver, submit_x, submit_y)

        time.sleep(3)
        highest_rated_end_time=time.time();
        print(f"[c] highest rated headphone completed in {round(highest_rated_end_time - highest_rated_start_time-8, 2)} seconds")
        
        
        add_to_cart_start=time.time()
        start_x, start_y = get_percentage_position(screen_width, screen_height, 24, 81)
        end_x, end_y = get_percentage_position(screen_width, screen_height, 24,60)
        for _ in range(1):
            driver.swipe(start_x, start_y, end_x, end_y, 600)

        time.sleep(3)
        final_tap_x, final_tap_y = get_percentage_position(screen_width, screen_height, 69, 83)
        perform_tap(driver, final_tap_x, final_tap_y)
        time.sleep(3)
        add_to_cart_end=time.time();
        print(f"[d] add to cart completed in {round(add_to_cart_end - add_to_cart_start-4, 2)} seconds")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_amazon_app()
