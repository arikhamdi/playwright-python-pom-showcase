import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


load_dotenv()

def run_diagnostic():
    url = os.getenv("BASE_URL", "https://www.google.com")
    print(f"🚀 Diagnosis launched on : {url}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url)
            print(f"✅ CConnection successful !")
            print(f"📝 Page title : {page.title()}")
        except Exception as e:
            print(f"❌ Connection failed : {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run_diagnostic()