from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QGridLayout, QVBoxLayout, QHBoxLayout, QLineEdit, QSizePolicy
)
from PySide6.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()

        # App Settings
        self.setWindowTitle("Calculator")
        self.resize(300, 400)

        # Font & Widget Setup
        self.setFont(QFont("Segoe UI", 12))
        self.text_box = QLineEdit()
        self.text_box.setReadOnly(True)
        self.text_box.setStyleSheet("""
            QLineEdit {
                font: 24pt 'Segoe UI';
                padding: 15px;
                border-radius: 10px;
                background-color: #ffffff;
                color: #333;
            }
        """)

        self.grid = QGridLayout()

        # Button Texts
        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Grid Layout: Add number/symbol buttons
        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked=False, t=text: self.button_click(t))
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.setStyleSheet("""
                QPushButton {
                    font: 18pt 'Segoe UI';
                    padding: 20px;
                    border-radius: 10px;
                    background-color: #eeeeee;
                    color: #222;
                }
                QPushButton:hover {
                    background-color: #dcdcdc;
                }
            """)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear and Delete Buttons
        self.clear_button = QPushButton("Clear")
        self.delete_button = QPushButton("Del")
        for btn in (self.clear_button, self.delete_button):
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.setStyleSheet("""
                QPushButton {
                    font: 16pt 'Segoe UI';
                    padding: 12px;
                    border-radius: 10px;
                    background-color: #f08080;
                    color: white;
                }
                QPushButton:hover {
                    background-color: #d66;
                }
            """)

        # Layouts
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear_button)
        button_row.addWidget(self.delete_button)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(20, 20, 20, 20)
        master_layout.setSpacing(15)

        # Connect clear and delete buttons
        self.clear_button.clicked.connect(lambda: self.button_click("clear"))
        self.delete_button.clicked.connect(lambda: self.button_click("del"))

        self.setLayout(master_layout)

    # Function to handle button clicks
    def button_click(self, text):
        if text == "=":
            try:
                expression = self.text_box.text()
                result = eval(expression)
                self.text_box.setText(str(result))
            except Exception as e:
                self.text_box.setText("Error")
        elif text == "clear":
            self.text_box.clear()
        elif text == "del":
            current = self.text_box.text()
            self.text_box.setText(current[:-1])
        else:
            current = self.text_box.text()
            self.text_box.setText(current + text)

# Finalize and run
if __name__ == "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.setStyleSheet("QWidget { background-color: #f0f0f0; }")
    main_window.show()
    app.exec()
