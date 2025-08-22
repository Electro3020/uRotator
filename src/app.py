from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
import sys
from controller import Controller

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = Controller((0, 90))
        self.controller.read_sensors()

        self.setWindowTitle("uRotator")

        layout = QVBoxLayout()

        self.rotatorIndicator = QLabel("Connecting...")
        layout.addWidget(self.rotatorIndicator)
        self.update_sensor_disp()

        self.lineedit = QLineEdit()
        self.lineedit.setMaxLength(3)
        self.lineedit.setPlaceholderText("Azi")
        layout.addWidget(self.lineedit)

        button = QPushButton("Set rotor")
        button.pressed.connect(self.press_rot)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()

    def update_sensor_disp(self):
        self.rotatorIndicator.setText(f"Azi: {self.controller.target_az}, Alt: {self.controller.target_al}")

    def press_rot(self):
        try:
            target = float(self.lineedit.text())
            if target > 360 or target < 0: return
        except: return

        self.controller.target_az = target

        self.update_sensor_disp()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()
