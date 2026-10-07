from selenium import webdriver


def crear_driver():
    """Crea una instancia de Chrome para las pruebas."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
