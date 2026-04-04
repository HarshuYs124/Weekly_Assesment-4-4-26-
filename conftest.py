import  pytest
from selenium import webdriver
from config.env import ConfigReader

@pytest.fixture
def setup_and_teardown():
    # Reading Config
    config = ConfigReader.read_config()
    env = config["qa"] # YAML has with qa
    base_url = env["base_url"]

    # Setup (Before test)
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    # teardown (After Test)
    driver.quit()

