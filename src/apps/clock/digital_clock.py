"""
Module: Retro Digital Clock
Purpose: A high-precision digital clock featuring custom font integration 
         and dynamic UI refreshing via QTimer.
Logic: Utilizes the PyQt5 Event Loop to poll system time every 1000ms, 
       rendering it with a custom digital-style typeface.
Standard: Seriously_Codical
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont, QFontDatabase


class Digital_Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(450, 150, 400, 150)

        # Ensure 'DS-DIGIT.TTF' is in the same directory as the script.
        try:
            font_id = QFontDatabase.addApplicationFont("../../../assets/DS-DIGIT.TTF")
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family, 100)
            self.time_label.setFont(my_font)
        except (IndexError, FileNotFoundError):
            # Fallback to system monospace if the custom font file is missing
            self.time_label.setFont(QFont("Courier", 100))

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        # Styling using high-contrast HSL values for better readability
        self.time_label.setStyleSheet("""
                                       font-size: 100px;
                                       color: hsl(295, 36%, 20%);
                                      """)
        self.setStyleSheet("background-color: hsl(295, 36%, 60%);")

        # Timer setup: Update the clock every 1 second (1000 ms)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Initial call to prevent a blank screen on startup
        self.update_time()

    def update_time(self):
        """Fetches the current system time and formats it for the display."""
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Digital_Clock()
    clock.show()
    sys.exit(app.exec_())