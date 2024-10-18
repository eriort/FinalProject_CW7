from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoAlertPresentException, TimeoutException


class TestLogin:

    def setup_method(self):
        # WebDriver setup (adjust for your WebDriver)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demo.guru99.com/Agile_Project/Agi_V1/")

    def teardown_method(self):
        # Close browser after test
        self.driver.quit()

    def test_valid_login(self):
        self.driver.find_element(By.NAME, 'uid').send_keys("1303")
        self.driver.find_element(By.NAME, 'password').send_keys("Guru99")
        self.driver.find_element(By.NAME, 'btnLogin').click()
        time.sleep(2)
        assert "Welcome To Customer's Page of Guru99 Bank" in self.driver.page_source

    def test_empty_credentials(self):
        self.driver.find_element(By.NAME, 'btnLogin').click()
        time.sleep(3)
        alert = self.driver.switch_to.alert


        alert_text = alert.text

        assert "User or Password is not valid" in alert_text, f"Unexpected alert text: {alert_text}"

        alert.accept()
        time.sleep(2)

    def test_invalid_username(self):
        self.driver.find_element(By.NAME, 'uid').send_keys("0152")
        self.driver.find_element(By.NAME, 'password').send_keys("Guru99")
        self.driver.find_element(By.NAME, 'btnLogin').click()
        time.sleep(3)
        try:

            alert = self.driver.switch_to.alert


            alert_text = alert.text

            assert "User or Password is not valid" in alert_text

            alert.accept()
        except TimeoutException:

            assert False, "Expected alert did not appear."

        except NoAlertPresentException:

            assert False, "Alert not found when expected"

    def test_invalid_password(self):
        self.driver.find_element(By.NAME, 'uid').send_keys("1303")
        self.driver.find_element(By.NAME, 'password').send_keys("58963")
        self.driver.find_element(By.NAME, 'btnLogin').click()
        time.sleep(3)
        try:

            alert = self.driver.switch_to.alert

            alert_text = alert.text

            assert "User or Password is not valid" in alert_text


            alert.accept()
        except TimeoutException:

            assert False, "Expected alert did not appear."


        except NoAlertPresentException:

            assert False, "Alert not found when expected"

    def test_reset_button(self):
        self.driver.find_element(By.NAME, 'uid').send_keys("1303")
        self.driver.find_element(By.NAME, 'password').send_keys("Guru99")
        self.driver.find_element(By.NAME, 'btnReset').click()

        assert self.driver.find_element(By.NAME, 'uid').get_attribute('value') == ""
        assert self.driver.find_element(By.NAME, 'password').get_attribute('value') == ""
        time.sleep(3)