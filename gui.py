import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QPushButton, QLabel

import RPi.GPIO as GPIO

class Application(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        self.RED_PIN = 18
        self.GREEN_PIN = 23
        self.BLUE_PIN = 24
        GPIO.setup(self.RED_PIN, GPIO.OUT)
        GPIO.setup(self.GREEN_PIN, GPIO.OUT)
        GPIO.setup(self.BLUE_PIN, GPIO.OUT)

    def exit(self):
        GPIO.cleanup()
        self.close()

    def toggle(self):
        action = self.selected_led
        GPIO.output(self.RED_PIN, GPIO.LOW)
        GPIO.output(self.GREEN_PIN, GPIO.LOW)
        GPIO.output(self.BLUE_PIN, GPIO.LOW)

        if action == 'red':
            GPIO.output(self.RED_PIN, GPIO.HIGH)
        elif action == 'green':
            GPIO.output(self.GREEN_PIN, GPIO.HIGH)
        else:
            GPIO.output(self.BLUE_PIN, GPIO.HIGH)

    def initUI(self):
        self.setWindowTitle('SIT210 5.1P')
        self.resize(350, 250)


        # Add Task name label
        self.label = QLabel('Task 5.1P - RPi Making GUI', self)
        self.label.setStyleSheet("font: bold 18pt Helvetica;")

        # Add buttons
        self.radio_group = QVBoxLayout() 

        self.radio_red = QRadioButton('Red', self)
        self.radio_red.setChecked(True)
        self.radio_red.toggled.connect(lambda: self.update_selected_led('red'))

        self.radio_green = QRadioButton('Green', self)
        self.radio_green.toggled.connect(lambda: self.update_selected_led('green'))

        self.radio_blue = QRadioButton('Blue', self)
        self.radio_blue.toggled.connect(lambda: self.update_selected_led('blue'))

        self.radio_group.addWidget(self.radio_red)
        self.radio_group.addWidget(self.radio_green)
        self.radio_group.addWidget(self.radio_blue)

        # Add Exit button
        
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.exit)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(self.radio_group)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

        # Initialize selected LED
        self.selected_led = 'red'

    def update_selected_led(self, led):
        self.selected_led = led
        self.toggle()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())

