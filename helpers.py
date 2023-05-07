import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys


def loadFile():
    """
    Loads the credentials from the credentials.csv file
    :return: username, password
    """
    with open("credentials.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            return row["username"], row["password"]


def login(driver, username, password):
    """
    Logs in to the portal using the given credentials
    :param driver: the selenium webdriver
    :param username: the username to log in with
    :param password: the password to log in with
    :return: None
    """
    # URL we have to reach after logging in
    landing_page = "https://myportal.lau.edu.lb/Pages/studentPortal.aspx"

    # Log in using the given credentials
    driver.find_element(By.CSS_SELECTOR, "input#username").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div/main/div/form/input[3]").click()

    # Wait until all the redirects are done, and we reach the landing page
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_matches(landing_page))


def navigateToSearch(driver):
    """
    Navigates to the course search page on banner
    :param driver:
    :return:
    """

    driver.get("https://banweb.lau.edu.lb/prod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu")
    options = driver.find_elements(By.CSS_SELECTOR, "td > a")
    for element in options:
        visible_text = element.accessible_name.lower()
        if visible_text == "look-up classes to add":
            element.click()
            break
