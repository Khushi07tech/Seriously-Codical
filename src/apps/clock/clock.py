"""
Module: Unified Clock Suite
Purpose: An aggregator application that hosts a Digital Clock, Stopwatch,
         and Alarm using a QStackedWidget for seamless navigation.
Architecture: Container-Based Dashboard using modular class imports.
Standard: Seriously_Codical
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QLabel, QPushButton,
                             QWidget, QStackedWidget)
from PyQt5.QtCore import Qt
from digital_clock import Digital_Clock
from stopwatch import Stopwatch
from alarm_clock import Alarm_Clock


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seriously_Codical Clock Suite")

        # Core UI Elements
        self.ui_label = QLabel("🎀 CLOCK 🎀", self)
        self.digital_clock_button = QPushButton("View Clock")
        self.stopwatch_button = QPushButton("Stopwatch")
        self.alarm_button = QPushButton("Set Alarm")

        self.initUI()

    def initUI(self):
        # Main Layout Setup
        self.ui_label.setAlignment(Qt.AlignCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(self.ui_label)

        # Navigation Bar
        hbox = QHBoxLayout()
        hbox.addWidget(self.digital_clock_button)
        hbox.addWidget(self.stopwatch_button)
        hbox.addWidget(self.alarm_button)
        vbox.addLayout(hbox)

        # The Stacked Widget (The "Pages" of our app)
        self.stack = QStackedWidget()
        self.digital_screen = Digital_Clock()
        self.stopwatch_screen = Stopwatch()
        self.alarm_screen = Alarm_Clock()

        self.stack.addWidget(self.digital_screen)
        self.stack.addWidget(self.stopwatch_screen)
        self.stack.addWidget(self.alarm_screen)

        self.stack.hide()  # Keep hidden until a button is pressed
        vbox.addWidget(self.stack)

        vbox.setContentsMargins(50, 50, 50, 50)
        vbox.setSpacing(20)
        hbox.setSpacing(30)

        # Container Widget
        central_widget = QWidget(self)
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        # Global Application Styling
        self.setStyleSheet("""
            QPushButton, QLabel{
                font-family: 'Times New Roman';    
            }
            QLabel{
                font-size: 50px;
                padding: 50px;
                color: hsl(295, 36%, 20%);
                background-color: hsl(295, 36%, 60%);
                border-radius: 20px;
            }
            QPushButton{
                font-size: 30px;
                padding: 15px 25px;
                border-radius: 15px;
                background-color: hsl(295, 36%, 64%);
                color: hsl(295, 36%, 20%);
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: hsl(295, 40%, 80%);
            }
            """)

        # Connect signals with Lambda to pass the specific index to the handler
        self.digital_clock_button.clicked.connect(lambda: self.show_screen(0))
        self.stopwatch_button.clicked.connect(lambda: self.show_screen(1))
        self.alarm_button.clicked.connect(lambda: self.show_screen(2))

    def show_screen(self, index):
        """Switches the current view and adjusts global UI components."""
        self.stack.setCurrentIndex(index)
        self.stack.show()
        self.ui_label.hide()  # Hides the welcome banner to maximize utility space


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()