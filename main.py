import json
import sys
import os
import wget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QFileDialog, QGraphicsBlurEffect
import MCSL2_Icon
from DownloadKit import DownloadKit
from MCSL2_Dialog import *
import subprocess


class Ui_MCSL2_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MCSL2_MainWindow):
        self.MCSL2_Window = MCSL2_MainWindow
        MCSL2_MainWindow.setObjectName("MCSL2_MainWindow")
        MCSL2_MainWindow.setFixedSize(944, 583)  # Make the size of window unchangeable.
        self._startPos = None
        self._endPos = None
        self._tracking = False
        MCSL2_MainWindow.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        MCSL2_MainWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(12)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        self.CentralWidget = QtWidgets.QWidget(MCSL2_MainWindow)
        self.CentralWidget.setObjectName("CentralWidget")
        self.OptionsWidget = QtWidgets.QWidget(self.CentralWidget)
        self.OptionsWidget.setGeometry(QtCore.QRect(0, 0, 211, 581))
        self.OptionsWidget.setObjectName("OptionsWidget")
        self.Close_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.Close_PushButton.setGeometry(QtCore.QRect(20, 20, 31, 23))
        self.Close_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Close_PushButton.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "    background-color: rgb(232, 17, 35);\n"
                                            "    border-radius: 11px;\n"
                                            "}\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "    background-color: rgb(193, 6, 16);\n"
                                            "    border-radius: 11px;\n"
                                            "}\n"
                                            "QPushButton:pressed\n"
                                            "{\n"
                                            "    background-color: rgb(170, 0, 0);\n"
                                            "    border-radius: 11px;\n"
                                            "}")
        self.Close_PushButton.setText("")
        self.Close_PushButton.setObjectName("Close_PushButton")
        self.Minimize_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.Minimize_PushButton.setGeometry(QtCore.QRect(60, 20, 31, 23))
        self.Minimize_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Minimize_PushButton.setStyleSheet("QPushButton\n"
                                               "{\n"
                                               "    background-color: rgb(225, 225, 0);\n"
                                               "    border-radius: 11px;\n"
                                               "}\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    background-color: rgb(161, 182, 0);\n"
                                               "    border-radius: 11px;\n"
                                               "}\n"
                                               "QPushButton:pressed\n"
                                               "{\n"
                                               "    background-color: rgb(161, 161, 0);\n"
                                               "    border-radius: 11px;\n"
                                               "}")
        self.Minimize_PushButton.setText("")
        self.Minimize_PushButton.setObjectName("Minimize_PushButton")
        self.Home_Page_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.Home_Page_PushButton.setGeometry(QtCore.QRect(20, 140, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.Home_Page_PushButton.setFont(font)
        self.Home_Page_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Home_Page_PushButton.setStyleSheet("QPushButton\n"
                                                "{\n"
                                                "    background-color: rgb(247, 247, 247);\n"
                                                "    border-radius: 7px;\n"
                                                "}\n"
                                                "QPushButton:hover\n"
                                                "{\n"
                                                "    background-color: rgb(230, 230, 230);\n"
                                                "    border-radius: 7px;\n"
                                                "}\n"
                                                "QPushButton:pressed\n"
                                                "{\n"
                                                "    background-color: rgb(225, 225, 225);\n"
                                                "    border-radius: 7px;\n"
                                                "}")
        self.Home_Page_PushButton.setObjectName("Home_Page_PushButton")
        self.Config_Page_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.Config_Page_PushButton.setGeometry(QtCore.QRect(20, 210, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.Config_Page_PushButton.setFont(font)
        self.Config_Page_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Config_Page_PushButton.setStyleSheet("QPushButton\n"
                                                  "{\n"
                                                  "    background-color: rgb(247, 247, 247);\n"
                                                  "    border-radius: 7px;\n"
                                                  "}\n"
                                                  "QPushButton:hover\n"
                                                  "{\n"
                                                  "    background-color: rgb(230, 230, 230);\n"
                                                  "    border-radius: 7px;\n"
                                                  "}\n"
                                                  "QPushButton:pressed\n"
                                                  "{\n"
                                                  "    background-color: rgb(225, 225, 225);\n"
                                                  "    border-radius: 7px;\n"
                                                  "}")
        self.Config_Page_PushButton.setObjectName("Config_Page_PushButton")
        self.MCSL2_Title_Label = QtWidgets.QLabel(self.OptionsWidget)
        self.MCSL2_Title_Label.setGeometry(QtCore.QRect(100, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.MCSL2_Title_Label.setFont(font)
        self.MCSL2_Title_Label.setObjectName("MCSL2_Title_Label")
        self.MCSL2_Title_Author_Label = QtWidgets.QLabel(self.OptionsWidget)
        self.MCSL2_Title_Author_Label.setGeometry(QtCore.QRect(100, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.MCSL2_Title_Author_Label.setFont(font)
        self.MCSL2_Title_Author_Label.setObjectName("MCSL2_Title_Author_Label")
        self.MCSL2_Title_Icon_Label = QtWidgets.QLabel(self.OptionsWidget)
        self.MCSL2_Title_Icon_Label.setGeometry(QtCore.QRect(20, 50, 71, 71))
        self.MCSL2_Title_Icon_Label.setText("")
        self.MCSL2_Title_Icon_Label.setPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"))
        self.MCSL2_Title_Icon_Label.setScaledContents(True)
        self.MCSL2_Title_Icon_Label.setObjectName("MCSL2_Title_Icon_Label")
        self.Download_Page_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.Download_Page_PushButton.setGeometry(QtCore.QRect(20, 280, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.Download_Page_PushButton.setFont(font)
        self.Download_Page_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Download_Page_PushButton.setStyleSheet("QPushButton\n"
                                                    "{\n"
                                                    "    background-color: rgb(247, 247, 247);\n"
                                                    "    border-radius: 7px;\n"
                                                    "}\n"
                                                    "QPushButton:hover\n"
                                                    "{\n"
                                                    "    background-color: rgb(230, 230, 230);\n"
                                                    "    border-radius: 7px;\n"
                                                    "}\n"
                                                    "QPushButton:pressed\n"
                                                    "{\n"
                                                    "    background-color: rgb(225, 225, 225);\n"
                                                    "    border-radius: 7px;\n"
                                                    "}")
        self.Download_Page_PushButton.setObjectName("Download_Page_PushButton")
        self.Server_Console_Page_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.Server_Console_Page_PushButton.setGeometry(QtCore.QRect(20, 350, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.Server_Console_Page_PushButton.setFont(font)
        self.Server_Console_Page_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Server_Console_Page_PushButton.setStyleSheet("QPushButton\n"
                                                          "{\n"
                                                          "    background-color: rgb(247, 247, 247);\n"
                                                          "    border-radius: 7px;\n"
                                                          "}\n"
                                                          "QPushButton:hover\n"
                                                          "{\n"
                                                          "    background-color: rgb(230, 230, 230);\n"
                                                          "    border-radius: 7px;\n"
                                                          "}\n"
                                                          "QPushButton:pressed\n"
                                                          "{\n"
                                                          "    background-color: rgb(225, 225, 225);\n"
                                                          "    border-radius: 7px;\n"
                                                          "}")
        self.Server_Console_Page_PushButton.setObjectName("Server_Console_Page_PushButton")
        self.Tools_Page_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.Tools_Page_PushButton.setGeometry(QtCore.QRect(20, 420, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.Tools_Page_PushButton.setFont(font)
        self.Tools_Page_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tools_Page_PushButton.setStyleSheet("QPushButton\n"
                                                 "{\n"
                                                 "    background-color: rgb(247, 247, 247);\n"
                                                 "    border-radius: 7px;\n"
                                                 "}\n"
                                                 "QPushButton:hover\n"
                                                 "{\n"
                                                 "    background-color: rgb(230, 230, 230);\n"
                                                 "    border-radius: 7px;\n"
                                                 "}\n"
                                                 "QPushButton:pressed\n"
                                                 "{\n"
                                                 "    background-color: rgb(225, 225, 225);\n"
                                                 "    border-radius: 7px;\n"
                                                 "}")
        self.Tools_Page_PushButton.setObjectName("Tools_Page_PushButton")
        self.About_Page_PushButton = QtWidgets.QPushButton(self.OptionsWidget)
        self.About_Page_PushButton.setGeometry(QtCore.QRect(20, 490, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.About_Page_PushButton.setFont(font)
        self.About_Page_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.About_Page_PushButton.setStyleSheet("QPushButton\n"
                                                 "{\n"
                                                 "    background-color: rgb(247, 247, 247);\n"
                                                 "    border-radius: 7px;\n"
                                                 "}\n"
                                                 "QPushButton:hover\n"
                                                 "{\n"
                                                 "    background-color: rgb(230, 230, 230);\n"
                                                 "    border-radius: 7px;\n"
                                                 "}\n"
                                                 "QPushButton:pressed\n"
                                                 "{\n"
                                                 "    background-color: rgb(225, 225, 225);\n"
                                                 "    border-radius: 7px;\n"
                                                 "}")
        self.About_Page_PushButton.setObjectName("About_Page_PushButton")
        self.FunctionsStackedWidget = QtWidgets.QStackedWidget(self.CentralWidget)
        self.FunctionsStackedWidget.setGeometry(QtCore.QRect(210, -20, 731, 601))
        self.FunctionsStackedWidget.setAutoFillBackground(False)
        self.FunctionsStackedWidget.setObjectName("FunctionsStackedWidget")
        self.HomePage = QtWidgets.QWidget()
        self.HomePage.setObjectName("HomePage")
        self.Config_PushButton = QtWidgets.QPushButton(self.HomePage)
        self.Config_PushButton.setGeometry(QtCore.QRect(600, 420, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Config_PushButton.setFont(font)
        self.Config_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Config_PushButton.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    background-color: rgb(247, 247, 247);\n"
                                             "    border-radius: 7px;\n"
                                             "}\n"
                                             "QPushButton:hover\n"
                                             "{\n"
                                             "    background-color: rgb(230, 230, 230);\n"
                                             "    border-radius: 7px;\n"
                                             "}\n"
                                             "QPushButton:pressed\n"
                                             "{\n"
                                             "    background-color: rgb(225, 225, 225);\n"
                                             "    border-radius: 7px;\n"
                                             "}")
        self.Config_PushButton.setObjectName("Config_PushButton")
        self.Choose_Server_PushButton = QtWidgets.QPushButton(self.HomePage)
        self.Choose_Server_PushButton.setGeometry(QtCore.QRect(480, 420, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Choose_Server_PushButton.setFont(font)
        self.Choose_Server_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Choose_Server_PushButton.setStyleSheet("QPushButton\n"
                                                    "{\n"
                                                    "    background-color: rgb(247, 247, 247);\n"
                                                    "    border-radius: 7px;\n"
                                                    "}\n"
                                                    "QPushButton:hover\n"
                                                    "{\n"
                                                    "    background-color: rgb(230, 230, 230);\n"
                                                    "    border-radius: 7px;\n"
                                                    "}\n"
                                                    "QPushButton:pressed\n"
                                                    "{\n"
                                                    "    background-color: rgb(225, 225, 225);\n"
                                                    "    border-radius: 7px;\n"
                                                    "}")
        self.Choose_Server_PushButton.setObjectName("Choose_Server_PushButton")
        self.Home_Label = QtWidgets.QLabel(self.HomePage)
        self.Home_Label.setGeometry(QtCore.QRect(30, 80, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Home_Label.setFont(font)
        self.Home_Label.setObjectName("Home_Label")
        self.Start_PushButton = QtWidgets.QPushButton(self.HomePage)
        self.Start_PushButton.setGeometry(QtCore.QRect(480, 490, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.Start_PushButton.setFont(font)
        self.Start_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_PushButton.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "    background-color: rgb(0, 120, 212);\n"
                                            "    border-radius: 10px;\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "}\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "    background-color: rgb(0, 110, 212);\n"
                                            "    border-radius: 10px;\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed\n"
                                            "{\n"
                                            "    background-color: rgb(0, 100, 212);\n"
                                            "    border-radius: 10px;\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "}")
        self.Start_PushButton.setFlat(False)
        self.Start_PushButton.setObjectName("Start_PushButton")
        self.Selected_Server_Label = QtWidgets.QLabel(self.HomePage)
        self.Selected_Server_Label.setGeometry(QtCore.QRect(490, 560, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.Selected_Server_Label.setFont(font)
        self.Selected_Server_Label.setObjectName("Selected_Server_Label")
        self.Notice_Label = QtWidgets.QLabel(self.HomePage)
        self.Notice_Label.setGeometry(QtCore.QRect(30, 140, 321, 141))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Notice_Label.setFont(font)
        self.Notice_Label.setAutoFillBackground(False)
        self.Notice_Label.setStyleSheet("QLabel\n"
                                        "{\n"
                                        "    background-color: rgb(247, 247, 247);\n"
                                        "    border-radius: 10px\n"
                                        "}")
        self.Notice_Label.setObjectName("Notice_Label")
        self.HomeTip1_Label = QtWidgets.QLabel(self.HomePage)
        self.HomeTip1_Label.setGeometry(QtCore.QRect(30, 300, 321, 181))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.HomeTip1_Label.setFont(font)
        self.HomeTip1_Label.setAutoFillBackground(False)
        self.HomeTip1_Label.setStyleSheet("QLabel\n"
                                          "{\n"
                                          "    background-color: rgb(247, 247, 247);\n"
                                          "    border-radius: 10px\n"
                                          "}")
        self.HomeTip1_Label.setObjectName("HomeTip1_Label")
        self.FunctionsStackedWidget.addWidget(self.HomePage)
        self.ConfigPage = QtWidgets.QWidget()
        self.ConfigPage.setObjectName("ConfigPage")
        self.Config_Label = QtWidgets.QLabel(self.ConfigPage)
        self.Config_Label.setGeometry(QtCore.QRect(30, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Config_Label.setFont(font)
        self.Config_Label.setObjectName("Config_Label")
        self.ConfigTip1_Label = QtWidgets.QLabel(self.ConfigPage)
        self.ConfigTip1_Label.setGeometry(QtCore.QRect(30, 140, 251, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.ConfigTip1_Label.setFont(font)
        self.ConfigTip1_Label.setAutoFillBackground(False)
        self.ConfigTip1_Label.setStyleSheet("QLabel\n"
                                            "{\n"
                                            "    background-color: rgb(247, 247, 247);\n"
                                            "    border-radius: 10px\n"
                                            "}")
        self.ConfigTip1_Label.setObjectName("ConfigTip1_Label")
        self.ConfigTip2_Label = QtWidgets.QLabel(self.ConfigPage)
        self.ConfigTip2_Label.setGeometry(QtCore.QRect(30, 280, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.ConfigTip2_Label.setFont(font)
        self.ConfigTip2_Label.setAutoFillBackground(False)
        self.ConfigTip2_Label.setStyleSheet("QLabel\n"
                                            "{\n"
                                            "    background-color: rgb(247, 247, 247);\n"
                                            "    border-radius: 10px\n"
                                            "}")
        self.ConfigTip2_Label.setObjectName("ConfigTip2_Label")
        self.Java_Label = QtWidgets.QLabel(self.ConfigPage)
        self.Java_Label.setGeometry(QtCore.QRect(350, 160, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Java_Label.setFont(font)
        self.Java_Label.setObjectName("Java_Label")
        self.Select_Java_ComboBox = QtWidgets.QComboBox(self.ConfigPage)
        self.Select_Java_ComboBox.setGeometry(QtCore.QRect(400, 160, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.Select_Java_ComboBox.setFont(font)
        self.Select_Java_ComboBox.setStyleSheet("QComboBox {\n"
                                                "    border-radius: 3px;\n"
                                                "    padding: 1px 2px 1px 2px;\n"
                                                "    min-width: 9em;\n"
                                                "    border: 2px solid rgb(223, 223, 223);\n"
                                                "}\n"
                                                "QComboBox::drop-down {\n"
                                                "    subcontrol-origin: padding;\n"
                                                "    subcontrol-position: top right;\n"
                                                "    width: 20px;\n"
                                                "    border-left-color: rgb(223, 223, 223);\n"
                                                "    border-left-style: solid;\n"
                                                "    border-top-right-radius: 4px;\n"
                                                "    border-bottom-right-radius: 4px;\n"
                                                "}\n"
                                                "QComboBox::down-arrow {\n"
                                                "    image: url(./resources/QComboBox.png);\n"
                                                "}\n"
                                                "QComboBox QAbstractItemView::item {\n"
                                                "    height: 25px;\n"
                                                "}\n"
                                                "QComboBox QAbstractItemView{\n"
                                                "    font-size: 18px;\n"
                                                "}")
        self.Select_Java_ComboBox.setObjectName("Select_Java_ComboBox")
        self.Select_Java_ComboBox.addItem("")
        self.Set_Java_Background = QtWidgets.QLabel(self.ConfigPage)
        self.Set_Java_Background.setGeometry(QtCore.QRect(330, 140, 351, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Set_Java_Background.setFont(font)
        self.Set_Java_Background.setAutoFillBackground(False)
        self.Set_Java_Background.setStyleSheet("QLabel\n"
                                               "{\n"
                                               "    background-color: rgb(247, 247, 247);\n"
                                               "    border-radius: 10px\n"
                                               "}")
        self.Set_Java_Background.setText("")
        self.Set_Java_Background.setObjectName("Set_Java_Background")
        self.Auto_Find_Java_PushButton = QtWidgets.QPushButton(self.ConfigPage)
        self.Auto_Find_Java_PushButton.setGeometry(QtCore.QRect(350, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Auto_Find_Java_PushButton.setFont(font)
        self.Auto_Find_Java_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Auto_Find_Java_PushButton.setStyleSheet("QPushButton\n"
                                                     "{\n"
                                                     "    background-color: rgb(0, 120, 212);\n"
                                                     "    border-radius: 6px;\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}\n"
                                                     "QPushButton:hover\n"
                                                     "{\n"
                                                     "    background-color: rgb(0, 110, 212);\n"
                                                     "    border-radius: 6px;\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}\n"
                                                     "QPushButton:pressed\n"
                                                     "{\n"
                                                     "    background-color: rgb(0, 100, 212);\n"
                                                     "    border-radius: 6px;\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}")
        self.Auto_Find_Java_PushButton.setFlat(False)
        self.Auto_Find_Java_PushButton.setObjectName("Auto_Find_Java_PushButton")
        self.Manual_Select_Java_PushButton = QtWidgets.QPushButton(self.ConfigPage)
        self.Manual_Select_Java_PushButton.setGeometry(QtCore.QRect(460, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Manual_Select_Java_PushButton.setFont(font)
        self.Manual_Select_Java_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Manual_Select_Java_PushButton.setStyleSheet("QPushButton\n"
                                                         "{\n"
                                                         "    background-color: rgb(0, 120, 212);\n"
                                                         "    border-radius: 6px;\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "}\n"
                                                         "QPushButton:hover\n"
                                                         "{\n"
                                                         "    background-color: rgb(0, 110, 212);\n"
                                                         "    border-radius: 6px;\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "}\n"
                                                         "QPushButton:pressed\n"
                                                         "{\n"
                                                         "    background-color: rgb(0, 100, 212);\n"
                                                         "    border-radius: 6px;\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "}")
        self.Manual_Select_Java_PushButton.setFlat(False)
        self.Manual_Select_Java_PushButton.setObjectName("Manual_Select_Java_PushButton")
        self.Download_Java_PushButton = QtWidgets.QPushButton(self.ConfigPage)
        self.Download_Java_PushButton.setGeometry(QtCore.QRect(570, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Download_Java_PushButton.setFont(font)
        self.Download_Java_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Download_Java_PushButton.setStyleSheet("QPushButton\n"
                                                    "{\n"
                                                    "    background-color: rgb(0, 120, 212);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}\n"
                                                    "QPushButton:hover\n"
                                                    "{\n"
                                                    "    background-color: rgb(0, 110, 212);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}\n"
                                                    "QPushButton:pressed\n"
                                                    "{\n"
                                                    "    background-color: rgb(0, 100, 212);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}")
        self.Download_Java_PushButton.setFlat(False)
        self.Download_Java_PushButton.setObjectName("Download_Java_PushButton")
        self.Set_Memory_Background = QtWidgets.QLabel(self.ConfigPage)
        self.Set_Memory_Background.setGeometry(QtCore.QRect(330, 280, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Set_Memory_Background.setFont(font)
        self.Set_Memory_Background.setAutoFillBackground(False)
        self.Set_Memory_Background.setStyleSheet("QLabel\n"
                                                 "{\n"
                                                 "    background-color: rgb(247, 247, 247);\n"
                                                 "    border-radius: 10px\n"
                                                 "}")
        self.Set_Memory_Background.setText("")
        self.Set_Memory_Background.setObjectName("Set_Memory_Background")
        self.Memory_1_Label = QtWidgets.QLabel(self.ConfigPage)
        self.Memory_1_Label.setGeometry(QtCore.QRect(350, 290, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Memory_1_Label.setFont(font)
        self.Memory_1_Label.setObjectName("Memory_1_Label")
        self.MinMemory_LineEdit = QtWidgets.QLineEdit(self.ConfigPage)
        self.MinMemory_LineEdit.setGeometry(QtCore.QRect(400, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.MinMemory_LineEdit.setFont(font)
        self.MinMemory_LineEdit.setStyleSheet("QLineEdit\n"
                                              "{\n"
                                              "    border-radius: 3px;\n"
                                              "    border: 2px;\n"
                                              "    border-color: rgb(223, 223, 223);\n"
                                              "    border-style: solid;\n"
                                              "}\n"
                                              "")
        self.MinMemory_LineEdit.setObjectName("MinMemory_LineEdit")
        self.Memory_2_Label = QtWidgets.QLabel(self.ConfigPage)
        self.Memory_2_Label.setGeometry(QtCore.QRect(500, 290, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Memory_2_Label.setFont(font)
        self.Memory_2_Label.setObjectName("Memory_2_Label")
        self.MaxMemory_LineEdit = QtWidgets.QLineEdit(self.ConfigPage)
        self.MaxMemory_LineEdit.setGeometry(QtCore.QRect(520, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.MaxMemory_LineEdit.setFont(font)
        self.MaxMemory_LineEdit.setStyleSheet("QLineEdit\n"
                                              "{\n"
                                              "    border-radius: 3px;\n"
                                              "    border: 2px;\n"
                                              "    border-color: rgb(223, 223, 223);\n"
                                              "    border-style: solid;\n"
                                              "}\n"
                                              "")
        self.MaxMemory_LineEdit.setObjectName("MaxMemory_LineEdit")
        self.Memory_Unit_Label = QtWidgets.QLabel(self.ConfigPage)
        self.Memory_Unit_Label.setGeometry(QtCore.QRect(620, 290, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Memory_Unit_Label.setFont(font)
        self.Memory_Unit_Label.setObjectName("Memory_Unit_Label")
        self.Set_Core_Background = QtWidgets.QLabel(self.ConfigPage)
        self.Set_Core_Background.setGeometry(QtCore.QRect(330, 360, 351, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Set_Core_Background.setFont(font)
        self.Set_Core_Background.setAutoFillBackground(False)
        self.Set_Core_Background.setStyleSheet("QLabel\n"
                                               "{\n"
                                               "    background-color: rgb(247, 247, 247);\n"
                                               "    border-radius: 10px\n"
                                               "}")
        self.Set_Core_Background.setText("")
        self.Set_Core_Background.setObjectName("Set_Core_Background")
        self.Core_Label = QtWidgets.QLabel(self.ConfigPage)
        self.Core_Label.setGeometry(QtCore.QRect(350, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Core_Label.setFont(font)
        self.Core_Label.setObjectName("Core_Label")
        self.ConfigTip3_Label = QtWidgets.QLabel(self.ConfigPage)
        self.ConfigTip3_Label.setGeometry(QtCore.QRect(350, 420, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.ConfigTip3_Label.setFont(font)
        self.ConfigTip3_Label.setObjectName("ConfigTip3_Label")
        self.Manual_Import_Core_PushButton = QtWidgets.QPushButton(self.ConfigPage)
        self.Manual_Import_Core_PushButton.setGeometry(QtCore.QRect(450, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Manual_Import_Core_PushButton.setFont(font)
        self.Manual_Import_Core_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Manual_Import_Core_PushButton.setStyleSheet("QPushButton\n"
                                                         "{\n"
                                                         "    background-color: rgb(0, 120, 212);\n"
                                                         "    border-radius: 6px;\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "}\n"
                                                         "QPushButton:hover\n"
                                                         "{\n"
                                                         "    background-color: rgb(0, 110, 212);\n"
                                                         "    border-radius: 6px;\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "}\n"
                                                         "QPushButton:pressed\n"
                                                         "{\n"
                                                         "    background-color: rgb(0, 100, 212);\n"
                                                         "    border-radius: 6px;\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "}")
        self.Manual_Import_Core_PushButton.setFlat(False)
        self.Manual_Import_Core_PushButton.setObjectName("Manual_Import_Core_PushButton")
        self.Others_Background = QtWidgets.QLabel(self.ConfigPage)
        self.Others_Background.setGeometry(QtCore.QRect(30, 400, 251, 121))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Others_Background.setFont(font)
        self.Others_Background.setAutoFillBackground(False)
        self.Others_Background.setStyleSheet("QLabel\n"
                                             "{\n"
                                             "    background-color: rgb(247, 247, 247);\n"
                                             "    border-radius: 10px\n"
                                             "}")
        self.Others_Background.setText("")
        self.Others_Background.setObjectName("Others_Background")
        self.Server_Name_Label = QtWidgets.QLabel(self.ConfigPage)
        self.Server_Name_Label.setGeometry(QtCore.QRect(50, 420, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Server_Name_Label.setFont(font)
        self.Server_Name_Label.setObjectName("Server_Name_Label")
        self.Server_Name_LineEdit = QtWidgets.QLineEdit(self.ConfigPage)
        self.Server_Name_LineEdit.setGeometry(QtCore.QRect(150, 430, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.Server_Name_LineEdit.setFont(font)
        self.Server_Name_LineEdit.setStyleSheet("QLineEdit\n"
                                                "{\n"
                                                "    border-radius: 3px;\n"
                                                "    border: 2px;\n"
                                                "    border-color: rgb(223, 223, 223);\n"
                                                "    border-style: solid;\n"
                                                "}\n"
                                                "")
        self.Server_Name_LineEdit.setObjectName("Server_Name_LineEdit")
        self.Completed_Save_PushButton = QtWidgets.QPushButton(self.ConfigPage)
        self.Completed_Save_PushButton.setGeometry(QtCore.QRect(50, 470, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Completed_Save_PushButton.setFont(font)
        self.Completed_Save_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Completed_Save_PushButton.setStyleSheet("QPushButton\n"
                                                     "{\n"
                                                     "    background-color: rgb(0, 120, 212);\n"
                                                     "    border-radius: 6px;\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}\n"
                                                     "QPushButton:hover\n"
                                                     "{\n"
                                                     "    background-color: rgb(0, 110, 212);\n"
                                                     "    border-radius: 6px;\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}\n"
                                                     "QPushButton:pressed\n"
                                                     "{\n"
                                                     "    background-color: rgb(0, 100, 212);\n"
                                                     "    border-radius: 6px;\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}")
        self.Completed_Save_PushButton.setFlat(False)
        self.Completed_Save_PushButton.setObjectName("Completed_Save_PushButton")
        self.Download_Core_PushButton = QtWidgets.QPushButton(self.ConfigPage)
        self.Download_Core_PushButton.setGeometry(QtCore.QRect(560, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Download_Core_PushButton.setFont(font)
        self.Download_Core_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Download_Core_PushButton.setStyleSheet("QPushButton\n"
                                                    "{\n"
                                                    "    background-color: rgb(0, 120, 212);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}\n"
                                                    "QPushButton:hover\n"
                                                    "{\n"
                                                    "    background-color: rgb(0, 110, 212);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}\n"
                                                    "QPushButton:pressed\n"
                                                    "{\n"
                                                    "    background-color: rgb(0, 100, 212);\n"
                                                    "    border-radius: 6px;\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}")
        self.Download_Core_PushButton.setFlat(False)
        self.Download_Core_PushButton.setObjectName("Download_Core_PushButton")
        self.Set_Java_Background.raise_()
        self.Config_Label.raise_()
        self.ConfigTip1_Label.raise_()
        self.ConfigTip2_Label.raise_()
        self.Java_Label.raise_()
        self.Select_Java_ComboBox.raise_()
        self.Auto_Find_Java_PushButton.raise_()
        self.Manual_Select_Java_PushButton.raise_()
        self.Download_Java_PushButton.raise_()
        self.Set_Memory_Background.raise_()
        self.Memory_1_Label.raise_()
        self.MinMemory_LineEdit.raise_()
        self.Memory_2_Label.raise_()
        self.MaxMemory_LineEdit.raise_()
        self.Memory_Unit_Label.raise_()
        self.Set_Core_Background.raise_()
        self.Core_Label.raise_()
        self.ConfigTip3_Label.raise_()
        self.Manual_Import_Core_PushButton.raise_()
        self.Others_Background.raise_()
        self.Server_Name_Label.raise_()
        self.Server_Name_LineEdit.raise_()
        self.Completed_Save_PushButton.raise_()
        self.Download_Core_PushButton.raise_()
        self.FunctionsStackedWidget.addWidget(self.ConfigPage)
        self.DownloadPage = QtWidgets.QWidget()
        self.DownloadPage.setObjectName("DownloadPage")
        self.Download_Label = QtWidgets.QLabel(self.DownloadPage)
        self.Download_Label.setGeometry(QtCore.QRect(30, 80, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Download_Label.setFont(font)
        self.Download_Label.setObjectName("Download_Label")
        self.Download_Type_ComboBox = QtWidgets.QComboBox(self.DownloadPage)
        self.Download_Type_ComboBox.setGeometry(QtCore.QRect(170, 180, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.Download_Type_ComboBox.setFont(font)
        self.Download_Type_ComboBox.setStyleSheet("QComboBox {\n"
                                                  "    border-radius: 3px;\n"
                                                  "    padding: 1px 2px 1px 2px;\n"
                                                  "    min-width: 9em;\n"
                                                  "    border: 2px solid rgb(223, 223, 223);\n"
                                                  "}\n"
                                                  "QComboBox::drop-down {\n"
                                                  "    subcontrol-origin: padding;\n"
                                                  "    subcontrol-position: top right;\n"
                                                  "    width: 20px;\n"
                                                  "    border-left-color: rgb(223, 223, 223);\n"
                                                  "    border-left-style: solid;\n"
                                                  "    border-top-right-radius: 4px;\n"
                                                  "    border-bottom-right-radius: 4px;\n"
                                                  "}\n"
                                                  "QComboBox::down-arrow {\n"
                                                  "    image: url(./resources/QComboBox.png);\n"
                                                  "}\n"
                                                  "QComboBox QAbstractItemView::item {\n"
                                                  "    height: 25px;\n"
                                                  "}\n"
                                                  "QComboBox QAbstractItemView{\n"
                                                  "    font-size: 18px;\n"
                                                  "}")
        self.Download_Type_ComboBox.setObjectName("Download_Type_ComboBox")
        self.Download_Type_ComboBox.addItem("")
        self.Download_Type_ComboBox.addItem("")
        self.Download_Type_ComboBox.addItem("")
        self.Download_Type_ComboBox.addItem("")
        self.Download_Type_ComboBox.addItem("")
        self.Download_Type_Background = QtWidgets.QLabel(self.DownloadPage)
        self.Download_Type_Background.setGeometry(QtCore.QRect(30, 140, 651, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Download_Type_Background.setFont(font)
        self.Download_Type_Background.setAutoFillBackground(False)
        self.Download_Type_Background.setStyleSheet("QLabel\n"
                                                    "{\n"
                                                    "    background-color: rgb(247, 247, 247);\n"
                                                    "    border-radius: 10px\n"
                                                    "}")
        self.Download_Type_Background.setText("")
        self.Download_Type_Background.setObjectName("Download_Type_Background")
        self.Download_Type_Label = QtWidgets.QLabel(self.DownloadPage)
        self.Download_Type_Label.setGeometry(QtCore.QRect(60, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Download_Type_Label.setFont(font)
        self.Download_Type_Label.setObjectName("Download_Type_Label")
        self.Download_Versions_ComboBox = QtWidgets.QComboBox(self.DownloadPage)
        self.Download_Versions_ComboBox.setGeometry(QtCore.QRect(170, 310, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.Download_Versions_ComboBox.setFont(font)
        self.Download_Versions_ComboBox.setStyleSheet("QComboBox {\n"
                                                      "    border-radius: 3px;\n"
                                                      "    padding: 1px 2px 1px 2px;\n"
                                                      "    min-width: 9em;\n"
                                                      "    border: 2px solid rgb(223, 223, 223);\n"
                                                      "}\n"
                                                      "QComboBox::drop-down {\n"
                                                      "    subcontrol-origin: padding;\n"
                                                      "    subcontrol-position: top right;\n"
                                                      "    width: 20px;\n"
                                                      "    border-left-color: rgb(223, 223, 223);\n"
                                                      "    border-left-style: solid;\n"
                                                      "    border-top-right-radius: 4px;\n"
                                                      "    border-bottom-right-radius: 4px;\n"
                                                      "}\n"
                                                      "QComboBox::down-arrow {\n"
                                                      "    image: url(./resources/QComboBox.png);\n"
                                                      "}\n"
                                                      "QComboBox QAbstractItemView::item {\n"
                                                      "    height: 25px;\n"
                                                      "}\n"
                                                      "QComboBox QAbstractItemView{\n"
                                                      "    font-size: 18px;\n"
                                                      "}")
        self.Download_Versions_ComboBox.setObjectName("Download_Versions_ComboBox")
        self.Download_Versions_ComboBox.addItem("")
        self.Download_Versions_Label = QtWidgets.QLabel(self.DownloadPage)
        self.Download_Versions_Label.setGeometry(QtCore.QRect(60, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Download_Versions_Label.setFont(font)
        self.Download_Versions_Label.setObjectName("Download_Versions_Label")
        self.Download_Versions_Background = QtWidgets.QLabel(self.DownloadPage)
        self.Download_Versions_Background.setGeometry(QtCore.QRect(30, 270, 651, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Download_Versions_Background.setFont(font)
        self.Download_Versions_Background.setAutoFillBackground(False)
        self.Download_Versions_Background.setStyleSheet("QLabel\n"
                                                        "{\n"
                                                        "    background-color: rgb(247, 247, 247);\n"
                                                        "    border-radius: 10px\n"
                                                        "}")
        self.Download_Versions_Background.setText("")
        self.Download_Versions_Background.setObjectName("Download_Versions_Background")
        self.Download_Progress_Background = QtWidgets.QLabel(self.DownloadPage)
        self.Download_Progress_Background.setGeometry(QtCore.QRect(30, 400, 651, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Download_Progress_Background.setFont(font)
        self.Download_Progress_Background.setAutoFillBackground(False)
        self.Download_Progress_Background.setStyleSheet("QLabel\n"
                                                        "{\n"
                                                        "    background-color: rgb(247, 247, 247);\n"
                                                        "    border-radius: 10px\n"
                                                        "}")
        self.Download_Progress_Background.setText("")
        self.Download_Progress_Background.setObjectName("Download_Progress_Background")
        self.Download_PushButton = QtWidgets.QPushButton(self.DownloadPage)
        self.Download_PushButton.setGeometry(QtCore.QRect(560, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Download_PushButton.setFont(font)
        self.Download_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Download_PushButton.setStyleSheet("QPushButton\n"
                                               "{\n"
                                               "    background-color: rgb(0, 120, 212);\n"
                                               "    border-radius: 6px;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "QPushButton:hover\n"
                                               "{\n"
                                               "    background-color: rgb(0, 110, 212);\n"
                                               "    border-radius: 6px;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}\n"
                                               "QPushButton:pressed\n"
                                               "{\n"
                                               "    background-color: rgb(0, 100, 212);\n"
                                               "    border-radius: 6px;\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}")
        self.Download_PushButton.setFlat(False)
        self.Download_PushButton.setObjectName("Download_PushButton")
        self.Download_Save_Path_Label = QtWidgets.QLabel(self.DownloadPage)
        self.Download_Save_Path_Label.setGeometry(QtCore.QRect(60, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.Download_Save_Path_Label.setFont(font)
        self.Download_Save_Path_Label.setObjectName("Download_Save_Path_Label")
        self.Download_Save_Path_LineEdit = QtWidgets.QLineEdit(self.DownloadPage)
        self.Download_Save_Path_LineEdit.setGeometry(QtCore.QRect(160, 430, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.Download_Save_Path_LineEdit.setFont(font)
        self.Download_Save_Path_LineEdit.setStyleSheet("QLineEdit\n"
                                                       "{\n"
                                                       "    border-radius: 3px;\n"
                                                       "    border: 2px;\n"
                                                       "    border-color: rgb(223, 223, 223);\n"
                                                       "    border-style: solid;\n"
                                                       "}\n"
                                                       "")
        self.Download_Save_Path_LineEdit.setObjectName("Download_Save_Path_LineEdit")
        self.Manually_Choose_Download_Save_Path_PushButton = QtWidgets.QPushButton(self.DownloadPage)
        self.Manually_Choose_Download_Save_Path_PushButton.setGeometry(QtCore.QRect(450, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Manually_Choose_Download_Save_Path_PushButton.setFont(font)
        self.Manually_Choose_Download_Save_Path_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Manually_Choose_Download_Save_Path_PushButton.setStyleSheet("QPushButton\n"
                                                                         "{\n"
                                                                         "    background-color: rgb(0, 120, 212);\n"
                                                                         "    border-radius: 6px;\n"
                                                                         "    color: rgb(255, 255, 255);\n"
                                                                         "}\n"
                                                                         "QPushButton:hover\n"
                                                                         "{\n"
                                                                         "    background-color: rgb(0, 110, 212);\n"
                                                                         "    border-radius: 6px;\n"
                                                                         "    color: rgb(255, 255, 255);\n"
                                                                         "}\n"
                                                                         "QPushButton:pressed\n"
                                                                         "{\n"
                                                                         "    background-color: rgb(0, 100, 212);\n"
                                                                         "    border-radius: 6px;\n"
                                                                         "    color: rgb(255, 255, 255);\n"
                                                                         "}")
        self.Manually_Choose_Download_Save_Path_PushButton.setFlat(False)
        self.Manually_Choose_Download_Save_Path_PushButton.setObjectName(
            "Manually_Choose_Download_Save_Path_PushButton")
        self.Download_Progress_Background.raise_()
        self.Download_Versions_Background.raise_()
        self.Download_Type_Background.raise_()
        self.Download_Label.raise_()
        self.Download_Type_ComboBox.raise_()
        self.Download_Type_Label.raise_()
        self.Download_Versions_ComboBox.raise_()
        self.Download_Versions_Label.raise_()
        self.Download_PushButton.raise_()
        self.Download_Save_Path_Label.raise_()
        self.Download_Save_Path_LineEdit.raise_()
        self.Manually_Choose_Download_Save_Path_PushButton.raise_()
        self.FunctionsStackedWidget.addWidget(self.DownloadPage)
        self.ConsolePage = QtWidgets.QWidget()
        self.ConsolePage.setObjectName("ConsolePage")
        self.Console_Label = QtWidgets.QLabel(self.ConsolePage)
        self.Console_Label.setGeometry(QtCore.QRect(30, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Console_Label.setFont(font)
        self.Console_Label.setObjectName("Console_Label")
        self.Console_Background = QtWidgets.QLabel(self.ConsolePage)
        self.Console_Background.setGeometry(QtCore.QRect(30, 140, 651, 311))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Console_Background.setFont(font)
        self.Console_Background.setAutoFillBackground(False)
        self.Console_Background.setStyleSheet("QLabel\n"
                                              "{\n"
                                              "    background-color: rgb(247, 247, 247);\n"
                                              "    border-radius: 10px\n"
                                              "}")
        self.Console_Background.setText("")
        self.Console_Background.setObjectName("Console_Background")
        self.Command_Background = QtWidgets.QLabel(self.ConsolePage)
        self.Command_Background.setGeometry(QtCore.QRect(30, 470, 651, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Command_Background.setFont(font)
        self.Command_Background.setAutoFillBackground(False)
        self.Command_Background.setStyleSheet("QLabel\n"
                                              "{\n"
                                              "    background-color: rgb(247, 247, 247);\n"
                                              "    border-radius: 10px\n"
                                              "}")
        self.Command_Background.setObjectName("Command_Background")
        self.Send_Command_PushButton = QtWidgets.QPushButton(self.ConsolePage)
        self.Send_Command_PushButton.setGeometry(QtCore.QRect(570, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.Send_Command_PushButton.setFont(font)
        self.Send_Command_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Send_Command_PushButton.setStyleSheet("QPushButton\n"
                                                   "{\n"
                                                   "    background-color: rgb(0, 120, 212);\n"
                                                   "    border-radius: 6px;\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "}\n"
                                                   "QPushButton:hover\n"
                                                   "{\n"
                                                   "    background-color: rgb(0, 110, 212);\n"
                                                   "    border-radius: 6px;\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "}\n"
                                                   "QPushButton:pressed\n"
                                                   "{\n"
                                                   "    background-color: rgb(0, 100, 212);\n"
                                                   "    border-radius: 6px;\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "}")
        self.Send_Command_PushButton.setFlat(False)
        self.Send_Command_PushButton.setObjectName("Send_Command_PushButton")
        self.Command_LineEdit = QtWidgets.QLineEdit(self.ConsolePage)
        self.Command_LineEdit.setGeometry(QtCore.QRect(70, 480, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.Command_LineEdit.setFont(font)
        self.Command_LineEdit.setStyleSheet("QLineEdit\n"
                                            "{\n"
                                            "    border-radius: 3px;\n"
                                            "}\n"
                                            "")
        self.Command_LineEdit.setObjectName("Command_LineEdit")
        self.FunctionsStackedWidget.addWidget(self.ConsolePage)
        self.ToolsPage = QtWidgets.QWidget()
        self.ToolsPage.setObjectName("ToolsPage")
        self.Tools_Label = QtWidgets.QLabel(self.ToolsPage)
        self.Tools_Label.setGeometry(QtCore.QRect(30, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Tools_Label.setFont(font)
        self.Tools_Label.setObjectName("Tools_Label")
        self.FunctionsStackedWidget.addWidget(self.ToolsPage)
        self.AboutPage = QtWidgets.QWidget()
        self.AboutPage.setObjectName("AboutPage")
        self.About_Label = QtWidgets.QLabel(self.AboutPage)
        self.About_Label.setGeometry(QtCore.QRect(30, 80, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.About_Label.setFont(font)
        self.About_Label.setObjectName("About_Label")
        self.About_Background = QtWidgets.QLabel(self.AboutPage)
        self.About_Background.setGeometry(QtCore.QRect(30, 140, 261, 231))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.About_Background.setFont(font)
        self.About_Background.setAutoFillBackground(False)
        self.About_Background.setStyleSheet("QLabel\n"
                                            "{\n"
                                            "    background-color: rgb(247, 247, 247);\n"
                                            "    border-radius: 10px\n"
                                            "}")
        self.About_Background.setText("")
        self.About_Background.setObjectName("About_Background")
        self.MCSL2_Icon_Label = QtWidgets.QLabel(self.AboutPage)
        self.MCSL2_Icon_Label.setGeometry(QtCore.QRect(60, 170, 71, 71))
        self.MCSL2_Icon_Label.setText("")
        self.MCSL2_Icon_Label.setPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Icon.png"))
        self.MCSL2_Icon_Label.setScaledContents(True)
        self.MCSL2_Icon_Label.setObjectName("MCSL2_Icon_Label")
        self.MCSL2_Label = QtWidgets.QLabel(self.AboutPage)
        self.MCSL2_Label.setGeometry(QtCore.QRect(150, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.MCSL2_Label.setFont(font)
        self.MCSL2_Label.setObjectName("MCSL2_Label")
        self.MCSL2_Author_Label_1 = QtWidgets.QLabel(self.AboutPage)
        self.MCSL2_Author_Label_1.setGeometry(QtCore.QRect(150, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.MCSL2_Author_Label_1.setFont(font)
        self.MCSL2_Author_Label_1.setObjectName("MCSL2_Author_Label_1")
        self.MCSL2_Author_Avatar = QtWidgets.QLabel(self.AboutPage)
        self.MCSL2_Author_Avatar.setGeometry(QtCore.QRect(60, 270, 71, 71))
        self.MCSL2_Author_Avatar.setText("")
        self.MCSL2_Author_Avatar.setPixmap(QtGui.QPixmap(":/MCSL2_Icon/MCSL2_Author.png"))
        self.MCSL2_Author_Avatar.setScaledContents(True)
        self.MCSL2_Author_Avatar.setObjectName("MCSL2_Author_Avatar")
        self.MCSL2_Author_Label_2 = QtWidgets.QLabel(self.AboutPage)
        self.MCSL2_Author_Label_2.setGeometry(QtCore.QRect(150, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.MCSL2_Author_Label_2.setFont(font)
        self.MCSL2_Author_Label_2.setObjectName("MCSL2_Author_Label_2")
        self.Description_Label = QtWidgets.QLabel(self.AboutPage)
        self.Description_Label.setGeometry(QtCore.QRect(310, 140, 381, 311))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.Description_Label.setFont(font)
        self.Description_Label.setAutoFillBackground(False)
        self.Description_Label.setStyleSheet("QLabel\n"
                                             "{\n"
                                             "    background-color: rgb(247, 247, 247);\n"
                                             "    border-radius: 10px\n"
                                             "}")
        self.Description_Label.setObjectName("Description_Label")
        self.Check_Update_PushButton = QtWidgets.QPushButton(self.AboutPage)
        self.Check_Update_PushButton.setGeometry(QtCore.QRect(30, 390, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        self.Check_Update_PushButton.setFont(font)
        self.Check_Update_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Check_Update_PushButton.setStyleSheet("QPushButton\n"
                                                   "{\n"
                                                   "    background-color: rgb(247, 247, 247);\n"
                                                   "    border-radius: 7px;\n"
                                                   "}\n"
                                                   "QPushButton:hover\n"
                                                   "{\n"
                                                   "    background-color: rgb(230, 230, 230);\n"
                                                   "    border-radius: 7px;\n"
                                                   "}\n"
                                                   "QPushButton:pressed\n"
                                                   "{\n"
                                                   "    background-color: rgb(225, 225, 225);\n"
                                                   "    border-radius: 7px;\n"
                                                   "}")
        self.Check_Update_PushButton.setObjectName("Check_Update_PushButton")
        self.FunctionsStackedWidget.addWidget(self.AboutPage)
        self.ChooseServerPage = QtWidgets.QWidget()
        self.ChooseServerPage.setObjectName("ChooseServerPage")
        self.Choose_Server_Label = QtWidgets.QLabel(self.ChooseServerPage)
        self.Choose_Server_Label.setGeometry(QtCore.QRect(30, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Choose_Server_Label.setFont(font)
        self.Choose_Server_Label.setObjectName("Choose_Server_Label")
        self.Choose_Server_ComboBox = QtWidgets.QComboBox(self.ChooseServerPage)
        self.Choose_Server_ComboBox.setGeometry(QtCore.QRect(220, 320, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        self.Choose_Server_ComboBox.setFont(font)
        self.Choose_Server_ComboBox.setStyleSheet("QComboBox {\n"
                                                  "    border-radius: 3px;\n"
                                                  "    padding: 1px 2px 1px 2px;\n"
                                                  "    min-width: 9em;\n"
                                                  "    border: 2px solid rgb(223, 223, 223);\n"
                                                  "}\n"
                                                  "QComboBox::drop-down {\n"
                                                  "    subcontrol-origin: padding;\n"
                                                  "    subcontrol-position: top right;\n"
                                                  "    width: 20px;\n"
                                                  "    border-left-color: rgb(223, 223, 223);\n"
                                                  "    border-left-style: solid;\n"
                                                  "    border-top-right-radius: 4px;\n"
                                                  "    border-bottom-right-radius: 4px;\n"
                                                  "}\n"
                                                  "QComboBox::down-arrow {\n"
                                                  "    image: url(./resources/QComboBox.png);\n"
                                                  "}\n"
                                                  "QComboBox QAbstractItemView::item {\n"
                                                  "    height: 25px;\n"
                                                  "}\n"
                                                  "QComboBox QAbstractItemView{\n"
                                                  "    font-size: 18px;\n"
                                                  "}")
        self.Choose_Server_ComboBox.setObjectName("Choose_Server_ComboBox")
        self.Choose_Server_ComboBox.addItem("")
        self.Choose_Server_Label2 = QtWidgets.QLabel(self.ChooseServerPage)
        self.Choose_Server_Label2.setGeometry(QtCore.QRect(60, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Choose_Server_Label2.setFont(font)
        self.Choose_Server_Label2.setObjectName("Choose_Server_Label2")
        self.Choose_Server_Background = QtWidgets.QLabel(self.ChooseServerPage)
        self.Choose_Server_Background.setGeometry(QtCore.QRect(30, 280, 651, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Choose_Server_Background.setFont(font)
        self.Choose_Server_Background.setAutoFillBackground(False)
        self.Choose_Server_Background.setStyleSheet("QLabel\n"
                                                    "{\n"
                                                    "    background-color: rgb(247, 247, 247);\n"
                                                    "    border-radius: 10px\n"
                                                    "}")
        self.Choose_Server_Background.setText("")
        self.Choose_Server_Background.setObjectName("Choose_Server_Background")
        self.Choose_Server_Tip1 = QtWidgets.QLabel(self.ChooseServerPage)
        self.Choose_Server_Tip1.setGeometry(QtCore.QRect(30, 140, 651, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Choose_Server_Tip1.setFont(font)
        self.Choose_Server_Tip1.setAutoFillBackground(False)
        self.Choose_Server_Tip1.setStyleSheet("QLabel\n"
                                              "{\n"
                                              "    background-color: rgb(247, 247, 247);\n"
                                              "    border-radius: 10px\n"
                                              "}")
        self.Choose_Server_Tip1.setObjectName("Choose_Server_Tip1")
        self.Completed_Choose_Server_PushButton = QtWidgets.QPushButton(self.ChooseServerPage)
        self.Completed_Choose_Server_PushButton.setGeometry(QtCore.QRect(560, 410, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.Completed_Choose_Server_PushButton.setFont(font)
        self.Completed_Choose_Server_PushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Completed_Choose_Server_PushButton.setStyleSheet("QPushButton\n"
                                                              "{\n"
                                                              "    background-color: rgb(0, 120, 212);\n"
                                                              "    border-radius: 8px;\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "}\n"
                                                              "QPushButton:pressed\n"
                                                              "{\n"
                                                              "    background-color: rgb(0, 107, 212);\n"
                                                              "    border-radius: 8px;\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "}")
        self.Completed_Choose_Server_PushButton.setFlat(False)
        self.Completed_Choose_Server_PushButton.setObjectName("Completed_Choose_Server_PushButton")
        self.Choose_Server_Background.raise_()
        self.Choose_Server_Label.raise_()
        self.Choose_Server_ComboBox.raise_()
        self.Choose_Server_Label2.raise_()
        self.Choose_Server_Tip1.raise_()
        self.Completed_Choose_Server_PushButton.raise_()
        self.FunctionsStackedWidget.addWidget(self.ChooseServerPage)
        self.Background = QtWidgets.QLabel(self.CentralWidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 211, 581))
        self.Background.setStyleSheet("QLabel\n"
                                      "{\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    border-radius: 10px\n"
                                      "}")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.Background_2 = QtWidgets.QLabel(self.CentralWidget)
        self.Background_2.setGeometry(QtCore.QRect(120, 0, 821, 581))
        self.Background_2.setStyleSheet("QLabel\n"
                                        "{\n"
                                        "    background-color: rgba(255, 255, 255,82%);\n"
                                        "    border-radius: 10px\n"
                                        "}")
        self.Background_2.setText("")
        self.Background_2.setObjectName("Background_2")
        self.Background_2.raise_()
        self.Background.raise_()
        self.OptionsWidget.raise_()
        self.FunctionsStackedWidget.raise_()
        MCSL2_MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MCSL2_MainWindow)
        self.FunctionsStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MCSL2_MainWindow)

    def mouseMoveEvent(self, e: QMouseEvent):  # ??????????????????
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    def retranslateUi(self, MCSL2_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MCSL2_MainWindow.setWindowTitle(_translate("MCSL2_MainWindow", "MainWindow"))
        self.Home_Page_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Config_Page_PushButton.setText(_translate("MCSL2_MainWindow", "???????????????"))
        self.MCSL2_Title_Label.setText(_translate("MCSL2_MainWindow", "MCSL 2"))
        self.MCSL2_Title_Author_Label.setText(_translate("MCSL2_MainWindow", "by LxHTT"))
        self.Download_Page_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Server_Console_Page_PushButton.setText(_translate("MCSL2_MainWindow", "??????????????????"))
        self.Tools_Page_PushButton.setText(_translate("MCSL2_MainWindow", "????????????"))
        self.About_Page_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Config_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Choose_Server_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Home_Label.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Start_PushButton.setText(_translate("MCSL2_MainWindow", "???????????????"))
        self.Selected_Server_Label.setText(_translate("MCSL2_MainWindow", "?????????????????????"))
        self.Notice_Label.setText(_translate("MCSL2_MainWindow", "   ??????????????????..."))
        self.HomeTip1_Label.setText(_translate("MCSL2_MainWindow", "   ??????????????????Java??? Minecraft????????????\n"
                                                                   "   1.?????????Java??????????????????\n"
                                                                   "   ???????????????????????????????????????\n"
                                                                   "   2.???????????????????????????????????????????????????\n"
                                                                   "   3. ??????????????????\n"
                                                                   "   ????????????IP???????????????"))
        self.Config_Label.setText(_translate("MCSL2_MainWindow", "???????????????"))
        self.ConfigTip1_Label.setText(_translate("MCSL2_MainWindow", "   ??????????????????????????????????????????\n"
                                                                     "   1.????????????????????????\n"
                                                                     "   2.???????????????\n"
                                                                     "   3.Java??????"))
        self.ConfigTip2_Label.setText(_translate("MCSL2_MainWindow", "   MCSL 2???????????????????????????\n"
                                                                     "   ???????????????????????????????????????\n"
                                                                     "   ????????????????????????"))
        self.Java_Label.setText(_translate("MCSL2_MainWindow", "Java:"))
        self.Select_Java_ComboBox.setItemText(0, _translate("MCSL2_MainWindow", "  ?????????"))
        self.Auto_Find_Java_PushButton.setText(_translate("MCSL2_MainWindow", "????????????"))
        self.Manual_Select_Java_PushButton.setText(_translate("MCSL2_MainWindow", "????????????"))
        self.Download_Java_PushButton.setText(_translate("MCSL2_MainWindow", "??????Java"))
        self.Memory_1_Label.setText(_translate("MCSL2_MainWindow", "?????????"))
        self.Memory_2_Label.setText(_translate("MCSL2_MainWindow", "~"))
        self.Memory_Unit_Label.setText(_translate("MCSL2_MainWindow", "MB"))
        self.Core_Label.setText(_translate("MCSL2_MainWindow", "??????????????????"))
        self.ConfigTip3_Label.setText(_translate("MCSL2_MainWindow", "MCSL 2?????????????????????????????????????????????\n"
                                                                     "??????????????????????????????????????????server.jar???"))
        self.Manual_Import_Core_PushButton.setText(_translate("MCSL2_MainWindow", "????????????"))
        self.Server_Name_Label.setText(_translate("MCSL2_MainWindow", "??????????????????"))
        self.Completed_Save_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Download_Core_PushButton.setText(_translate("MCSL2_MainWindow", "????????????"))
        self.Download_Label.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Download_Type_ComboBox.setItemText(0, _translate("MCSL2_MainWindow", "  ?????????"))
        self.Download_Type_ComboBox.setItemText(1, _translate("MCSL2_MainWindow", "  [ ???????????? ] Java"))
        self.Download_Type_ComboBox.setItemText(2, _translate("MCSL2_MainWindow", "  [ ????????? ] Spigot"))
        self.Download_Type_ComboBox.setItemText(3, _translate("MCSL2_MainWindow", "  [ ????????? ] Paper"))
        self.Download_Type_ComboBox.setItemText(4, _translate("MCSL2_MainWindow", "  [ ????????? ] BungeeCord"))
        self.Download_Type_Label.setText(_translate("MCSL2_MainWindow", "???????????????"))
        self.Download_Versions_ComboBox.setItemText(0, _translate("MCSL2_MainWindow", "  ?????????"))
        self.Download_Versions_Label.setText(_translate("MCSL2_MainWindow", "???????????????"))
        self.Download_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Download_Save_Path_Label.setText(_translate("MCSL2_MainWindow", "????????????:"))
        self.Manually_Choose_Download_Save_Path_PushButton.setText(_translate("MCSL2_MainWindow", "??????.."))
        self.Console_Label.setText(_translate("MCSL2_MainWindow", "??????????????????"))
        self.Command_Background.setText(_translate("MCSL2_MainWindow", "  >"))
        self.Send_Command_PushButton.setText(_translate("MCSL2_MainWindow", "??????"))
        self.Tools_Label.setText(_translate("MCSL2_MainWindow", "????????????"))
        self.About_Label.setText(_translate("MCSL2_MainWindow", "??????"))
        self.MCSL2_Label.setText(_translate("MCSL2_MainWindow", "MCSL 2"))
        self.MCSL2_Author_Label_1.setText(_translate("MCSL2_MainWindow", "by LxHTT"))
        self.MCSL2_Author_Label_2.setText(_translate("MCSL2_MainWindow", "Bilibili???\n"
                                                                         "????????????LxHTT"))
        self.Description_Label.setText(_translate("MCSL2_MainWindow", "    ?????????MCSL???Remake??? \n"
                                                                      "\n"
                                                                      "    ????????????C#?????????????????????????????????????????????\n"
                                                                      "\n"
                                                                      "    ??????Python??? \n"
                                                                      "\n"
                                                                      "    MCSL 2 ??????UI?????????????????????????????????????????????\n"
                                                                      "\n"
                                                                      "    ????????????????????????????????????????????????????????????????????? \n"
                                                                      "\n"
                                                                      "    ??????Bug????????????????????????????????????MCSL 2??? \n"
                                                                      "\n"
                                                                      "    ????????????: lxhtz.dl@qq.com "))
        self.Check_Update_PushButton.setText(_translate("MCSL2_MainWindow", "????????????"))
        self.Choose_Server_Label.setText(_translate("MCSL2_MainWindow", "???????????????"))
        self.Choose_Server_ComboBox.setItemText(0, _translate("MCSL2_MainWindow", "  ?????????"))
        self.Choose_Server_Label2.setText(_translate("MCSL2_MainWindow", "?????????????????????"))
        self.Choose_Server_Tip1.setText(_translate("MCSL2_MainWindow", "   MCSL 2????????????????????????????????????MCSL 2????????????????????????????????????????????????\n"
                                                                       "\n"
                                                                       "   MCSL 2??????????????????????????????????????????????????????????????????"))
        self.Completed_Choose_Server_PushButton.setText(_translate("MCSL2_MainWindow", "?????????"))

        # Window event binding
        self.Close_PushButton.clicked.connect(self.Quit)
        self.Minimize_PushButton.clicked.connect(self.Minimize)

        # Pages navigation binding
        self.Home_Page_PushButton.clicked.connect(self.ToHomePage)
        self.Config_Page_PushButton.clicked.connect(self.ToConfigPage)
        self.Download_Page_PushButton.clicked.connect(self.ToDownloadPage)
        self.Server_Console_Page_PushButton.clicked.connect(self.ToConsolePage)
        self.Tools_Page_PushButton.clicked.connect(self.ToToolsPage)
        self.About_Page_PushButton.clicked.connect(self.ToAboutPage)
        self.Config_PushButton.clicked.connect(self.ToConfigPage)
        self.Choose_Server_PushButton.clicked.connect(self.ToChooseServerPage)
        self.Completed_Choose_Server_PushButton.clicked.connect(self.ToHomePage)
        self.Download_Core_PushButton.clicked.connect(self.ToDownloadPage)

        # Functions binding
        self.Start_PushButton.clicked.connect(self.LaunchMinecraftServer)
        self.Manual_Select_Java_PushButton.clicked.connect(self.ManuallySelectJava)
        self.Manual_Import_Core_PushButton.clicked.connect(self.ManuallyImportCore)
        self.Download_Java_PushButton.clicked.connect(self.ToDownloadJava)
        self.Check_Update_PushButton.clicked.connect(self.CheckUpdate)
        self.Download_PushButton.clicked.connect(self.StartDownload)
        self.Download_Type_ComboBox.currentIndexChanged.connect(self.RefreshDownloadType)
        self.Manually_Choose_Download_Save_Path_PushButton.clicked.connect(self.SetDownloadSavePath)
        self.Auto_Find_Java_PushButton.clicked.connect(self.AutoDetectJava)
        self.Completed_Save_PushButton.clicked.connect(self.SaveAMinecraftServer)

    def Quit(self):
        app.quit()

    def Minimize(self):
        self.MCSL2_Window.showMinimized()

    def ToHomePage(self):
        self.FunctionsStackedWidget.setCurrentIndex(0)

    def ToConfigPage(self):
        self.FunctionsStackedWidget.setCurrentIndex(1)

    def ToDownloadPage(self):
        self.FunctionsStackedWidget.setCurrentIndex(2)

    def ToConsolePage(self):
        self.FunctionsStackedWidget.setCurrentIndex(3)

    def ToToolsPage(self):
        self.FunctionsStackedWidget.setCurrentIndex(4)

    def ToAboutPage(self):
        self.FunctionsStackedWidget.setCurrentIndex(5)

    def ToChooseServerPage(self):
        self.FunctionsStackedWidget.setCurrentIndex(6)

    def LaunchMinecraftServer(self):
        Tip = "cnm  ?????????"
        CallMCSL2Dialog(Tip)
        # Fix = '-Xms2048M -Xmx2048M -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -jar '
        # monitor = subprocess.Popen(LaunchCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # while True:
        #     result = monitor.stdout.readline()
        #     if result != b'':
        #         try:
        #             print(result.decode('gbk').strip('\r\n'))
        #         except:
        #             print(result.decode('utf-8').strip('\r\n'))
        #     else:
        #         break

    def ManuallySelectJava(self):
        global JavaPath
        JavaPathSysList = QFileDialog.getOpenFileName(self, '??????java.exe??????', os.getcwd(), "java.exe")
        if JavaPathSysList[0] != "":
            self.Select_Java_ComboBox.addItem(JavaPathSysList[0])
            JavaPath = JavaPathSysList[0]
        else:
            Tip = "??????????????????????????????Java??????"
            CallMCSL2Dialog(Tip)

    def ManuallyImportCore(self):
        global CorePath
        CoreSysList = QFileDialog.getOpenFileName(self, '?????????????????????', os.getcwd(), "*.jar")
        if CoreSysList[0] != "":
            CorePath = CoreSysList[0]
        else:
            Tip = "???????????????????????????????????????????????????"
            CallMCSL2Dialog(Tip)

    def SaveAMinecraftServer(self):
        global MinMem, MaxMem, Name
        '''
        0 -> Illegal
        1 -> OK
        '''
        # The min memory parser
        if self.MinMemory_LineEdit.text() != "":
            if int(self.MinMemory_LineEdit.text()) %1 == 0:
                MinMemory = int(self.MinMemory_LineEdit.text())
                MinMem = 1
            else:
                MinMem = 0
        else:
            MinMem = 0

        # The max memory parser
        if self.MaxMemory_LineEdit.text() != "":
            if int(self.MaxMemory_LineEdit.text()) % 1 == 0:
                MaxMemory = int(self.MaxMemory_LineEdit.text())
                MaxMem = 1
            else:
                MaxMem = 0
        else:
            MaxMem = 0

        # The server name parser
        if self.Server_Name_LineEdit.text() != "":
            TMPServerName = self.Server_Name_LineEdit.text()
            IllegalCodeList = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
            for i in range(len(IllegalCodeList)):
                if not IllegalCodeList[i] in TMPServerName:
                    ServerName = TMPServerName
                    Name = 1
                else:
                    Name = 0
        else:
            Name = 0

        # Pop-up parser
        if MinMem == 0 and MaxMem == 0 and Name == 0:
            Tip = "???????????????????????????????????????\n\n??????"
        elif MinMem == 0 and MaxMem == 0 and Name == 1:
            Tip = "?????????????????????\n\n??????"
        elif MinMem == 1 and MaxMem == 0 and Name == 1:
            Tip = "???????????????????????????\n\n??????"
        elif MinMem == 0 and MaxMem == 1 and Name == 1:
            Tip = "???????????????????????????\n\n??????"
        elif MinMem == 1 and MaxMem == 1 and Name == 0:
            Tip = "?????????????????????????????????\n\n??????"
        elif MinMem == 0 and MaxMem == 1 and Name == 0:
            Tip = "????????????????????????????????????????????????\n\n??????"
        elif MinMem == 1 and MaxMem == 0 and Name == 0:
            Tip = "????????????????????????????????????????????????\n\n??????"
        elif MinMem == 1 and MaxMem == 1 and Name == 1:
            # need MaxMem, MinMem, JavaPath, CorePath
            Tip = "??????????????????????????????????????????????????????????????????"
        CallMCSL2Dialog(Tip)

    def AutoDetectJava(self):
        Tip = "cnm  ?????????????????????"
        CallMCSL2Dialog(Tip)

    def ToDownloadJava(self):
        self.FunctionsStackedWidget.setCurrentIndex(2)
        self.Download_Type_ComboBox.setCurrentIndex(1)

    # The function of refreshing download type.
    def RefreshDownloadType(self):
        ComboBoxNames.clear()
        DownloadUrls.clear()
        FileFormats.clear()
        self.Download_Versions_ComboBox.clear()
        """
        self.Download_Type_ComboBox.currentIndex()
        0 - Failed.
        1 - Java.
        2 - Spigot.
        3 - Paper.
        4. - BungeeCord.(Hidden)
        """
        if self.Download_Type_ComboBox.currentIndex() == 0:
            pass
        elif self.Download_Type_ComboBox.currentIndex() == 1:  # Java
            if os.path.isfile("JavaDownloadInfo.json"):
                os.remove("JavaDownloadInfo.json")
            RefreshDownloadJavaUrl = 'https://raw.iqiq.io/LxHTT/MCSL2/master/JavaDownloadInfo.json'
            wget.download(RefreshDownloadJavaUrl, 'JavaDownloadInfo.json')
            DecodeDownloadJsons(DJson="JavaDownloadInfo.json")
        elif self.Download_Type_ComboBox.currentIndex() == 2:  # Spigot
            if os.path.isfile("SpigotDownloadInfo.json"):
                os.remove("SpigotDownloadInfo.json")  # ???????????????????????????????????????
            RefreshDownloadSpigotUrl = 'https://raw.iqiq.io/LxHTT/MCSL2/master/SpigotDownloadInfo.json'
            wget.download(RefreshDownloadSpigotUrl, 'SpigotDownloadInfo.json')
            DecodeDownloadJsons(DJson="SpigotDownloadInfo.json")
        elif self.Download_Type_ComboBox.currentIndex() == 3:  # Paper
            if os.path.isfile("PaperDownloadInfo.json"):
                os.remove("PaperDownloadInfo.json")
            RefreshDownloadPaperUrl = 'https://raw.iqiq.io/LxHTT/MCSL2/master/PaperDownloadInfo.json'
            wget.download(RefreshDownloadPaperUrl, 'PaperDownloadInfo.json')
            DecodeDownloadJsons(DJson="PaperDownloadInfo.json")
        elif self.Download_Type_ComboBox.currentIndex() == 4:  # BungeeCord
            if os.path.isfile("BungeeCordDownloadInfo.json"):
                os.remove("BungeeCordDownloadInfo.json")
            RefreshDownloadBCUrl = 'https://raw.iqiq.io/LxHTT/MCSL2/master/BungeeCordDownloadInfo.json'
            wget.download(RefreshDownloadBCUrl, 'BungeeCordDownloadInfo.json')
            DecodeDownloadJsons(DJson="BungeeCordDownloadInfo.json")
        for i in range(len(ComboBoxNames)):
            self.Download_Versions_ComboBox.addItem("  " + ComboBoxNames[i])

    # The function of setting downloader save path
    def SetDownloadSavePath(self):
        global SaveFolder
        SaveFolder = QtWidgets.QFileDialog.getExistingDirectory(self, "?????????????????????????????????", "./").replace("/", "\\")
        self.Download_Save_Path_LineEdit.setText("  " + SaveFolder)

    # The function of downloading
    def StartDownload(self):
        DownloadIndex = self.Download_Versions_ComboBox.currentIndex()
        ComboBoxName = ComboBoxNames[DownloadIndex]
        DownloadUrl = DownloadUrls[DownloadIndex]
        FileFormat = FileFormats[DownloadIndex]
        FileName = FileNames[DownloadIndex]
        Downloader = DownloadKit(goal_path=SaveFolder, roads=32, file_exists='skip')
        Downloader.block_size = '10M'
        StartDownloading = Downloader.add(DownloadUrl)
        Tip = "?????????: " + FileName + "." + FileFormat + "\n????????????: " + SaveFolder
        CallMCSL2Dialog(Tip)
        Downloader.wait(StartDownloading)
        if StartDownloading.result == 'success':
            Tip = "????????????."
            CallMCSL2Dialog(Tip)
        elif not StartDownloading.result:
            Tip = "????????????, ?????????????????????, ??????????????????."
            CallMCSL2Dialog(Tip)
        elif StartDownloading.result == "skip":
            Tip = "?????????????????????????????????..\n\n??????????????????????????????????????????!"
            CallMCSL2Dialog(Tip)
        else:
            pass

    # The function of checking update
    def CheckUpdate(self):
        if os.path.isfile("versionInfo"):
            os.remove("versionInfo")
        CheckUpdateUrl = 'https://raw.iqiq.io/LxHTT/MCSL2/master/versionInfo'
        wget.download(CheckUpdateUrl, 'versionInfo')
        LatestVersion = open(r'versionInfo', 'r').read()
        if float(LatestVersion) > Version:
            Tip = "??????????????????:v" + str(LatestVersion)
            CallMCSL2Dialog(Tip)
        elif float(LatestVersion) == Version:
            Tip = "??????????????????:v" + str(LatestVersion)
            CallMCSL2Dialog(Tip)
        elif float(LatestVersion) < Version:
            Tip = "??????????????????(\n\n???????????????: v" + str(Version) + "\n\n???????????????: v" + str(LatestVersion)
            CallMCSL2Dialog(Tip)


# Customize dialogs
class MCSL2Dialog(QtWidgets.QDialog, Ui_MCSL2_Dialog):
    def __init__(self):
        super(MCSL2Dialog, self).__init__()
        self.setupUi(self)


# The function of decoding downloaded jsons
def DecodeDownloadJsons(DJson):
    with open(file=DJson, mode='r', encoding="utf-8") as OpenDownloadList:
        DownloadList = str(OpenDownloadList.read())
    PyDownloadList = json.loads(DownloadList)['MCSLDownloadList']
    for i in PyDownloadList:
        ComboBoxName = i["name"]
        ComboBoxNames.insert(0, ComboBoxName)
        DownloadUrl = i["url"]
        DownloadUrls.insert(0, DownloadUrl)
        FileFormat = i["format"]
        FileFormats.insert(0, FileFormat)
        FileName = i["filename"]
        FileNames.insert(0, FileName)


# The function of calling MCSL2 Dialog
def CallMCSL2Dialog(Tip):
    SaveTip = open(r'Tip', 'w+')
    SaveTip.write(Tip)
    SaveTip.close()
    MCSL2Dialog().exec()
    os.remove(r'Tip')


# Start app
ComboBoxNames = []
DownloadUrls = []
FileFormats = []
FileNames = []
Version = 2.0
app = QtWidgets.QApplication(sys.argv)
MainWindow = Ui_MCSL2_MainWindow()
ui = Ui_MCSL2_MainWindow()
ui.setupUi(MainWindow)
MainWindow.setWindowTitle("MCSL 2 ver2.0.0")
MainWindow.show()
sys.exit(app.exec_())
