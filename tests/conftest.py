import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opciones = Options()
    # Ejecuta Chrome en segundo plano sin interfaz gráfica
    opciones.add_argument("--headless=new")
    # Simula una pantalla grande para evitar diseños móviles ocultos
    opciones.add_argument("--window-size=1920,1080")
    navegador = webdriver.Chrome(options=opciones)

    # Entrega el navegador a la prueba
    yield navegador

    # Se ejecuta automáticamente al terminar cada prueba
    navegador.quit()
