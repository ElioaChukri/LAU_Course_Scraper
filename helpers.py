import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from bs4 import BeautifulSoup


def loadFile():
    """
    Loads the credentials from the credentials.csv file
    :return: username, password
    """
    with open("credentials.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            return row["username"], row["password"]


def writeCsv(rows):
    """
    Writes the given rows to the output.csv file
    :param rows: the rows to write to the file
    :return: None
    """
    with open("output.csv", "w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(rows[0])
        csv_writer.writerows(rows[1:])


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


def searchForCourses(driver):
    """
    Navigates to the search page, chooses the proper term and options, and searches for the wanted courses
    :param driver: the selenium webdriver
    :return: the courses page html
    """

    # Navigate to the search page
    driver.get("https://banweb.lau.edu.lb/prod/bwskfcls.p_sel_crse_search")

    # Select the proper term from the dropdown menu and click submit
    term_drop_down = Select(driver.find_element(By.CSS_SELECTOR, "select#term_input_id"))
    term_drop_down.select_by_visible_text("Fall 2023 (View only)")
    driver.find_element(By.XPATH, "/html/body/div[3]/form/input[2]").click()

    # Click on advanced search
    driver.find_element(By.XPATH, "/html/body/div[3]/form/input[18]").click()

    # Select the proper options for the search
    subject_drop_down = Select(driver.find_element(By.CSS_SELECTOR, "select#subj_id"))
    subject_drop_down.select_by_visible_text("Computer Science")
    campus_drop_down = Select(driver.find_element(By.CSS_SELECTOR, "select#camp_id"))
    campus_drop_down.deselect_all()
    campus_drop_down.select_by_visible_text("Byblos")

    # Click on "Section Search" button
    driver.find_element(By.XPATH, "/html/body/div[3]/form/span/input[1]").click()

    return driver.page_source


def parseCourses(html):
    """
    Parses the courses page html using bs4 and returns a list of lists containing the courses data
    :param html: the html source code of the page we wish to extract course data from
    :return: data_list: a list of lists containing the courses data
    """
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("table.datadisplaytable > tbody")
    data = table.select("tr")
    data_list = []

    # First row elements are the headers
    row = []
    for th in data[1].select("th"):
        row.append(th.text.strip())
    data_list.append(row)

    # Rest of the rows are the courses
    for tr in data[2:]:
        row = []
        for td in tr.select("td"):
            row.append(td.text.strip())
        data_list.append(row)

    return data_list
