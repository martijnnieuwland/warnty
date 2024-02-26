# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warnty.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFormLayout,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QSplitter, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1037, 763)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dateEdit)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBox)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.widget)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 403))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.scrollArea)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Manufacturer", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Product", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Purchase date", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Warranty years", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Proof of Purchase", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Remarks", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
    # retranslateUi

