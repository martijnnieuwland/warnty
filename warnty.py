from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("warnty")
        self.setMinimumSize(400, 300)
        self.setMaximumSize(1200, 800)
        button = QPushButton("Press me!")

        self.setCentralWidget(button)


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
