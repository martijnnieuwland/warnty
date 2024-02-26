import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QTextEdit, QAction, QMenu
from random import choice
# from ui_warnty import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(self.mapToGlobal(pos))

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
