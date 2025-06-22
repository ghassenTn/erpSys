# Comprehensive ERP System (PyQt6 Demo)

This project is a demonstration of a comprehensive Enterprise Resource Planning (ERP) system built using Python and the PyQt6 GUI framework. It showcases a modular design allowing for various business functions to be managed within a single application.

## Project Structure

-   `main.py`: The main entry point for the application. Initializes the UI, loads modules, and starts the event loop.
-   `modules/`: Contains the different ERP modules.
    -   `core/`: Houses essential modules like Finance, HRM, Inventory.
    -   `advanced/`: Houses optional or industry-specific modules like Document Management.
    -   Each `*_module.py` file typically provides `get_module_ui()` and `get_module_name()` functions for dynamic loading.
-   `ui/`: Intended for UI files (e.g., `.ui` from Qt Designer), though not extensively used in this iteration.
-   `utils/`: Contains utility scripts.
    -   `database.py`: Handles SQLite database connection, schema initialization, and basic operations.
    -   `styles.py`: Provides the application's stylesheet.
-   `tests/`: Contains unit tests.
    -   `test_database_utils.py`: Unit tests for database functionalities.
-   `database/`: Directory where the `erp_main.db` SQLite database file is stored (created automatically).

## Features (Current Implementation)

*   **Modular Design**: Core and Advanced modules are loaded dynamically at runtime.
    *   **Core Modules (Basic UI Structure)**:
        *   Accounting & Finance
        *   Human Resources (HRM) - Includes a basic DB data loading example.
        *   Inventory Management
    *   **Advanced Modules (Basic UI Structure)**:
        *   Document Management
*   **Database Integration**: Uses SQLite for data persistence.
    *   Initial schema for Employees and Journal Entries.
    *   Database is initialized on application startup.
*   **UI/UX**:
    *   Basic custom styling applied for a consistent look and feel.
    *   Icons for module tabs.
*   **Testing**:
    *   Unit tests for database utility functions.

## Setup and Running

### Prerequisites

*   Python 3.x
*   PyQt6

### Installation

1.  **Clone the repository (or ensure files are in `erp_system` directory):**
    ```bash
    # If this were a git repo:
    # git clone <repository_url>
    # cd erp_system
    ```

2.  **Install dependencies:**
    It's highly recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install PyQt6
    ```

### Running the Application

Navigate to the `erp_system` directory and run:

```bash
python main.py
```
This will launch the ERP application window. The SQLite database `database/erp_main.db` will be created if it doesn't exist.

### Running Tests

From the `erp_system` root directory, run:

```bash
python -m unittest tests/test_database_utils.py
```
Or, to discover all tests (if more test files are added):
```bash
python -m unittest discover tests
```

## Further Development Ideas

*   Implement full CRUD (Create, Read, Update, Delete) operations for each module.
*   Design and implement detailed database schemas for all modules.
*   Develop actual business logic within each module.
*   Add more sophisticated UI components (e.g., tables, forms with validation, charts).
*   Implement user authentication and authorization.
*   Expand on advanced modules and add more industry-specific ones.
*   Improve error handling and logging.
*   Package the application for distribution.

## Packaging for Distribution (Conceptual)

To create a standalone executable for this application (so users don't need to install Python or PyQt6 separately), you can use tools like:

*   **PyInstaller**: A popular choice for freezing Python applications into stand-alone executables for Windows, Linux, macOS, and more. It analyzes your script and bundles all necessary files.
    *   Example basic usage: `pyinstaller --onefile --windowed main.py`
*   **cx_Freeze**: Another cross-platform tool for freezing Python scripts into executables.
*   **Briefcase (BeeWare)**: Part of the BeeWare suite, aims to help package applications for various platforms, including mobile.

The general process involves:
1.  Installing the packaging tool (e.g., `pip install pyinstaller`).
2.  Running the tool against your main script (`main.py`).
3.  Configuring options (e.g., one-file vs. one-directory bundle, including data files, icons).
4.  Testing the generated executable on target platforms.

Note that packaging PyQt applications can sometimes require careful handling of dependencies, data files (like images or stylesheets if not embedded), and platform-specific considerations. The `database/` directory would also need to be handled correctly by the packager or the application logic would need to ensure it can create it in a user-writable location.

---
This README provides a basic overview. As the project grows, more detailed documentation for each module and functionality would be necessary.
