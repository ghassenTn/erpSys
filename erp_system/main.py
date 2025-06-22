import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QMenuBar, QStatusBar
from PyQt6.QtGui import QAction

class ERPMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comprehensive ERP System")
        self.setGeometry(100, 100, 1200, 800)

        # Central Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Tab Widget for Modules
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

from PyQt6.QtCore import QSize # Import QSize

# ... (other imports)

class ERPMainWindow(QMainWindow):
    # ... (__init__ method)
        # Create Menu Bar
        self._create_menu_bar()

        # Create Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTabWidget, QMenuBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTabWidget, QMenuBar, QStatusBar, QStyle
import importlib.util # For dynamic module loading
import os
from utils.database import init_db # Import the database initialization function
from utils.styles import get_base_stylesheet # Import the stylesheet

# Define paths for different types of modules
CORE_MODULES_DIR = os.path.join(os.path.dirname(__file__), "modules", "core")
ADVANCED_MODULES_DIR = os.path.join(os.path.dirname(__file__), "modules", "advanced")
MODULE_DIRECTORIES = [CORE_MODULES_DIR, ADVANCED_MODULES_DIR]

class ERPMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comprehensive ERP System")
        self.setGeometry(100, 100, 1200, 800)

        # Apply Stylesheet
        self.setStyleSheet(get_base_stylesheet())

        # Central Widget and Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Tab Widget for Modules
        self.tab_widget = QTabWidget()
        self.tab_widget.setIconSize(QSize(24, 24)) # Set icon size for tabs
        self.layout.addWidget(self.tab_widget)

        # Create Menu Bar
        self._create_menu_bar()

        # Create Status Bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

        # Load initial modules
        self._load_modules()

    def get_icon_for_module(self, module_name: str) -> QIcon:
        """Returns a QIcon for a given module name."""
        # Using QStyle standard pixmaps for simplicity
        # These are somewhat generic, but better than nothing.
        # You might want to use custom icons for a more polished look.
        style = self.style() # or QApplication.style()

        if "Finance" in module_name:
            return style.standardIcon(QStyle.StandardPixmap.SP_FileDialogDetailedView)
        elif "HRM" in module_name or "Human" in module_name:
            return style.standardIcon(QStyle.StandardPixmap.SP_ContactsView)
        elif "Inventory" in module_name:
            return style.standardIcon(QStyle.StandardPixmap.SP_ListView)
        elif "Document" in module_name:
            return style.standardIcon(QStyle.StandardPixmap.SP_FileIcon)
        elif "Sales" in module_name:
            return style.standardIcon(QStyle.StandardPixmap.SP_DialogYesButton) # Placeholder
        elif "Procurement" in module_name or "Purchase" in module_name:
            return style.standardIcon(QStyle.StandardPixmap.SP_ArrowRight) # Placeholder
        # Add more mappings as needed
        else:
            return style.standardIcon(QStyle.StandardPixmap.SP_ComputerIcon) # Default icon

    def _create_menu_bar(self):
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu("&File")
        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # View Menu
        view_menu = menu_bar.addMenu("&View")
        # Add view options later, e.g., toggle module visibility

        # Help Menu
        help_menu = menu_bar.addMenu("&Help")
        about_action = QAction("&About", self)
        # about_action.triggered.connect(self.show_about_dialog) # To be implemented
        help_menu.addAction(about_action)

    def _load_modules(self):
        """Dynamically loads modules from predefined module directories."""
        loaded_modules_count = 0
        for module_dir_path in MODULE_DIRECTORIES:
            if not os.path.exists(module_dir_path):
                print(f"Module directory not found: {module_dir_path}")
                continue

            # Determine the base package name based on the directory (e.g., "modules.core" or "modules.advanced")
            base_package_name = "modules." + os.path.basename(module_dir_path)

            for filename in os.listdir(module_dir_path):
                if filename.endswith("_module.py") and filename != "__init__.py":
                    module_name_to_load = filename[:-3]  # Remove .py
                    module_full_path = os.path.join(module_dir_path, filename)
                    module_import_name = f"{base_package_name}.{module_name_to_load}"

                    try:
                        spec = importlib.util.spec_from_file_location(module_import_name, module_full_path)
                        if spec and spec.loader:
                            module = importlib.util.module_from_spec(spec)
                            # Add to sys.modules so it can be imported by other modules if needed
                            sys.modules[module_import_name] = module
                            spec.loader.exec_module(module)

                            if hasattr(module, 'get_module_ui') and hasattr(module, 'get_module_name'):
                                module_ui = module.get_module_ui()
                                module_tab_name = module.get_module_name()

                                # Get a standard icon based on module name (example)
                                icon = self.get_icon_for_module(module_tab_name)
                                self.tab_widget.addTab(module_ui, icon, module_tab_name)

                                print(f"Successfully loaded module: {module_tab_name} (from {os.path.basename(module_dir_path)})")
                                loaded_modules_count +=1
                            else:
                                print(f"Module {module_name_to_load} from {filename} does not have get_module_ui or get_module_name function.")
                        else:
                            print(f"Could not create spec for module: {module_name_to_load} from {filename}")
                    except Exception as e:
                        print(f"Error loading module {module_name_to_load} from {filename}: {e}")

        if loaded_modules_count > 0:
            self.status_bar.showMessage(f"Loaded {loaded_modules_count} module(s).")
        else:
            self.status_bar.showMessage("No modules loaded. Check console for errors.")

        # Remove dummy tabs if any were there previously
        # For now, we are dynamically loading, so the old dummy tabs are not needed.
        # If you want to keep some default tabs or handle errors gracefully,
        # you might need a more sophisticated tab management.

        # Example of a remaining dummy tab (if needed, or remove this section)
        # This will now be loaded if an inventory_module.py is created.
        # The old placeholder for Inventory Management is now removed,
        # as it will be picked up by the dynamic loader if inventory_module.py exists.


if __name__ == "__main__":
    # Ensure the erp_system directory is in PYTHONPATH if running from outside
    # For simplicity, when running main.py directly, its directory is usually in path.

    # Initialize the database at startup
    init_db()

    app = QApplication(sys.argv)
    main_window = ERPMainWindow()
    main_window.show()
    sys.exit(app.exec())
