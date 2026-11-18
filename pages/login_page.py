from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    # Localizadores exclusivos de esta página
    URL = "https://saucedemo.com"
    USER_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.NAME, "password")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def iniciar_sesion(self, usuario: str, clave: str):
        campo_user = self.wait.until(EC.element_to_be_clickable(self.USER_INPUT))
        campo_user.clear()
        campo_user.send_keys(usuario)

        campo_pwd = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        campo_pwd.clear()
        campo_pwd.send_keys(clave)
        campo_pwd.send_keys(Keys.RETURN)

    def obtener_mensaje_error(self) -> str:
        elemento_error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return elemento_error.text
