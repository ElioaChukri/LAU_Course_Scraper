from driver import initializeDriver
from helpers import loadFile, login, searchForCourses, parseCourses, writeCsv


def main():
    # Load the credentials from the credentials.csv file
    username, password = loadFile()

    # Initialize the driver with pre-set options to run headless
    driver = initializeDriver()

    # Navigate to the portal
    driver.get("https://myportal.lau.edu.lb/")

    # Log in using the given credentials
    login(driver, username, password)

    # Search for the wanted courses and get the html source code of the courses page
    courses_page = searchForCourses(driver)

    # Parse the courses page and write the data to the output.csv file
    data = parseCourses(courses_page)
    writeCsv(data)
    print("Done!")


if __name__ == "__main__":
    main()
