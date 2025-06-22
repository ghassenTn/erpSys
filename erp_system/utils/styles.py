# erp_system/utils/styles.py

def get_base_stylesheet():
    """Returns a base stylesheet for the application."""
    return """
        QMainWindow {
            background-color: #f0f0f0; /* Light gray background for the main window */
        }
        QTabWidget::pane { /* The tab widget frame */
            border-top: 2px solid #C2C7CB;
            background-color: #ffffff; /* White background for tab content area */
        }
        QTabBar::tab { /* The tab bar buttons */
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                        stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
            border: 1px solid #C4C4C3;
            border-bottom-color: #C2C7CB; /* Same as pane border color */
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            min-width: 8ex;
            padding: 5px 10px; /* Increased padding for better spacing */
            margin-right: 2px; /* Space between tabs */
        }
        QTabBar::tab:selected, QTabBar::tab:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #fafafa, stop: 0.4 #f4f4f4,
                                        stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);
        }
        QTabBar::tab:selected {
            border-color: #9B9B9B;
            border-bottom-color: #C2C7CB; /* Same as pane border color */
        }
        QTabBar::tab:!selected {
            margin-top: 2px; /* Make non-selected tabs look slightly recessed */
        }
        QGroupBox {
            background-color: #f7f7f7; /* Slightly off-white for group boxes */
            border: 1px solid #cccccc;
            border-radius: 5px;
            margin-top: 1ex; /* Margin above the group box title */
            padding-top: 1ex; /* Padding above the content, below title */
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left; /* Position at the top-left */
            padding: 0 3px 0 3px;
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f0f0f0, stop:1 #e0e0e0);
            border-radius: 3px;
            color: #333333; /* Darker text for title for contrast */
        }
        QPushButton {
            background-color: #4CAF50; /* Green */
            border: 1px solid #3e8e41;
            color: white;
            padding: 6px 12px;
            text-align: center;
            text-decoration: none;
            font-size: 10pt;
            border-radius: 4px;
            margin: 2px;
        }
        QPushButton:hover {
            background-color: #45a049; /* Darker Green */
        }
        QPushButton:pressed {
            background-color: #3e8e41;
        }
        QLineEdit, QTextEdit, QSpinBox { /* General input fields */
            background-color: #ffffff;
            border: 1px solid #cccccc;
            border-radius: 3px;
            padding: 4px;
            color: #333333;
        }
        QTextEdit {
             background-color: #fdfdfd; /* Slightly different for larger text areas */
        }
        QLabel {
            color: #333333; /* Standard text color */
            padding: 2px;
        }
        QStatusBar {
            background-color: #e0e0e0; /* Status bar background */
            color: #333333;
        }
        QMenuBar {
            background-color: #e8e8e8;
        }
        QMenuBar::item {
            background: transparent;
            padding: 4px 8px;
        }
        QMenuBar::item:selected { /* When selected using mouse or keyboard */
            background: #d0d0d0;
        }
        QMenu {
            background-color: #f0f0f0; /* Background of menu */
            border: 1px solid #cacaca;
        }
        QMenu::item:selected {
            background-color: #4CAF50; /* Green selection in menus */
            color: white;
        }
    """
