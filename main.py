import csv
from driver import initializeDriver
from helpers import loadFile, login, navigateToSearch


def main():
    username, password = loadFile()
    driver = initializeDriver()
    driver.get("https://myportal.lau.edu.lb/")
    login(driver, username, password)
    navigateToSearch(driver)


if __name__ == "__main__":
    main()
