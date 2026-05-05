# ParaBank QA Automation

> [Versión en Español](#parabank-qa-automatización)

End-to-end test automation framework for the [ParaBank](https://parabank.parasoft.com) demo banking application, built with **Selenium WebDriver** and **pytest** following the **Page Object Model** (POM) pattern.

---

## Tech Stack

| Tool | Version | Role |
|---|---|---|
| Python | 3.11+ | Language |
| Selenium WebDriver | 4.x | Browser automation |
| pytest | 9.x | Test runner |
| pytest-html | 4.x | HTML report generation |
| webdriver-manager | 4.x | Auto-manages ChromeDriver |

---

## [Manual and Exploratory Test Cases](https://docs.google.com/spreadsheets/d/1Y6SNjHjeQ5mN3Z1oCo8Gp-3OE2-S-Jf9Gco2HFdXYKA/edit?usp=sharing)

---

## Project Structure

```
parabank-qa/
├── locators/               # Element selectors, grouped by page
│   ├── login_locators.py
│   ├── register_locators.py
│   ├── accounts_locators.py
│   └── transfer_locators.py
├── pages/                  # Page Object Model classes
│   ├── base_page.py        # Shared actions with built-in explicit waits
│   ├── login_page.py
│   ├── register_page.py
│   ├── accounts_page.py
│   └── transfer_page.py
├── tests/                  # pytest test files
│   ├── test_login.py
│   ├── test_register.py
│   ├── test_accounts.py
│   └── test_transfer.py
├── test_data/              # Reusable test data and generators
│   └── users.py
├── utils/                  # Shared utilities
│   ├── config.py           # URL constants
│   ├── driver_factory.py   # Chrome driver setup (CI-aware)
│   └── waits.py            # Explicit wait helpers
├── reports/                # Auto-generated HTML reports (git-ignored)
├── conftest.py             # pytest fixtures (driver, logged_in_driver)
├── pytest.ini              # pytest configuration
└── requirements.txt
```

---

## Test Coverage

| Module | Test | What it verifies |
|---|---|---|
| Login | `test_login_valid_user` | Valid credentials land on Accounts Overview |
| Login | `test_login_invalid` | Wrong password shows "could not be verified" error |
| Registration | `test_register_new_user_successfully` | New user registers and sees welcome message |
| Registration | `test_register_duplicate_username_shows_error` | Existing username triggers field-level error |
| Registration | `test_register_blank_form_shows_validation_errors` | Empty form shows required-field errors |
| Accounts | `test_accounts_overview_displays_after_login` | Accounts heading and table visible after login |
| Accounts | `test_accounts_table_contains_account_links` | Table has at least one clickable account link |
| Accounts | `test_open_new_checking_account` | CHECKING account opens and returns a numeric ID |
| Accounts | `test_open_new_savings_account` | SAVINGS account opens and returns a numeric ID |
| Transfer | `test_transfer_funds_between_accounts` | $100 transfer shows "Transfer Complete!" |
| Transfer | `test_transfer_confirmation_shows_amount` | Confirmation message contains the exact amount |

---

## Prerequisites

- Python 3.11+
- Google Chrome (latest)
- Git

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/parabank-qa.git
cd parabank-qa

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

```bash
# Run all tests (HTML report written to reports/report.html)
pytest

# Run a single test file
pytest tests/test_login.py

# Run with verbose output
pytest -v

# Run one specific test
pytest tests/test_login.py::test_login_valid_user

# Run without the HTML report
pytest --no-header -p no:html
```

Open `reports/report.html` in any browser to view the formatted report.

---

## Architecture

### Page Object Model

Every page of ParaBank has a corresponding class under `pages/`. Each class inherits from `BasePage`, which wraps Selenium interactions with **10-second explicit waits** so tests do not break on slow connections or AJAX responses.

### Fixtures (`conftest.py`)

| Fixture | Scope | Description |
|---|---|---|
| `driver` | function | Creates a Chrome session, opens the home page, quits after the test |
| `logged_in_driver` | function | Builds on `driver`; authenticates as `john` before yielding |

### CI / CD

Tests run automatically on every push and pull request via **GitHub Actions** (`ubuntu-latest`, Python 3.11). Chrome is pre-installed on the runner; `driver_factory.py` detects the `CI` environment variable and enables headless mode automatically. The HTML report is uploaded as a build artifact after every run.

---

---

# ParaBank QA Automatización

> [English version](#parabank-qa-automation)

Framework de automatización de pruebas end-to-end para la aplicación bancaria demo [ParaBank](https://parabank.parasoft.com), construido con **Selenium WebDriver** y **pytest** siguiendo el patrón **Page Object Model** (POM).

---

## Stack Tecnológico

| Herramienta | Versión | Rol |
|---|---|---|
| Python | 3.11+ | Lenguaje |
| Selenium WebDriver | 4.x | Automatización de navegador |
| pytest | 9.x | Ejecución de pruebas |
| pytest-html | 4.x | Generación de reportes HTML |
| webdriver-manager | 4.x | Gestión automática de ChromeDriver |

---

## [Documentación casos de prueba Manuales y Exploratorios](https://docs.google.com/spreadsheets/d/1Y6SNjHjeQ5mN3Z1oCo8Gp-3OE2-S-Jf9Gco2HFdXYKA/edit?usp=sharing)

---

## Estructura del Proyecto

```
parabank-qa/
├── locators/               # Selectores de elementos agrupados por página
│   ├── login_locators.py
│   ├── register_locators.py
│   ├── accounts_locators.py
│   └── transfer_locators.py
├── pages/                  # Clases del Page Object Model
│   ├── base_page.py        # Acciones compartidas con esperas explícitas
│   ├── login_page.py
│   ├── register_page.py
│   ├── accounts_page.py
│   └── transfer_page.py
├── tests/                  # Archivos de prueba pytest
│   ├── test_login.py
│   ├── test_register.py
│   ├── test_accounts.py
│   └── test_transfer.py
├── test_data/              # Datos de prueba reutilizables y generadores
│   └── users.py
├── utils/                  # Utilidades compartidas
│   ├── config.py           # Constantes de URL
│   ├── driver_factory.py   # Configuración de Chrome (con soporte CI)
│   └── waits.py            # Funciones de espera explícita
├── reports/                # Reportes HTML generados automáticamente
├── conftest.py             # Fixtures de pytest (driver, logged_in_driver)
├── pytest.ini              # Configuración de pytest
└── requirements.txt
```

---

## Cobertura de Pruebas

| Módulo | Prueba | Qué verifica |
|---|---|---|
| Login | `test_login_valid_user` | Credenciales válidas redirigen a Accounts Overview |
| Login | `test_login_invalid` | Contraseña incorrecta muestra error de verificación |
| Registro | `test_register_new_user_successfully` | Usuario nuevo se registra y ve el mensaje de bienvenida |
| Registro | `test_register_duplicate_username_shows_error` | Usuario existente genera error en el campo correspondiente |
| Registro | `test_register_blank_form_shows_validation_errors` | Formulario vacío muestra errores de campo requerido |
| Cuentas | `test_accounts_overview_displays_after_login` | Encabezado y tabla de cuentas visibles tras el login |
| Cuentas | `test_accounts_table_contains_account_links` | La tabla tiene al menos un enlace de cuenta |
| Cuentas | `test_open_new_checking_account` | Se abre una cuenta CHECKING y se recibe un ID numérico |
| Cuentas | `test_open_new_savings_account` | Se abre una cuenta SAVINGS y se recibe un ID numérico |
| Transferencia | `test_transfer_funds_between_accounts` | Transferencia de $100 muestra "Transfer Complete!" |
| Transferencia | `test_transfer_confirmation_shows_amount` | El mensaje de confirmación contiene el monto exacto |

---

## Requisitos Previos

- Python 3.11+
- Google Chrome (última versión)
- Git

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/your-username/parabank-qa.git
cd parabank-qa

# 2. Crear y activar un entorno virtual
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Ejecución de Pruebas

```bash
# Ejecutar todas las pruebas (reporte en reports/report.html)
pytest

# Ejecutar un archivo específico
pytest tests/test_login.py

# Ejecutar con salida detallada
pytest -v

# Ejecutar una prueba específica
pytest tests/test_login.py::test_login_valid_user

# Ejecutar sin reporte HTML
pytest --no-header -p no:html
```

Abre `reports/report.html` en cualquier navegador para ver el reporte formateado.

---

## Arquitectura

### Page Object Model

Cada página de ParaBank tiene su clase correspondiente en `pages/`. Todas heredan de `BasePage`, que envuelve las interacciones de Selenium con **esperas explícitas de 10 segundos** para que las pruebas no fallen por tiempos de carga lentos o respuestas AJAX.

### Fixtures (`conftest.py`)

| Fixture | Alcance | Descripción |
|---|---|---|
| `driver` | función | Crea una sesión Chrome, abre la página principal y cierra el navegador al terminar |
| `logged_in_driver` | función | Extiende `driver`; autentica como `john` antes de ceder el control |

### CI / CD

Las pruebas se ejecutan automáticamente en cada push y pull request mediante **GitHub Actions** (`ubuntu-latest`, Python 3.11). Chrome viene preinstalado en el runner; `driver_factory.py` detecta la variable de entorno `CI` y activa el modo headless automáticamente. El reporte HTML se sube como artefacto de la build después de cada ejecución.
