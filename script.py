import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

action = sys.argv[1] if len(sys.argv) > 1 else "signin"

try:
    if action == "signin":
        driver.get("https://hipharm.modulus.biz/index.php?module=cmn&page=Index&action=Login&url=index.php%3Fmodule%3Dhr%26page%3DEmployee%26action%3DAttendanceLogs")
        time.sleep(4) 
        driver.find_element(By.NAME, "username").send_keys("fady.youssef")
        driver.find_element(By.NAME, "password").send_keys("b9H3xa")
        driver.find_element(By.ID, "Submit").click()
        print("تم تسجيل الدخول بنجاح!")
        time.sleep(5)
        
    elif action == "signout":
        driver.get("https://hipharm.modulus.biz/index.php?module=cmn&page=Index&action=Login")
        time.sleep(2)
        driver.get("https://hipharm.modulus.biz/index.php?module=cmn&page=Index&action=Logout")
        print("تم تسجيل الخروج بنجاح!")
        time.sleep(3)

except Exception as e:
    print(f"حدث خطأ: {e}")
finally:
    driver.quit()
