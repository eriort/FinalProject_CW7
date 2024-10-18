from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from constants import  PAYMENT_GATEWAY_URL


class TestPaymentGateway:
    def setup_method(self):

        self.driver = webdriver.Chrome()
        self.driver.get(PAYMENT_GATEWAY_URL)

    def teardown_method(self):
        self.driver.quit()
        time.sleep(3)
    def test_select_item_and_buy(self):
        select_element = Select(self.driver.find_element(By.NAME, 'quantity'))
        time.sleep(3)

        select_element.select_by_index(8)

        self.driver.find_element(By.XPATH, "//*[@id='three']/div/form/div/div[8]/ul/li/input").click() # Clicking the Buy button
        time.sleep(3)

        assert "Payment Process" in self.driver.page_source


    def test_fill_credit_card(self):

        self.test_select_item_and_buy()

        self.driver.find_element(By.NAME, 'card_nmuber').send_keys("96348556302300001") # Filling credit card details
        self.driver.find_element(By.NAME, 'cvv_code').send_keys("783")


        select_month = Select(self.driver.find_element(By.NAME, 'month'))
        select_month.select_by_visible_text("03")


        select_year = Select(self.driver.find_element(By.NAME, 'year'))
        select_year.select_by_visible_text("2027")
        time.sleep(3)


        self.driver.find_element(By.NAME, 'submit').click()


        assert "Payment success" in self.driver.page_source or "Transaction failed" in self.driver.page_source
        time.sleep(5)