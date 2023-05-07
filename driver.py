from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys


def initializeDriver():
    """
    Initialize the driver with pre-set options to run headless
    :return: driver: the selenium webdriver
    """

    options = webdriver.ChromeOptions()
    options.add_argument(
        f"user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    )
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(options=options)

    return driver
