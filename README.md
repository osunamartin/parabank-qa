ENG

# 🎯 Objective

This repository contains an end-to-end test automation framework for the demo banking application [ParaBank](https://parabank.parasoft.com), using:

* ✅ Selenium WebDriver
* ✅ Pytest
* ✅ Page Object Model (POM)
* ✅ UI Automation
* ✅ Automated HTML Reports

The goal is to validate critical banking system functionalities in a reproducible and maintainable way.

Including:

* User login
* User registration
* Bank account overview
* Opening new accounts
* Fund transfers between accounts
* Form validations and error handling

---

## 📝 Manual Testing Documentation

* [Manual and exploratory test cases](https://docs.google.com/spreadsheets/d/1Y6SNjHjeQ5mN3Z1oCo8Gp-3OE2-S-Jf9Gco2HFdXYKA/edit?usp=sharing)

---

## 🧰 Technologies

* Python 3.11+
* Selenium WebDriver
* Pytest
* Pytest-HTML
* WebDriver Manager

---

## ⚙️ Prerequisites

Make sure you have installed:

* Google Chrome
* Python 3.11+
* Git

---

## 🐍 Environment Setup

Clone the repository:

```bash
git clone https://github.com/your-username/parabank-qa.git
cd parabank-qa
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run a specific file:

```bash
pytest tests/test_login.py
```

Run a single test:

```bash
pytest tests/test_login.py::test_login_valid_user
```

Verbose mode:

```bash
pytest -v
```

Run without HTML report:

```bash
pytest --no-header -p no:html
```

The HTML report is automatically generated at:

```bash
reports/report.html
```

---

## 🧪 Test Coverage

### Login

* Successful login validation
* Empty field validation
* Error message verification

### Registration

* Successful new user registration
* Duplicate username validation
* Required fields validation

### Accounts Overview

* Proper account overview display
* Verification of account links
* Opening CHECKING and SAVINGS accounts

### Transfers

* Transfers between accounts
* Transferred amount validation
* Successful transfer confirmation

---

## 🧱 Project Architecture

The project uses the **Page Object Model (POM)** pattern to separate automation logic from test logic.

Main structure:

```bash
parabank-qa/
├── locators/
├── pages/
├── tests/
├── test_data/
├── utils/
├── reports/
├── conftest.py
├── pytest.ini
└── requirements.txt
```

### Main Components

#### `pages/`

Contains Page Object classes responsible for encapsulating interactions with each screen.

#### `locators/`

Contains grouped selectors for each page.

#### `tests/`

Contains automated test scenarios implemented with pytest.

#### `utils/`

Reusable utilities such as:

* Driver setup
* Explicit waits
* Global configuration

---

## 🧩 Important Fixtures

### `driver`

* Initializes a Chrome session
* Opens the application
* Closes the browser after each test

### `logged_in_driver`

* Extends the `driver` fixture
* Automatically logs in before authenticated tests

---

## 🚀 CI/CD

The project is prepared for automatic execution using **GitHub Actions**.

Includes:

* Automatic execution on pushes and pull requests
* Headless execution support in CI
* Automatic HTML report generation
* Report artifact uploads

---

## 🧼 Best Practices Used

* Page Object Model (POM)
* Explicit waits for stability
* Reusable fixtures
* Separation of concerns
* Independent tests
* Scalable and maintainable structure

---

## 🚀 Possible Future Improvements

* Allure Reports integration
* Data-driven testing
* Cross-browser testing
* Dockerized environment
* Selenium Grid integration

---

## 👨‍💻 Author

Project created by Martin Osuna as a QA Automation practice project using Python, Selenium WebDriver, and end-to-end testing.

---

ESP

# 🎯 Objetivo

Este repositorio contiene un framework de automatización de pruebas end-to-end para la aplicación bancaria demo [ParaBank](https://parabank.parasoft.com), utilizando:

* ✅ Selenium WebDriver
* ✅ Pytest
* ✅ Page Object Model (POM)
* ✅ Automatización UI
* ✅ Reportes HTML automáticos

El objetivo es validar funcionalidades críticas del sistema bancario de forma reproducible y mantenible.

Entre ellas:

* Login de usuarios
* Registro de cuentas
* Visualización de cuentas bancarias
* Apertura de nuevas cuentas
* Transferencias entre cuentas
* Validaciones de formularios y mensajes de error

---

## 📝 Documentación de Pruebas Manuales

* [Casos de prueba manuales y exploratorios](https://docs.google.com/spreadsheets/d/1Y6SNjHjeQ5mN3Z1oCo8Gp-3OE2-S-Jf9Gco2HFdXYKA/edit?usp=sharing)

---

## 🧰 Tecnologías

* Python 3.11+
* Selenium WebDriver
* Pytest
* Pytest-HTML
* WebDriver Manager

---

## ⚙️ Requisitos previos

Tener instalado:

* Google Chrome
* Python 3.11+
* Git

---

## 🐍 Setup del entorno

Clonar el repositorio:

```bash
git clone https://github.com/your-username/parabank-qa.git
cd parabank-qa
```

Crear y activar entorno virtual:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar tests

Correr todos los tests:

```bash
pytest
```

Correr un archivo específico:

```bash
pytest tests/test_login.py
```

Correr un test puntual:

```bash
pytest tests/test_login.py::test_login_valid_user
```

Modo verbose:

```bash
pytest -v
```

Ejecutar sin reporte HTML:

```bash
pytest --no-header -p no:html
```

El reporte HTML se genera automáticamente en:

```bash
reports/report.html
```

---

## 🧪 Cobertura de pruebas

### Login

* Validación de login exitoso
* Validación de campos vacíos
* Verificación de mensajes de error

### Registro

* Registro exitoso de nuevos usuarios
* Validación de usuario duplicado
* Validación de campos obligatorios

### Accounts Overview

* Visualización correcta de cuentas
* Verificación de links de cuentas
* Apertura de cuentas CHECKING y SAVINGS

### Transferencias

* Transferencia entre cuentas
* Validación del monto transferido
* Confirmación de transferencia exitosa

---

## 🧱 Arquitectura del proyecto

El proyecto utiliza el patrón **Page Object Model (POM)** para separar la lógica de automatización de la lógica de pruebas.

Estructura principal:

```bash
parabank-qa/
├── locators/
├── pages/
├── tests/
├── test_data/
├── utils/
├── reports/
├── conftest.py
├── pytest.ini
└── requirements.txt
```

### Componentes principales

#### `pages/`

Contiene las clases Page Object encargadas de encapsular las interacciones con cada pantalla.

#### `locators/`

Contiene los selectores de elementos agrupados por página.

#### `tests/`

Contiene los escenarios automatizados implementados con pytest.

#### `utils/`

Funciones reutilizables como:

* Configuración del driver
* Waits explícitos
* Configuración global

---

## 🧩 Fixtures importantes

### `driver`

* Inicializa una sesión de Chrome
* Abre la aplicación
* Cierra el navegador al finalizar el test

### `logged_in_driver`

* Extiende el fixture `driver`
* Realiza login automático antes de ejecutar pruebas autenticadas

---

## 🚀 CI/CD

El proyecto está preparado para ejecutarse automáticamente mediante **GitHub Actions**.

Incluye:

* Ejecución automática en pushes y pull requests
* Soporte para ejecución headless en CI
* Generación automática de reportes HTML
* Upload de artifacts del reporte

---

## 🧼 Buenas prácticas usadas

* Uso de Page Object Model (POM)
* Esperas explícitas para mayor estabilidad
* Fixtures reutilizables
* Separación de responsabilidades
* Tests independientes
* Estructura escalable y mantenible

---

## 🚀 Posibles mejoras futuras

* Integración con Allure Reports
* Data-driven testing
* Cross-browser testing
* Dockerización del entorno
* Integración con Selenium Grid

---

## 👨‍💻 Autor

Proyecto creado por Martin Osuna como práctica de QA Automation utilizando Python, Selenium WebDriver y testing end-to-end.
