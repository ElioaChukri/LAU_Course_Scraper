import csv
from driver import initializeDriver
from helpers import loadFile, login, searchForCourses


def main():
    username, password = loadFile()
    driver = initializeDriver()
    driver.get("https://myportal.lau.edu.lb/")
    login(driver, username, password)
    courses_page = searchForCourses(driver)
    print(courses_page)


if __name__ == "__main__":
    main()
