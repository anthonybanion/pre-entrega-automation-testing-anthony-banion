import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver import crear_driver

URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
PASSWORD = "secret_sauce"


def test_login_exitoso():
    """Verifica que un usuario válido pueda iniciar sesión."""

    driver = crear_driver()

    try:
        driver.get(URL)

        wait = WebDriverWait(driver, 10)

        # Ingresar usuario
        campo_usuario = wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        campo_usuario.send_keys(USUARIO)

        # Ingresar contraseña
        campo_password = wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        campo_password.send_keys(PASSWORD)

        # Hacer clic en Login
        boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        boton_login.click()

        # Validar URL de inventario
        wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url

        # Validar texto Products
        titulo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

        assert titulo.text == "Products"

        # Validar título de la página
        assert driver.title == "Swag Labs"

    finally:
        driver.quit()


def test_catalogo():
    """Verifica la navegación y los elementos principales del catálogo."""

    driver = crear_driver()

    try:
        driver.get(URL)

        wait = WebDriverWait(driver, 10)

        # Login
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
            USUARIO
        )

        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
            PASSWORD
        )

        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

        # Esperar inventario
        wait.until(EC.url_contains("/inventory.html"))

        # Validar título de la página
        assert driver.title == "Swag Labs"

        # Validar título Products
        titulo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))

        assert titulo.text == "Products"

        # Validar que exista al menos un producto visible
        productos = wait.until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

        assert len(productos) > 0

        # Obtener nombre y precio del primer producto
        primer_producto = productos[0]

        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

        precio = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        ).text

        print(f"Primer producto: {nombre}")
        print(f"Precio: {precio}")

        assert nombre != ""
        assert precio != ""

        # Validar menú
        menu = wait.until(
            EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))
        )

        assert menu.is_displayed()

        # Validar filtro
        filtro = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
        )

        assert filtro.is_displayed()

    finally:
        driver.quit()


def test_carrito():
    """Verifica que un producto pueda agregarse correctamente al carrito."""

    driver = crear_driver()

    try:
        driver.get(URL)

        wait = WebDriverWait(driver, 10)

        # Login
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
            USUARIO
        )

        wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
            PASSWORD
        )

        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

        # Esperar inventario
        wait.until(EC.url_contains("/inventory.html"))

        # Obtener primer producto
        productos = wait.until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

        primer_producto = productos[0]

        nombre_producto = primer_producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        ).text

        # Botón Add to cart del primer producto
        boton_agregar = primer_producto.find_element(By.CSS_SELECTOR, "button")

        boton_agregar.click()

        # Verificar contador del carrito
        contador = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        assert contador.text == "1"

        # Ir al carrito
        carrito = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )

        carrito.click()

        # Verificar URL
        wait.until(EC.url_contains("/cart.html"))

        assert "/cart.html" in driver.current_url

        # Verificar producto agregado
        producto_carrito = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
        )

        assert producto_carrito.text == nombre_producto

    finally:
        driver.quit()
