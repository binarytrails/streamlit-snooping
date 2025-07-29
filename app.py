# app.py
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_page_info(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--disable-extensions")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "section"))
        )

        title = driver.title
        source = driver.page_source
        return title, source

    except Exception as e:
        return f"[!] Error: {e}", ""

    finally:
        driver.quit()


st.title("🕷️ Selenium URL Loader")

url = st.text_input("Enter a URL to load:", placeholder="https://example.com")

if st.button("Fetch"):
    if url:
        title, source = get_page_info(url)
        st.subheader("Page Title:")
        st.write(title)
        st.subheader("Page Source Snippet:")
        st.code(source)
    else:
        st.warning("Please enter a valid URL.")

