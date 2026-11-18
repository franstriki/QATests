import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "usuario, clave, debe_entrar",
    [
        ("standard_user", "secret_sauce", True),
        ("locked_out_user", "secret_sauce", False),
        ("usuario_invalido", "clave_mal", False),
    ],
)
def test_flujo_login(driver, usuario, clave, debe_entrar):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.abrir()
    login_page.iniciar_sesion(usuario, clave)

    if debe_entrar:
        assert inventory_page.esta_visible(), f"El usuario {usuario} debió entrar."
    else:
        assert not inventory_page.esta_visible(), f"El usuario {usuario} no debió entrar."
        assert "Epic sadface" in login_page.obtener_mensaje_error()
