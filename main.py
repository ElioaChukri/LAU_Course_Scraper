from driver import initializeDriver
from helpers import loadFile, login, searchForCourses, parseCourses, writeCsv


def main():
    username, password = loadFile()
    driver = initializeDriver()
    driver.get("https://myportal.lau.edu.lb/")
    login(driver, username, password)
    courses_page = searchForCourses(driver)
    data = parseCourses(courses_page)
    writeCsv(data)
    print("Done!")


if __name__ == "__main__":
    main()
