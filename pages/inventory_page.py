from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def esta_visible(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.INVENTORY_LIST))
            return True
        except TimeoutException:
            return False
