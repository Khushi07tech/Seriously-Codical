"""
Module: Precision Stopwatch
Purpose: A high-resolution stopwatch utilizing a 10ms polling interval
         to track time down to centiseconds.
Architecture: Uses QTime as a state object and QTimer as the ticking mechanism.
Standard: Seriously_Codical
"""

import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QHBoxLayout,
                             QVBoxLayout, QWidget, QPushButton)
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")

        # Core State: QTime holds our elapsed duration
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)

        # Controls
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        # High-frequency timer (10ms interval)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.time_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # HSL Styling for a clean, professional aesthetic
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: Times New Roman;
            }    
            QPushButton{
                font-size: 30px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
            }
            QPushButton:hover{
                background-color: #e0e0e0;
            }
            QLabel{
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
                color: #333;
            }
        """)

        # Connecting Signals to Slots
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        """Activates the timer if it isn't already running."""
        if not self.timer.isActive():
            self.timer.start(10)  # 10ms centisecond precision

    def stop(self):
        """Pauses the current timing state."""
        self.timer.stop()

    def reset(self):
        """Stops the timer and zeroes out the time object."""
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        """
        Custom formatting to extract hours, minutes, seconds, and centiseconds.
        The ':02' ensures zero-padding for a consistent UI layout.
        """
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10  # Convert ms to centiseconds
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_time(self):
        """Triggered every 10ms to advance the clock state."""
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())