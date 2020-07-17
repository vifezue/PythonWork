from selenium import webdriver
from functions.functionLibrary import *
import re
from selenium.common.exceptions import NoAlertPresentException

"""""""""""""""""""""
    Victor Ifezue
    Week 4 Assignment
    IT414 Petz
"""""""""""""""""""""

my_browser = startBrowser()
directory = getPath()

submitButton = my_browser.find_element_by_id("my_submit")
txtFirstName = my_browser.find_element_by_id("firstName")
txtLastName = my_browser.find_element_by_id("lastName")
txtPhone = my_browser.find_element_by_id("phoneNumber")
txtEmailAddress = my_browser.find_element_by_id("emailAddress")
textboxes = my_browser.find_elements_by_tag_name("input[type ='text']")

for item in textboxes:

    itemValue = item.get_attribute("value")
    itemID = item.get_attribute("id")

    if itemID == "firstName":

        # Blank field TEST
        txtFirstName.send_keys("")

        screenshotDestination = "screenshot1.png"
        destinationPath = os.path.join(directory, screenshotDestination)

        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "First name is required" in errorText:

            renameFileAsPassed(destinationPath)
        txtFirstName.clear()
        screenshotDestination = None

        # Invalid length TEST
        txtFirstName.send_keys("Jo")

        screenshotDestination = "screenshot2.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Please check the length of the First name field" in errorText:
            renameFileAsPassed(destinationPath)
        txtFirstName.clear()
        screenshotDestination = None

        # Too large of a length TEST
        txtFirstName.send_keys("Micheal Jordan")
        screenshotDestination = "screenshot01.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Please check the length of the First name field" in errorText:
            renameFileAsPassed(destinationPath)
        txtFirstName.clear()
        screenshotDestination = None

        # FIRST NAME TEST
        txtFirstName.send_keys("Micheal")
        screenshotDestination = "screenshot14.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()
        renameFileAsPassed(destinationPath)
        txtFirstName.clear()

    if itemID == "lastName":
        txtLastName.send_keys("")
        screenshotDestination = "screenshot3.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Last name is required" in errorText:
            renameFileAsPassed(destinationPath)
        txtLastName.clear()
        screenshotDestination = None

        # LAST NAME TEST
        txtLastName.send_keys("Jo")
        screenshotDestination = "screenshot4.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Please check the length of the Last name field" in errorText:
            renameFileAsPassed(destinationPath)
        txtLastName.clear()
        screenshotDestination = None

        # LAST NAME TEST
        txtLastName.send_keys("Jordan")
        screenshotDestination = "screenshot5.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Please check the length of the Last name field" in errorText:
            renameFileAsPassed(destinationPath)
        txtLastName.clear()
        screenshotDestination = None

    if itemID == "phoneNumber":
        txtPhone.send_keys("")
        screenshotDestination = "screenshot6.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Phone number is required" in errorText:
            renameFileAsPassed(destinationPath)
        txtPhone.clear()

        #   BAD PHONE NUMMBER TEST
        txtPhone.send_keys("34sdsd")
        screenshotDestination = "screenshot7.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Your phone number is an incorrect format" in errorText:
            renameFileAsPassed(destinationPath)
        txtPhone.clear()
        screenshotDestination = None

        # BAD PHONE NUMBER TEST
        txtPhone.send_keys("545454545454545454")
        screenshotDestination = "screenshot8.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Your phone number is an incorrect format" in errorText:
            renameFileAsPassed(destinationPath)
        txtPhone.clear()
        screenshotDestination = None

        # BAD PHONE NUMBER TEST
        txtPhone.send_keys("586563393a")
        screenshotDestination = "screenshot9.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Your phone number is an incorrect format" in errorText:
            renameFileAsPassed(destinationPath)
        txtPhone.clear()
        screenshotDestination = None

        # SUCESSFUL PHONE NUMBER TEST
        txtPhone.send_keys("586-563-3934")
        screenshotDestination = "screenshot10.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()
        renameFileAsPassed(destinationPath)
        txtPhone.clear()

    if itemID == "emailAddress":
        # BAD EMAIL ADDRESS TEST
        txtEmailAddress.send_keys("9887799.com")
        screenshotDestination = "screenshot11.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()
        errorAlert = my_browser.switch_to.alert

        errorText = errorAlert.text
        errorAlert.accept()

        if "Your email address is in an incorrect format" in errorText:
            renameFileAsPassed(destinationPath)
        txtEmailAddress.clear()
        screenshotDestination = None

        # BAD EMAIL ADDRESS TEST
        txtEmailAddress.send_keys("pinvalid")
        screenshotDestination = "screenshot12.png"
        destinationPath = os.path.join(directory, screenshotDestination)
        my_browser.save_screenshot(destinationPath)
        submitButton.click()

        errorAlert = my_browser.switch_to.alert
        errorText = errorAlert.text
        errorAlert.accept()

        if "Your email address is in an incorrect format" in errorText:
            renameFileAsPassed(destinationPath)
        txtEmailAddress.clear()
        screenshotDestination = None

# SUCCESSFUL SUBMISSION TEST
txtFirstName.send_keys("Victor")
txtLastName.send_keys("Ifezue")
txtPhone.send_keys("586-563-3934")
txtEmailAddress.send_keys("ifezue@me.com")
screenshotDestination = "screenshot13.png"
destinationPath = os.path.join(directory, screenshotDestination)
my_browser.save_screenshot(destinationPath)
submitButton.click()
try:
    #SUCCESSFUL SUBMISSION TEST
    errorAlert = my_browser.switch_to.alert
    errorText = errorAlert.text
    errorAlert.accept()
except NoAlertPresentException:
    last_browser = startSubmitBrowser()
    submitURLtext = last_browser.find_element_by_class_name("lead")
    if "Your response has been received. Thank you for submitting!" in submitURLtext.text:
        renameFileAsPassed(destinationPath)
        last_browser.quit()
        my_browser.quit()
