from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QFormLayout

class InventoryModuleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        # Item Master Section
        item_master_group = QGroupBox("Item Master")
        item_master_layout = QFormLayout()
        item_master_layout.addRow(QLabel("Product Catalog:"), QLabel("[Placeholder]"))
        item_master_layout.addRow(QLabel("Item Categories:"), QLabel("[Placeholder]"))
        item_master_layout.addRow(QLabel("Pricing Information:"), QLabel("[Placeholder]"))
        item_master_group.setLayout(item_master_layout)
        self.main_layout.addWidget(item_master_group)

        # Stock Levels Section
        stock_levels_group = QGroupBox("Stock Levels & Control")
        stock_levels_layout = QFormLayout()
        stock_levels_layout.addRow(QLabel("Current Stock:"), QLabel("[Placeholder]"))
        stock_levels_layout.addRow(QLabel("Stock Movements:"), QLabel("[Placeholder]"))
        stock_levels_layout.addRow(QLabel("Reorder Points:"), QLabel("[Placeholder]"))
        stock_levels_group.setLayout(stock_levels_layout)
        self.main_layout.addWidget(stock_levels_group)

        # Purchase Orders Section
        po_group = QGroupBox("Purchase Orders (Procurement Link)")
        po_layout = QFormLayout()
        po_layout.addRow(QLabel("View Purchase Orders:"), QLabel("[Placeholder]"))
        po_layout.addRow(QLabel("Receive Goods:"), QLabel("[Placeholder]"))
        po_group.setLayout(po_layout)
        self.main_layout.addWidget(po_group)

        # Sales Orders Section
        so_group = QGroupBox("Sales Orders (Sales Link)")
        so_layout = QFormLayout()
        so_layout.addRow(QLabel("View Sales Orders:"), QLabel("[Placeholder]"))
        so_layout.addRow(QLabel("Dispatch Goods:"), QLabel("[Placeholder]"))
        so_group.setLayout(so_layout)
        self.main_layout.addWidget(so_group)

        self.main_layout.addStretch()

def get_module_ui():
    """Returns the UI component for this module."""
    return InventoryModuleUI()

def get_module_name():
    """Returns the display name for this module."""
    return "Inventory Management"
