"""
Take screenshots of AryaCart pages using Selenium
"""
import os, sys, time

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except ImportError:
    print("Installing selenium...")
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

SAVE_DIR = r"c:\Users\amang\Desktop\codealpha_tasks\Task1_AryaCart\screenshots"
BASE_URL = "http://127.0.0.1:8000"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

pages = [
    ("01_home_page.png", "/", "Home Page"),
    ("02_shop_page.png", "/products/", "Shop Page"),
    ("03_product_detail.png", "/product/macbook-pro-m3/", "Product Detail"),
    ("04_register_page.png", "/accounts/register/", "Register Page"),
    ("05_login_page.png", "/accounts/login/", "Login Page"),
    ("06_about_page.png", "/pages/about/", "About Page"),
    ("07_contact_page.png", "/pages/contact/", "Contact Page"),
]

for filename, path, name in pages:
    try:
        url = BASE_URL + path
        driver.get(url)
        time.sleep(2)
        filepath = os.path.join(SAVE_DIR, filename)
        driver.save_screenshot(filepath)
        print(f"  OK: {name} -> {filename}")
    except Exception as e:
        print(f"  FAIL: {name} -> {e}")

# Now login and take cart/profile screenshots
try:
    driver.get(BASE_URL + "/accounts/login/")
    time.sleep(1)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    
    # Cart page
    driver.get(BASE_URL + "/cart/")
    time.sleep(1)
    driver.save_screenshot(os.path.join(SAVE_DIR, "08_cart_page.png"))
    print("  OK: Cart Page -> 08_cart_page.png")
    
    # Profile page  
    driver.get(BASE_URL + "/accounts/profile/")
    time.sleep(1)
    driver.save_screenshot(os.path.join(SAVE_DIR, "09_profile_page.png"))
    print("  OK: Profile Page -> 09_profile_page.png")
    
    # Admin panel
    driver.get(BASE_URL + "/admin/")
    time.sleep(1)
    driver.save_screenshot(os.path.join(SAVE_DIR, "10_admin_panel.png"))
    print("  OK: Admin Panel -> 10_admin_panel.png")
    
except Exception as e:
    print(f"  FAIL: Logged-in pages -> {e}")

driver.quit()
print(f"\nDone! Screenshots saved to {SAVE_DIR}")
