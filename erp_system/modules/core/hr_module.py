from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QFormLayout, QPushButton, QTextEdit
from utils.database import get_db_connection # Import database utility
import sqlite3

class HRModuleUI(QWidget):
    """
    UI class for the Human Resources (HRM) module.
    Provides sections for Employee Management, Payroll, Recruitment, and Performance.
    Includes a basic example of loading employee data from the database.
    """
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        # Employee Management Section
        employee_group = QGroupBox("Employee Management")
        employee_layout = QVBoxLayout() # Changed to QVBoxLayout for more flexibility

        self.employee_data_display = QTextEdit()
        self.employee_data_display.setReadOnly(True)
        self.employee_data_display.setPlaceholderText("Employee data will be shown here...")

        load_button = QPushButton("Load Employees (Test DB)")
        load_button.clicked.connect(self.load_employee_data)

        form_layout = QFormLayout() # For other fields if needed
        form_layout.addRow(QLabel("Employee Database:"), QLabel("[Placeholder for forms/tables]"))
        form_layout.addRow(QLabel("Attendance Tracking:"), QLabel("[Placeholder]"))
        form_layout.addRow(QLabel("Leave Management:"), QLabel("[Placeholder]"))

        employee_layout.addLayout(form_layout)
        employee_layout.addWidget(load_button)
        employee_layout.addWidget(self.employee_data_display)
        employee_group.setLayout(employee_layout)
        self.main_layout.addWidget(employee_group)

        # Payroll Section
        payroll_group = QGroupBox("Payroll")
        payroll_layout = QFormLayout()
        payroll_layout.addRow(QLabel("Process Salaries:"), QLabel("[Placeholder]"))
        payroll_layout.addRow(QLabel("Tax Calculations:"), QLabel("[Placeholder]"))
        payroll_layout.addRow(QLabel("Payslip Generation:"), QLabel("[Placeholder]"))
        payroll_group.setLayout(payroll_layout)
        self.main_layout.addWidget(payroll_group)

        # Recruitment Section
        recruitment_group = QGroupBox("Recruitment")
        recruitment_layout = QFormLayout()
        recruitment_layout.addRow(QLabel("Job Postings:"), QLabel("[Placeholder]"))
        recruitment_layout.addRow(QLabel("Applicant Tracking:"), QLabel("[Placeholder]"))
        recruitment_layout.addRow(QLabel("Interview Scheduling:"), QLabel("[Placeholder]"))
        recruitment_group.setLayout(recruitment_layout)
        self.main_layout.addWidget(recruitment_group)

        # Performance Management Section
        performance_group = QGroupBox("Performance Management")
        performance_layout = QFormLayout()
        performance_layout.addRow(QLabel("Appraisal Cycles:"), QLabel("[Placeholder]"))
        performance_layout.addRow(QLabel("Goal Setting:"), QLabel("[Placeholder]"))
        performance_group.setLayout(performance_layout)
        self.main_layout.addWidget(performance_group)

        self.main_layout.addStretch() # Add stretch to push content to the top

    def load_employee_data(self):
        """
        Fetches employee data from the database and displays it in the
        employee_data_display QTextEdit widget.
        This is a basic demonstration of database interaction.
        """
        self.employee_data_display.clear()
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT id, first_name, last_name, email, position FROM employees ORDER BY last_name, first_name")
                employees = cursor.fetchall()
                if employees:
                    self.employee_data_display.append("ID | Name | Email | Position")
                    self.employee_data_display.append("-" * 50)
                    for emp in employees:
                        self.employee_data_display.append(f"{emp['id']} | {emp['first_name']} {emp['last_name']} | {emp['email']} | {emp['position']}")
                else:
                    self.employee_data_display.append("No employees found in the database.")
            except sqlite3.Error as e:
                self.employee_data_display.append(f"Database error: {e}")
            finally:
                conn.close()
        else:
            self.employee_data_display.append("Failed to connect to the database.")


def get_module_ui():
    """Returns the UI component for this module."""
    return HRModuleUI()

def get_module_name():
    """Returns the display name for this module."""
    return "Human Resources (HRM)"
