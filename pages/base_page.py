from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    # Constructor to initialize driver and explicit wait.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def click(self, locator):
        # Waits until the element is clickable and then click
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Input text
    def enter_text(self,locator, text):
        #Wait for element and clear existing text
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        # enter new text
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self,locator):
        # Wait for element and return its visible text
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self,locator):
        # Wait until element is visible and return it
        return self.wait.until(EC.visibility_of_element_located(locator))
