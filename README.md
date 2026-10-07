# Pre-Entrega Automation Testing

Proyecto de automatización de pruebas web desarrollado como pre-entrega del curso de Automation Testing.

## Sitio bajo prueba

https://www.saucedemo.com/

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Google Chrome
- pytest-html
- Git
- GitHub

## Estructura del proyecto

```text
automatic_test/

├── tests/
│   └── test_saucedemo.py
│
├── utils/
│   └── driver.py
│
├── reports/
├── screenshots/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Pruebas automatizadas

### 1. Login

- Navegación al sitio SauceDemo.
- Inicio de sesión con usuario `standard_user`.
- Inicio de sesión con contraseña `secret_sauce`.
- Validación de la URL `/inventory.html`.
- Validación del texto `Products`.
- Validación del título `Swag Labs`.

### 2. Catálogo

- Validación del título de la página.
- Verificación de productos visibles.
- Verificación del menú principal.
- Verificación del selector de ordenamiento.
- Obtención y visualización del nombre y precio del primer producto.

### 3. Carrito

- Selección del primer producto.
- Verificación del contador del carrito.
- Navegación al carrito.
- Verificación de que el producto seleccionado se encuentre en el carrito.

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
cd automatic_test
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Navegador

Las pruebas se ejecutan utilizando **Google Chrome** mediante Selenium WebDriver.

Es necesario tener Google Chrome instalado en el equipo donde se ejecuten las pruebas.

Selenium gestiona automáticamente el controlador necesario para la ejecución del navegador.

## Ejecución de las pruebas

Ejecutar todas las pruebas:

```bash
pytest -v
```
