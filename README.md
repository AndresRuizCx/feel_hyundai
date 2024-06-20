### Descripción de Carpetas y Archivos

- **`main.py`**: El punto de entrada principal de la aplicación. Contiene el código necesario para iniciar y ejecutar la aplicación.

- **`README.md`**: Este archivo. Proporciona información sobre el proyecto, incluyendo su estructura, instalación y uso.

- **`requirements.txt`**: Lista de dependencias del proyecto. Utilizado por `pip` para instalar todas   las bibliotecas necesarias.

- **`config/`**:
  - **`settings.py`**: Archivo de configuración del proyecto. Contiene parámetros de configuración globales que pueden ser utilizados en toda la aplicación.

- **`data/`**:
  - **`fetcher.py`**: Contiene la clase `DataFetcher`, que se encarga de la obtención de datos desde diversas fuentes (APIs, bases de datos, etc.).

- **`models/`**:
  - **`__init__.py`**: Archivo necesario para que Python trate este directorio como un módulo.
  - **`base.py`**: Define las clases base o abstractas para los modelos de datos utilizados en el proyecto.

- **`services/`**:
  - **`__init__.py`**: Archivo necesario para que Python trate este directorio como un módulo.
  - **`report_generator.py`**: Contiene la clase `ReportGenerator`, que maneja la lógica de negocio para la generación de reportes basados en los datos obtenidos.

- **`interfaces/`**:
  - **`__init__.py`**: Archivo necesario para que Python trate este directorio como un módulo.
  - **`workable.py`**: Define la interfaz `Workable`.
  - **`eatable.py`**: Define la interfaz `Eatable`.
  - **`database.py`**: Define la interfaz `Database`. Estas interfaces se utilizan para asegurar que las clases implementen ciertos métodos específicos.

- **`tests/`**:
  - **`__init__.py`**: Archivo necesario para que Python trate este directorio como un módulo.
  - **`test_fetcher.py`**: Contiene las pruebas unitarias para el `DataFetcher`.
  - **`test_report_generator.py`**: Contiene las pruebas unitarias para el `ReportGenerator`.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/my_project.git
   cd my_project

