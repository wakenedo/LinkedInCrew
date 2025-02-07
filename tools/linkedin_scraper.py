import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from crewai_tools import tool
from tools.utils import get_linkedin_posts  # Ensure utils.py exists

class LinkedinToolException(Exception):
    def __init__(self):  # Fixed constructor
        super().__init__("LinkedinToolException: You need to set the LINKEDIN_EMAIL and LINKEDIN_PASSWORD env variables")

def scrape_linkedin_posts_fn() -> str:
    """
    A tool that can be used to scrape LinkedIn posts from a user profile.
    """
    from config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD, LINKEDIN_PROFILE_NAME  # Import from config.py

    if not (LINKEDIN_EMAIL and LINKEDIN_PASSWORD):
        raise LinkedinToolException()
    if not LINKEDIN_PROFILE_NAME:
        raise ValueError("Missing required env variable: LINKEDIN_PROFILE_NAME")

    # Use ChromeOptions for better automation handling
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection
    browser = webdriver.Chrome(options=options)

    browser.get("https://www.linkedin.com/login")

    # Locate and fill in login credentials
    username_input = browser.find_element(By.ID, "username")
    password_input = browser.find_element(By.ID, "password")
    username_input.send_keys(LINKEDIN_EMAIL)
    password_input.send_keys(LINKEDIN_PASSWORD)
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)

    # Navigate to the profile's recent activity
    browser.get(f"https://www.linkedin.com/in/{LINKEDIN_PROFILE_NAME}/recent-activity/all/")

    for _ in range(2):  # Fixed syntax error
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    
    posts = get_linkedin_posts(browser.page_source)
    browser.quit()

    return str(posts[:2])  # Ensure returning posts before quitting

@tool("ScrapeLinkedinPosts")
def scrape_linkedin_posts_tool() -> str:
    """ A tool that scrapes LinkedIn posts from a user profile. """
    return scrape_linkedin_posts_fn()
