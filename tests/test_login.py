import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

def test_login_success(page):
    """
    Test case to verify that a user can login successfully 
    with valid credentials.
    """
    base_url = os.getenv("BASE_URL")
    user = os.getenv("STANDARD_USER")
    password = os.getenv("PASSWORD")

    required_vars = {
        "BASE_URL": base_url, 
        "STANDARD_USER": user, 
        "PASSWORD": password
    }

    missing_vars = [name for name, val in 
                    {"BASE_URL": base_url, "STANDARD_USER": user, "PASSWORD": password}.items() 
                    if not val
                    ]
    
    if missing_vars:
        raise ValueError(f"❌ Configuration error: Missing variables in .env : {', '.join(missing_vars)}")
    
    login_page = LoginPage(page)

    
    # 2. Action
    login_page.load(base_url)
    login_page.login(user, password)
    
    # 3. Assert
    assert "inventory.html" in page.url