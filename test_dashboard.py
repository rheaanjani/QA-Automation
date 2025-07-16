import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = r"C:\webdriver\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    
    url = "https://dash.tepak.id"
    print(f"🌐 Membuka {url}")
    driver.get(url)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("✅ Halaman berhasil dimuat.")

    # 4. Verifikasi judul halaman
    title = driver.title
    print(f"🔎 Judul halaman: {title}")
    if "TailAdmin" in title or "Dashboard" in title:
        print("✅ Judul sesuai.")
    else:
        print("⚠️ Judul tidak sesuai.")

    # 5. Periksa elemen penting (contoh: heading atau tombol)
    try:
        heading = driver.find_element(By.TAG_NAME, "h1")
        print("✅ Heading ditemukan:", heading.text.strip())
    except:
        print("❌ Heading tidak ditemukan.")

    # 6. Screenshot
    os.makedirs("screenshots", exist_ok=True)
    screenshot_path = "screenshots/homepage_tepak.png"
    driver.save_screenshot(screenshot_path)
    print(f"📸 Screenshot disimpan: {screenshot_path}")

finally:
    time.sleep(2)
    driver.quit()
    print("✅ Selesai.")