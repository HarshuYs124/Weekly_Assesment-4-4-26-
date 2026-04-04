from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger


def test_valid_login(setup_and_teardown):
    driver = setup_and_teardown # get driver instance from fixture

    lp = LoginPage(driver) # create loginpage object

    config = ConfigReader.read_config() # read configuration from YAML
    env = config['qa'] # select qa environment

    BASE_URL = env['base_url'] # get application URL
    USERNAME = env['username'] # get username
    PASSWORD = env['password'] # get password

    # opening the website using base URL
    driver.get(BASE_URL)

    get_logger().info("Trying to log in") # log info message
    # get_logger().error()


    # Perform login
    lp.click_login() # click on login link
    lp.enter_email(USERNAME) # enter username/email
    lp.enter_password(PASSWORD) # enter password
    lp.click_login_button() # click login button
