# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheetahTracker.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# Import Essential Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import cv2 as cv
import numpy as np
from os.path import isfile

# Start of GUI Initialization
class Ui_CheetahTracker(object):
    def __init__(self):
        self.selectROI = False # Interactive Region Selection
        self.boxPoints = []

    def setupUi(self, CheetahTracker):
        CheetahTracker.setObjectName("CheetahTracker")
        CheetahTracker.resize(1333, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("VIBOT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CheetahTracker.setWindowIcon(icon)
        CheetahTracker.setAutoFillBackground(True)
        CheetahTracker.setStyleSheet("rgb (162, 254, 255)\n"
"background-color: rgb(97, 221, 255);")
        CheetahTracker.setSizeGripEnabled(False)
        CheetahTracker.setModal(False)
        self.label = QtWidgets.QLabel(CheetahTracker)
        self.label.setGeometry(QtCore.QRect(260, 10, 831, 61))
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.InputConsole = QtWidgets.QGroupBox(CheetahTracker)
        self.InputConsole.setGeometry(QtCore.QRect(270, 530, 881, 151))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.InputConsole.setPalette(palette)
        self.InputConsole.setAlignment(QtCore.Qt.AlignCenter)
        self.InputConsole.setFlat(False)
        self.InputConsole.setCheckable(False)
        self.InputConsole.setObjectName("InputConsole")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.InputConsole)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 591, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoadVideo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LoadVideo.setObjectName("LoadVideo")
        self.horizontalLayout.addWidget(self.LoadVideo)
        self.CaptureVideo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CaptureVideo.setObjectName("CaptureVideo")
        self.horizontalLayout.addWidget(self.CaptureVideo)
        self.TrackObject = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.TrackObject.setObjectName("TrackObject")
        self.horizontalLayout.addWidget(self.TrackObject)
        self.Reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Reset.setObjectName("Reset")
        self.horizontalLayout.addWidget(self.Reset)
        self.Process = QtWidgets.QGroupBox(self.InputConsole)
        self.Process.setGeometry(QtCore.QRect(660, 30, 191, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Process.setPalette(palette)
        self.Process.setObjectName("Process")
        self.CurrentProcess = QtWidgets.QLineEdit(self.Process)
        self.CurrentProcess.setGeometry(QtCore.QRect(10, 30, 171, 51))
        self.CurrentProcess.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentProcess.setObjectName("CurrentProcess")
        self.PKFLabel = QtWidgets.QLabel(CheetahTracker)
        self.PKFLabel.setGeometry(QtCore.QRect(950, 100, 301, 301))
        self.PKFLabel.setText("")
        self.PKFLabel.setObjectName("PKFLabel")
        self.KFLabel = QtWidgets.QLabel(CheetahTracker)
        self.KFLabel.setGeometry(QtCore.QRect(90, 100, 301, 301))
        self.KFLabel.setText("")
        self.KFLabel.setObjectName("KFLabel")
        self.PFLabel = QtWidgets.QLabel(CheetahTracker)
        self.PFLabel.setGeometry(QtCore.QRect(520, 100, 301, 301))
        self.PFLabel.setText("")
        self.PFLabel.setObjectName("PFLabel")
        self.label_2 = QtWidgets.QLabel(CheetahTracker)
        self.label_2.setGeometry(QtCore.QRect(130, 440, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(CheetahTracker)
        self.label_3.setGeometry(QtCore.QRect(560, 440, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(CheetahTracker)
        self.label_4.setGeometry(QtCore.QRect(950, 440, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(CheetahTracker)
        self.label_5.setGeometry(QtCore.QRect(40, 580, 81, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("VIBOT.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(CheetahTracker)
        QtCore.QMetaObject.connectSlotsByName(CheetahTracker)

    def retranslateUi(self, CheetahTracker):
        _translate = QtCore.QCoreApplication.translate
        CheetahTracker.setWindowTitle(_translate("CheetahTracker", "Cheetah Tracker"))
        self.label.setText(_translate("CheetahTracker", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#75507b;\">Non-Rigid Object Tracking Based on CamShift and Particle-Kalman Filter</span></p></body></html>"))
        self.InputConsole.setTitle(_translate("CheetahTracker", "Console"))
        self.LoadVideo.setText(_translate("CheetahTracker", "Load Video"))
        self.CaptureVideo.setText(_translate("CheetahTracker", "Capture Video"))
        self.TrackObject.setText(_translate("CheetahTracker", "Start Tracker"))
        self.Reset.setText(_translate("CheetahTracker", "Stop/Reset"))
        self.Process.setTitle(_translate("CheetahTracker", "Current Process"))
        self.label_2.setText(_translate("CheetahTracker", "Tracking with Kalman Filter"))
        self.label_3.setText(_translate("CheetahTracker", "Tracking with Particle Filter"))
        self.label_4.setText(_translate("CheetahTracker", "Tracking with Particle-Kalman Filter"))
# End of GUI Initialization

        # Connect All Push Buttons to the corresponding functions
        self.LoadVideo.clicked.connect(self.on_LoadVideo_clicked)
        self.CaptureVideo.clicked.connect(self.on_CaptureVideo_clicked)
        self.TrackObject.clicked.connect(self.on_TrackObject_clicked)
        self.TrackObject.setEnabled(False)
        self.Reset.clicked.connect(self.on_Reset_clicked)
        self.Reset.setEnabled(False)

# Define the Functionalities for Push Button Actions
    def on_LoadVideo_clicked(self):
        # Load a Video with File Picker
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        LoadfileName, _ = QFileDialog.getOpenFileName(CheetahTracker,"Select a Video","","Video Files (*.avi *.flv *.wmv *.mp4 *.mpg)", options=options)
        if isfile(LoadfileName):
            global videoInput
            videoInput = LoadfileName
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Video Loaded!")
            msgBox.setInformativeText("Click 'Start Tracker' to Start Streaming!!!")
            msgBox.exec_()
            self.TrackObject.setEnabled(True)
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Video Loaded!!!")
            msgBox.exec_()

    def on_CaptureVideo_clicked(self):
        global videoInput
        videoInput = 0 # 0 for Internal Camera (1 for External Camera)
        # Show the Message
        msgBox = QMessageBox()
        msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
        msgBox.setText("Camera initialized!")
        msgBox.setInformativeText("Click 'Start Tracker' to Start Capture!!!")
        msgBox.exec_()
        self.TrackObject.setEnabled(True)

    def on_TrackObject_clicked(self):
        self.Reset.setEnabled(True)
        # Define Functions
        def on_Mouse_dragged(event, x, y, flags, params):
            # Get the Coordinates
            current_mouse_position[0] = x
            current_mouse_position[1] = y

            if event == cv.EVENT_LBUTTONDOWN:
                # If Left Mouse Button is Pressed
                self.boxPoints = []
                # Start Mouse Position
                start = [x, y]

                self.selectROI = True
                self.boxPoints.append(start)

            elif event == cv.EVENT_LBUTTONUP:
                # If Left Mouse Button is Released
                # End Mouse Position
                end = [x, y]
                self.selectROI = False
                self.boxPoints.append(end)

        def center(points):
            # Returns the Centre of the Box Points
            x = np.float32((points[0][0] + points[1][0] + points[2][0] + points[3][0]) / 4.0)
            y = np.float32((points[0][1] + points[1][1] + points[2][1] + points[3][1]) / 4.0)
            return np.array([np.float32(x), np.float32(y)], np.float32)

        def nothing(x):
            # This function is called as a Call-back everytime the Trackbar is moved
            # Do Nothing
            pass

        def particleEvaluator(back_proj, particle):
            # Function to Evaluate Particles in Each Frame
            return back_proj[particle[1],particle[0]]

        def resample(weights):
            # Function to Resample Particles according to Weights
            n = len(weights)
            indices = []
            C = [0.] + [sum(weights[:i+1]) for i in range(n)]
            u0, j = np.random.random(), 0
            for u in [(u0+i)/n for i in range(n)]:
                while u > C[j]:
                    j+=1
                indices.append(j-1)
            return indices

        # Initializations
        global initTracker
        initTracker = True # Loop the Video frames
        mode = 0 # Switch between MeanShift & CamShift
        initParticles = True # Initiate Particles to Track
        frameCounter = 0 # No. of Frames

        current_mouse_position = np.ones(2, dtype=np.int32)

        global cap

        # Initiate openCV Video Capture Object
        cap = cv.VideoCapture(videoInput)

        # Set Display Windows
        windowSelect = "Target Model Initialization"
        windowHSV = "HSV Histogram Thresholding"

        cv.namedWindow(windowSelect, cv.WINDOW_NORMAL)
        cv.namedWindow(windowHSV, cv.WINDOW_NORMAL)

        # Initiate Kalman Filter Object
        kalman = cv.KalmanFilter(4,2)
        kalman.measurementMatrix = np.array([[1,0,0,0],
                                             [0,1,0,0]],np.float32)

        kalman.transitionMatrix = np.array([[1,0,1,0],
                                            [0,1,0,1],
                                            [0,0,1,0],
                                            [0,0,0,1]],np.float32)

        kalman.processNoiseCov = np.array([[1,0,0,0],
                                           [0,1,0,0],
                                           [0,0,1,0],
                                           [0,0,0,1]],np.float32) * 0.03

        measurement = np.array((2,1), np.float32)
        prediction = np.zeros((2,1), np.float32)

        # Set Trackbars for HSV Selection Thresholds
        s_lower = 60
        cv.createTrackbar("s lower", windowHSV, s_lower, 255, nothing)
        s_upper = 255
        cv.createTrackbar("s upper", windowHSV, s_upper, 255, nothing)
        v_lower = 32
        cv.createTrackbar("v lower", windowHSV, v_lower, 255, nothing)
        v_upper = 255
        cv.createTrackbar("v upper", windowHSV, v_upper, 255, nothing)

        # Set a Mouse Callback
        cv.setMouseCallback(windowSelect, on_Mouse_dragged, 0)
        ROI = False

        # Setup the Termination Criteria for MeanShift(CamShift) Tracker
        #Either 10 Iterations or move by atleast 1 pixel pos. difference
        term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

        while (initTracker):

            if (cap.isOpened):
                # If Video is open
                ret, frame = cap.read()
                ret, frame1 = cap.read()
                ret, frame2 = cap.read()
                ret, frame3 = cap.read()

            # Get Parameters from HSV Trackbars
            s_lower = cv.getTrackbarPos("s lower", windowHSV)
            s_upper = cv.getTrackbarPos("s upper", windowHSV)
            v_lower = cv.getTrackbarPos("v lower", windowHSV)
            v_upper = cv.getTrackbarPos("v upper", windowHSV)

            # Select ROI to Track and Display it
            if (len(self.boxPoints) > 1) and (self.boxPoints[0][1] < self.boxPoints[1][1]) and (self.boxPoints[0][0] < self.boxPoints[1][0]):
                crop = frame[self.boxPoints[0][1]:self.boxPoints[1][1],self.boxPoints[0][0]:self.boxPoints[1][0]].copy()

                h, w, c = crop.shape   # Size of ROI Template
                if (h > 0) and (w > 0):
                    ROI = True

                    # Convert Frame's Color Space (RGB to HSV)
                    hsvROI =  cv.cvtColor(crop, cv.COLOR_BGR2HSV)

                    # Select all Hue (0 - 180) and Saturation values but Eliminate values with very low
                    # Saturation (or value that lacks useful Colour Information)
                    mask = cv.inRange(hsvROI, np.array((0., float(s_lower),float(v_lower))), np.array((180.,float(s_upper),float(v_upper))))

                    # Construct HSV Histogram & Normalize it
                    hsvHist = cv.calcHist([hsvROI],[0, 1],mask,[180, 255],[0,180, 0, 255])
                    cv.normalize(hsvHist,hsvHist,0,255,cv.NORM_MINMAX)

                    # Set Intial Position of Object to Track
                    track_window = (self.boxPoints[0][0],self.boxPoints[0][1],self.boxPoints[1][0] - self.boxPoints[0][0],self.boxPoints[1][1] - self.boxPoints[0][1])
                    #cv.imshow(windowROI,crop)

                # Reset the Coordinates of ROI
                self.boxPoints = []

            # Display ROI Selection
            if (self.selectROI):
                top_left = (self.boxPoints[0][0], self.boxPoints[0][1])
                bottom_right = (current_mouse_position[0], current_mouse_position[1])
                cv.rectangle(frame,top_left, bottom_right, (0,255,0), 2)

            ############################## MeanShift/CamShift Tracker ##############################
            # Adopted from : http://docs.opencv.org/3.1.0/db/df8/tutorial_py_meanshift.html
            # If ROI is Initiated
            if (ROI):

                # Convert Frame's Color Space (RGB to HSV)
                img_hsv = cv.cvtColor(frame1, cv.COLOR_BGR2HSV)

                # Back Projection of Histogram based on Hue and Saturation Values
                img_bproject = cv.calcBackProject([img_hsv],[0,1],hsvHist,[0,180,0,255],1)
                cv.imshow(windowHSV,img_bproject)

                # Apply CamShift or MeanShift to Track New Location
                if mode:
                    ret1, track_window = cv.CamShift(img_bproject, track_window, term_crit)
                    self.CurrentProcess.setText('CamShift Tracker')

                else:
                    ret1, track_window = cv.meanShift(img_bproject, track_window, term_crit)
                    self.CurrentProcess.setText('MeanShift Tracker')

                # Draw Bounding Box over the Tracked Region
                x,y,w,h = track_window
                frame1 = cv.rectangle(frame1, (x,y), (x+w,y+h), (255,0,0),2)
                frame2 = cv.rectangle(frame2, (x,y), (x+w,y+h), (255,0,0),2)
                frame3 = cv.rectangle(frame3, (x,y), (x+w,y+h), (255,0,0),2)

                ############################## Kalman Filter ##############################
                # Adopted from: https://github.com/opencv/opencv/blob/master/samples/python/kalman.py

                # Extract the Centre of the Tracked Region
                pts = np.array([[x,y],[x+w,y],[x+w,y+h],[x,y+h]])

                # Use Extracted Centre for Kalman Correction
                kalman.correct(center(pts))

                # Get New Kalman Filter Prediction
                prediction = kalman.predict()

                # Draw Bounding Box over the Predicted Region
                frame1 = cv.rectangle(frame1, (prediction[0]-(0.5*w),prediction[1]-(0.5*h)), (prediction[0]+(0.5*w),prediction[1]+(0.5*h)), (0,255,255),2)

                ############################## Particle Filter ##############################
                # Adopted from: https://github.com/prateekroy/Computer-Vision/blob/master/HW3/detection_tracking.py

                if (initParticles):

                    # Track Point for the Initial Frame
                    pt = (frameCounter, x+w/2, y+h/2) # Centroid of our Tracking Window from Mean shift
                    frameCounter = frameCounter + 1

                    # Spread 200 - 400 Random Particles near to the Object to Track
                    n_particles = 300

                    init_pos = np.array([x + w/2.0,y + h/2.0], int) # Initial Position
                    particles = np.ones((n_particles, 2), int) * init_pos # Init Particles to init position
                    weights = np.ones(n_particles) / n_particles   # Weights are uniform at first
                    initParticles = False

                # Perform the Tracking
                stepsize = 18; # No. of frames

                # Particle Motion Model: Uniform step
                np.add(particles, np.random.uniform(-stepsize, stepsize, particles.shape), out=particles, casting="unsafe")

                # Clip Out-of-bounds Particles
                particles = particles.clip(np.zeros(2), np.array((frame2.shape[1],frame2.shape[0]))-1).astype(int)

                f = particleEvaluator(img_bproject, particles.T) # Evaluate Particles

                weights = np.float32(f.clip(1))
                weights /= np.sum(weights) # Normalize Weights
                pos = np.sum(particles.T * weights, axis=1).astype(int) # Expected Position: Weighted Average of Particles

                # Coordinates of the Predicted ROI
                a = np.int32(pos[0]) # x-Centre of the ROI
                b = np.int32(pos[1]) # y-Centre of the ROI
                X = np.int32(a-w/2) # x
                Y = np.int32(b-h/2) # y
                X_W = np.int32(a+w/2) # x+w
                Y_H = np.int32(b+h/2) # y+h

                if 1. / np.sum(weights**2) < n_particles / 2.:
                    # If Particle Cloud degenerate resample Particles according to Weights
                    particles = particles[resample(weights),:]
                pt = (frameCounter, np.int32(pos[0]),np.int32(pos[1]))
                frameCounter = frameCounter + 1

                # Draw Bounding Box over the Region Predicted by Particle Filter
                frame2 = cv.rectangle(frame2, (X,Y), (X_W,Y_H), (0,0,255),2)

                ############################## Particle-Kalman Filter ##############################

                # Extract the Centre of the Tracked Region (from the Output of Particle Filter)
                ptsPKF = np.array([[X,Y],[X_W,Y],[X_W,Y_H],[X,Y_H]])

                # Use Extracted Centre for Kalman Correction
                kalman.correct(center(ptsPKF))

                # Get New Kalman Filter Prediction
                predictionPKF = kalman.predict()

                # Draw Bounding Box over the Region Predicted by Particle-Kalman Filter
                frame3 = cv.rectangle(frame3, (predictionPKF[0]-(0.5*w),predictionPKF[1]-(0.5*h)), (predictionPKF[0]+(0.5*w),predictionPKF[1]+(0.5*h)), (0,255,0),2)

            else:

                # If ROI is Not Initiated
                # Convert Frame's Color Space (RGB to HSV)
                img_hsv =  cv.cvtColor(frame1, cv.COLOR_BGR2HSV)

                # Select all Hue (0 - 180) and Saturation values but Eeliminate values with very low
                # Saturation or value that lacks useful Colour Information)
                mask = cv.inRange(img_hsv, np.array((0., float(s_lower),float(v_lower))), np.array((180.,float(s_upper),float(v_upper))))

                cv.imshow(windowHSV,mask)

            # Display Tracking Output
            cv.imshow(windowSelect,frame)

            nkf = cv.resize(frame1, (301, 301))
            frnk = cv.cvtColor(nkf, cv.COLOR_BGR2RGB)
            h, w, ch = frnk.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frnk, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.KFLabel.setPixmap(pixmap)

            npf = cv.resize(frame2, (301, 301))
            frpf = cv.cvtColor(npf, cv.COLOR_BGR2RGB)
            h, w, ch = frpf.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frpf, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.PFLabel.setPixmap(pixmap)

            npkf = cv.resize(frame3, (301, 301))
            frpkf = cv.cvtColor(npkf, cv.COLOR_BGR2RGB)
            h, w, ch = frpkf.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frpkf, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pixmap = QPixmap(convertToQtFormat)
            self.PKFLabel.setPixmap(pixmap)

            key = cv.waitKey(30) & 0xFF
            if key==ord('m'): # Switch between MeanShift & CamShift
                mode=not mode

        # Close All Windows
        cap.release()
        cv.destroyAllWindows()

    def on_Reset_clicked(self):
        global initTracker
        initTracker = False
        self.CurrentProcess.setText('')
        self.PFLabel.clear()
        self.KFLabel.clear()
        self.PKFLabel.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheetahTracker = QtWidgets.QDialog()
    ui = Ui_CheetahTracker()
    ui.setupUi(CheetahTracker)
    CheetahTracker.show()
    sys.exit(app.exec_())
