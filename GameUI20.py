# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        MainWindow.resize(1114, 759)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 570, 1071, 141))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.BottomBar = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.BottomBar.setObjectName(_fromUtf8("BottomBar"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.StartStop = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.StartStop.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartStop.setFont(font)
        self.StartStop.setObjectName(_fromUtf8("StartStop"))
        self.verticalLayout_4.addWidget(self.StartStop)
        self.Tick = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.Tick.setMinimumSize(QtCore.QSize(0, 35))
        self.Tick.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Tick.setFont(font)
        self.Tick.setAutoDefault(False)
        self.Tick.setDefault(False)
        self.Tick.setFlat(False)
        self.Tick.setObjectName(_fromUtf8("Tick"))
        self.verticalLayout_4.addWidget(self.Tick)
        self.ToBegin = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.ToBegin.setEnabled(True)
        self.ToBegin.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ToBegin.setFont(font)
        self.ToBegin.setObjectName(_fromUtf8("ToBegin"))
        self.verticalLayout_4.addWidget(self.ToBegin)
        self.BottomBar.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.LPresets = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LPresets.setFont(font)
        self.LPresets.setTextFormat(QtCore.Qt.AutoText)
        self.LPresets.setAlignment(QtCore.Qt.AlignCenter)
        self.LPresets.setWordWrap(False)
        self.LPresets.setObjectName(_fromUtf8("LPresets"))
        self.horizontalLayout_2.addWidget(self.LPresets)
        self.ChoicePresets = QtGui.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ChoicePresets.setFont(font)
        self.ChoicePresets.setEditable(False)
        self.ChoicePresets.setFrame(True)
        self.ChoicePresets.setObjectName(_fromUtf8("ChoicePresets"))
        self.horizontalLayout_2.addWidget(self.ChoicePresets)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Blank = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Blank.setFont(font)
        self.Blank.setObjectName(_fromUtf8("Blank"))
        self.verticalLayout.addWidget(self.Blank)
        self.RandomStart = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RandomStart.setFont(font)
        self.RandomStart.setToolTip(_fromUtf8(""))
        self.RandomStart.setIconSize(QtCore.QSize(200, 200))
        self.RandomStart.setObjectName(_fromUtf8("RandomStart"))
        self.verticalLayout.addWidget(self.RandomStart)
        self.EditRules = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EditRules.setFont(font)
        self.EditRules.setIconSize(QtCore.QSize(200, 200))
        self.EditRules.setObjectName(_fromUtf8("EditRules"))
        self.verticalLayout.addWidget(self.EditRules)
        self.BottomBar.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.SaveState = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SaveState.setFont(font)
        self.SaveState.setObjectName(_fromUtf8("SaveState"))
        self.verticalLayout_3.addWidget(self.SaveState)
        self.RemovePreset = QtGui.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RemovePreset.setFont(font)
        self.RemovePreset.setObjectName(_fromUtf8("RemovePreset"))
        self.verticalLayout_3.addWidget(self.RemovePreset)
        self.BottomBar.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(800, 20, 297, 521))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.RightBar = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.RightBar.setObjectName(_fromUtf8("RightBar"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.FPSL = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.FPSL.setMinimumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FPSL.setFont(font)
        self.FPSL.setAlignment(QtCore.Qt.AlignCenter)
        self.FPSL.setObjectName(_fromUtf8("FPSL"))
        self.gridLayout.addWidget(self.FPSL, 0, 0, 1, 1)
        self.FPSSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget_5)
        self.FPSSpinBox.setMinimumSize(QtCore.QSize(50, 50))
        self.FPSSpinBox.setReadOnly(False)
        self.FPSSpinBox.setKeyboardTracking(False)
        self.FPSSpinBox.setDecimals(2)
        self.FPSSpinBox.setMinimum(0.01)
        self.FPSSpinBox.setMaximum(1001.0)
        self.FPSSpinBox.setSingleStep(1.0)
        self.FPSSpinBox.setProperty("value", 8.0)
        self.FPSSpinBox.setObjectName(_fromUtf8("FPSSpinBox"))
        self.gridLayout.addWidget(self.FPSSpinBox, 0, 1, 1, 1)
        self.RightBar.addLayout(self.gridLayout)
        self.LDelay = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.LDelay.setMinimumSize(QtCore.QSize(0, 60))
        self.LDelay.setMaximumSize(QtCore.QSize(16777215, 50))
        self.LDelay.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LDelay.setFont(font)
        self.LDelay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LDelay.setFrameShape(QtGui.QFrame.NoFrame)
        self.LDelay.setScaledContents(False)
        self.LDelay.setAlignment(QtCore.Qt.AlignCenter)
        self.LDelay.setObjectName(_fromUtf8("LDelay"))
        self.RightBar.addWidget(self.LDelay)
        self.LGeneration = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.LGeneration.setMaximumSize(QtCore.QSize(16777215, 40))
        self.LGeneration.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LGeneration.setFont(font)
        self.LGeneration.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LGeneration.setFrameShape(QtGui.QFrame.NoFrame)
        self.LGeneration.setAlignment(QtCore.Qt.AlignCenter)
        self.LGeneration.setObjectName(_fromUtf8("LGeneration"))
        self.RightBar.addWidget(self.LGeneration)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(10, 0, 30, -1)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.PlagueCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlagueCheckBox.sizePolicy().hasHeightForWidth())
        self.PlagueCheckBox.setSizePolicy(sizePolicy)
        self.PlagueCheckBox.setSizeIncrement(QtCore.QSize(0, 50))
        self.PlagueCheckBox.setBaseSize(QtCore.QSize(50, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PlagueCheckBox.setFont(font)
        self.PlagueCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PlagueCheckBox.setAutoFillBackground(True)
        self.PlagueCheckBox.setObjectName(_fromUtf8("PlagueCheckBox"))
        self.horizontalLayout_5.addWidget(self.PlagueCheckBox)
        self.RandomInfection = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.RandomInfection.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RandomInfection.sizePolicy().hasHeightForWidth())
        self.RandomInfection.setSizePolicy(sizePolicy)
        self.RandomInfection.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RandomInfection.setFont(font)
        self.RandomInfection.setObjectName(_fromUtf8("RandomInfection"))
        self.horizontalLayout_5.addWidget(self.RandomInfection)
        self.RightBar.addLayout(self.horizontalLayout_5)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.RightBar.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.RightBar.addItem(spacerItem1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.ScaleIn = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.ScaleIn.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ScaleIn.setFont(font)
        self.ScaleIn.setFlat(False)
        self.ScaleIn.setObjectName(_fromUtf8("ScaleIn"))
        self.horizontalLayout_4.addWidget(self.ScaleIn)
        self.ScaleOut = QtGui.QPushButton(self.verticalLayoutWidget_5)
        self.ScaleOut.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ScaleOut.setFont(font)
        self.ScaleOut.setObjectName(_fromUtf8("ScaleOut"))
        self.horizontalLayout_4.addWidget(self.ScaleOut)
        self.RightBar.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.LSize = QtGui.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LSize.setFont(font)
        self.LSize.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.LSize.setAlignment(QtCore.Qt.AlignCenter)
        self.LSize.setObjectName(_fromUtf8("LSize"))
        self.horizontalLayout.addWidget(self.LSize)
        self.RowsColumsCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RowsColumsCheckBox.setFont(font)
        self.RowsColumsCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RowsColumsCheckBox.setAutoFillBackground(False)
        self.RowsColumsCheckBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.RowsColumsCheckBox.setIconSize(QtCore.QSize(24, 24))
        self.RowsColumsCheckBox.setChecked(True)
        self.RowsColumsCheckBox.setObjectName(_fromUtf8("RowsColumsCheckBox"))
        self.horizontalLayout.addWidget(self.RowsColumsCheckBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.LRows = QtGui.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LRows.setFont(font)
        self.LRows.setAlignment(QtCore.Qt.AlignCenter)
        self.LRows.setObjectName(_fromUtf8("LRows"))
        self.horizontalLayout_3.addWidget(self.LRows)
        self.RowsSpinBox = QtGui.QSpinBox(self.verticalLayoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RowsSpinBox.sizePolicy().hasHeightForWidth())
        self.RowsSpinBox.setSizePolicy(sizePolicy)
        self.RowsSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.RowsSpinBox.setMinimum(1)
        self.RowsSpinBox.setMaximum(1000)
        self.RowsSpinBox.setProperty("value", 10)
        self.RowsSpinBox.setObjectName(_fromUtf8("RowsSpinBox"))
        self.horizontalLayout_3.addWidget(self.RowsSpinBox)
        self.LColums = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.LColums.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LColums.setFont(font)
        self.LColums.setAlignment(QtCore.Qt.AlignCenter)
        self.LColums.setObjectName(_fromUtf8("LColums"))
        self.horizontalLayout_3.addWidget(self.LColums)
        self.ColumnsSpinBox = QtGui.QSpinBox(self.verticalLayoutWidget_5)
        self.ColumnsSpinBox.setEnabled(False)
        self.ColumnsSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        self.ColumnsSpinBox.setMinimum(1)
        self.ColumnsSpinBox.setMaximum(1000)
        self.ColumnsSpinBox.setProperty("value", 10)
        self.ColumnsSpinBox.setObjectName(_fromUtf8("ColumnsSpinBox"))
        self.horizontalLayout_3.addWidget(self.ColumnsSpinBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.RightBar.addLayout(self.verticalLayout_6)
        self.groupBox_B = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_B.setGeometry(QtCore.QRect(10, 560, 1091, 151))
        self.groupBox_B.setTitle(_fromUtf8(""))
        self.groupBox_B.setObjectName(_fromUtf8("groupBox_B"))
        self.groupBox_R = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_R.setGeometry(QtCore.QRect(790, 10, 311, 541))
        self.groupBox_R.setTitle(_fromUtf8(""))
        self.groupBox_R.setFlat(False)
        self.groupBox_R.setCheckable(False)
        self.groupBox_R.setObjectName(_fromUtf8("groupBox_R"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 761, 531))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.groupBox_B.raise_()
        self.groupBox_R.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.graphicsView.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.LPresets.setBuddy(self.ChoicePresets)
        self.FPSL.setBuddy(self.FPSSpinBox)
        self.LRows.setBuddy(self.RowsSpinBox)
        self.LColums.setBuddy(self.ColumnsSpinBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Game of life", None))
        self.StartStop.setToolTip(_translate("MainWindow", "Start automatic generation with desired FPS.\n"
"Shortcut: space", None))
        self.StartStop.setText(_translate("MainWindow", "Start/Stop", None))
        self.StartStop.setShortcut(_translate("MainWindow", "Space", None))
        self.Tick.setToolTip(_translate("MainWindow", "Moves 1 generation ahead.\n"
"Shortcut: right arrow", None))
        self.Tick.setText(_translate("MainWindow", "Tick", None))
        self.Tick.setShortcut(_translate("MainWindow", "Right", None))
        self.ToBegin.setToolTip(_translate("MainWindow", "With this button you can always come back to the state \n"
"when you edited the setup at generetion 0\n"
"Shortcut: left arrow", None))
        self.ToBegin.setText(_translate("MainWindow", "Back to beginning", None))
        self.ToBegin.setShortcut(_translate("MainWindow", "Left", None))
        self.LPresets.setToolTip(_translate("MainWindow", "Save and load your presets", None))
        self.LPresets.setText(_translate("MainWindow", "Presets:", None))
        self.ChoicePresets.setStatusTip(_translate("MainWindow", "aaa", None))
        self.Blank.setToolTip(_translate("MainWindow", "Sets generation to 0 and makes every cell dead", None))
        self.Blank.setText(_translate("MainWindow", "New Life", None))
        self.RandomStart.setText(_translate("MainWindow", "Randomize", None))
        self.EditRules.setToolTip(_translate("MainWindow", "When cell dies, stays allive...", None))
        self.EditRules.setText(_translate("MainWindow", "Edit rules", None))
        self.SaveState.setToolTip(_translate("MainWindow", "You can save what you see. ", None))
        self.SaveState.setText(_translate("MainWindow", "Save current \n"
"state as preset", None))
        self.RemovePreset.setToolTip(_translate("MainWindow", "Nothing to explain", None))
        self.RemovePreset.setText(_translate("MainWindow", "Remove Current\n"
"Preset", None))
        self.FPSL.setToolTip(_translate("MainWindow", "Frames per second", None))
        self.FPSL.setText(_translate("MainWindow", "FPS:", None))
        self.FPSSpinBox.setToolTip(_translate("MainWindow", "Frames per second", None))
        self.LDelay.setText(_translate("MainWindow", "Last generation took:\n"
"0 sec.to calculate", None))
        self.LGeneration.setText(_translate("MainWindow", "Generation: 0", None))
        self.PlagueCheckBox.setToolTip(_translate("MainWindow", "In plague mode you can \n"
"infect cells with right mouse\n"
"button. They wil die after 1 \n"
"generations and infect other \n"
"cells. \n"
" They are marked with purple.", None))
        self.PlagueCheckBox.setText(_translate("MainWindow", "Plague mode", None))
        self.RandomInfection.setToolTip(_translate("MainWindow", "Disaster! Random infection!", None))
        self.RandomInfection.setText(_translate("MainWindow", "Random", None))
        self.ScaleIn.setToolTip(_translate("MainWindow", "Scale + 10%\n"
"You can use mouse wheel too", None))
        self.ScaleIn.setText(_translate("MainWindow", "Scale +", None))
        self.ScaleOut.setToolTip(_translate("MainWindow", "Scale - 10%\n"
"You can use mouse wheel too", None))
        self.ScaleOut.setText(_translate("MainWindow", "Scale -", None))
        self.LSize.setText(_translate("MainWindow", "Size of living area:", None))
        self.RowsColumsCheckBox.setText(_translate("MainWindow", "Rows = Colums", None))
        self.LRows.setText(_translate("MainWindow", "Rows:", None))
        self.LColums.setText(_translate("MainWindow", "Columns", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Bye bye :(", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setToolTip(_translate("MainWindow", "Info about author and program itself", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

