from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
import sys
from random import choice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("warnty")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
# class DlgMain(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My GUI")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dlgMain = DlgMain()
#     dlgMain.show()
#     sys.exit(app.exec_())


# One window to enter new warranty information

# A widget to enter the product name

# A widget to enter purchase date

# A widget to enter warranty duration

# A widget to calculate warranty expiration date

# Save and exit button

# Confirmation dialog with info about warning date
