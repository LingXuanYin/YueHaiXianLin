# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1440, 810)
        MainWindow.setMinimumSize(QSize(1440, 810))
        MainWindow.setMaximumSize(QSize(1440, 810))
        icon = QIcon()
        icon.addFile(u":/images/images/images/titel_icon_small.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setMinimumSize(QSize(1440, 810))
        self.styleSheet.setMaximumSize(QSize(1440, 810))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(3"
                        "3, 37, 43);\n"
"	background-image: url(:/images/images/images/titel_icon.jpg);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(140 ,219 ,247); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"	background-color: rgb(0,184,252);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
""
                        "#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"	background-color: rgb(0,184,252);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(0,184,252);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 12px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{\n"
"	background-c"
                        "olor: rgb(0,184,252)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(140,219,247); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(0,184,252); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#ex"
                        "traTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"	background-color: rgb(0,184,252);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(0,184,252); }\n"
"\n"
"/* Bottom Bar */\n"
"#botto"
                        "mBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"	background-color: rgb(0,184,252);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTab"
                        "leWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(0,184,252);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	bac"
                        "kground-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(0,184,252);\n"
"	selection-background-color: rgb(20,124,255);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(140 ,219 ,247);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(20,124,255);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* //////////////////////////////////"
                        "///////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(0,184,252);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
""
                        "}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: rgb(0,184,252);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     "
                        "background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(40,120,255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(44, 49, 60);\n"
"	border: 3px solid rgb(140 ,219 ,247);\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
""
                        "QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"Q"
                        "ComboBox QAbstractItemView {\n"
"\n"
"	color: rgb(140 ,219 ,247);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(140 ,219 ,247);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(140 ,219 ,247);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(0,184,252);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
                        "	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(140 ,219 ,247);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(140 ,219 ,247);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(0,184,252);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {\n"
"	color: rgb(0,184,252);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {\n"
"	color: rgb(140 ,219 ,247);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"	color: rgb(0,184,252);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////"
                        "//////////////////////////////\n"
"Button */\n"
"#content QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#content QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid #66ccFF;\n"
"}\n"
"#content QPushButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid #66ccFF ;\n"
"}\n"
"#pagesContainer QLineEdit:hover {\n"
"	border: 2px solid #66CCFF ;\n"
"}\n"
"QScrollBar:vertical\n"
"{\n"
"    width:0px;\n"
"    background:rgb(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/titel_icon_small.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy1)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_Cookies = QPushButton(self.topMenu)
        self.btn_Cookies.setObjectName(u"btn_Cookies")
        sizePolicy.setHeightForWidth(self.btn_Cookies.sizePolicy().hasHeightForWidth())
        self.btn_Cookies.setSizePolicy(sizePolicy)
        self.btn_Cookies.setMinimumSize(QSize(0, 45))
        self.btn_Cookies.setFont(font)
        self.btn_Cookies.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Cookies.setLayoutDirection(Qt.LeftToRight)
        self.btn_Cookies.setStyleSheet(u"background-image: url(:/images/images/images/cookie.png);")

        self.verticalLayout_8.addWidget(self.btn_Cookies)

        self.btn_Links = QPushButton(self.topMenu)
        self.btn_Links.setObjectName(u"btn_Links")
        sizePolicy.setHeightForWidth(self.btn_Links.sizePolicy().hasHeightForWidth())
        self.btn_Links.setSizePolicy(sizePolicy)
        self.btn_Links.setMinimumSize(QSize(0, 45))
        self.btn_Links.setFont(font)
        self.btn_Links.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Links.setLayoutDirection(Qt.LeftToRight)
        self.btn_Links.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-link.png);")

        self.verticalLayout_8.addWidget(self.btn_Links)

        self.btn_Pie = QPushButton(self.topMenu)
        self.btn_Pie.setObjectName(u"btn_Pie")
        sizePolicy.setHeightForWidth(self.btn_Pie.sizePolicy().hasHeightForWidth())
        self.btn_Pie.setSizePolicy(sizePolicy)
        self.btn_Pie.setMinimumSize(QSize(0, 45))
        self.btn_Pie.setFont(font)
        self.btn_Pie.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Pie.setLayoutDirection(Qt.LeftToRight)
        self.btn_Pie.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-pie.png);")

        self.verticalLayout_8.addWidget(self.btn_Pie)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Setting_btn = QPushButton(self.extraTopMenu)
        self.Setting_btn.setObjectName(u"Setting_btn")
        self.Setting_btn.setEnabled(False)
        sizePolicy.setHeightForWidth(self.Setting_btn.sizePolicy().hasHeightForWidth())
        self.Setting_btn.setSizePolicy(sizePolicy)
        self.Setting_btn.setMinimumSize(QSize(0, 45))
        self.Setting_btn.setFont(font)
        self.Setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.Setting_btn.setLayoutDirection(Qt.LeftToRight)
        self.Setting_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.Setting_btn)

        self.More_btn = QPushButton(self.extraTopMenu)
        self.More_btn.setObjectName(u"More_btn")
        sizePolicy.setHeightForWidth(self.More_btn.sizePolicy().hasHeightForWidth())
        self.More_btn.setSizePolicy(sizePolicy)
        self.More_btn.setMinimumSize(QSize(0, 45))
        self.More_btn.setFont(font)
        self.More_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.More_btn.setLayoutDirection(Qt.LeftToRight)
        self.More_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.More_btn)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.LeftInfo_TextEdit = QTextEdit(self.extraCenter)
        self.LeftInfo_TextEdit.setObjectName(u"LeftInfo_TextEdit")
        self.LeftInfo_TextEdit.setMinimumSize(QSize(222, 0))
        self.LeftInfo_TextEdit.setStyleSheet(u"background: transparent;")
        self.LeftInfo_TextEdit.setFrameShape(QFrame.NoFrame)
        self.LeftInfo_TextEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.LeftInfo_TextEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"\n"
"font: 12pt \"\u9ed1\u4f53\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon2)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon3)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setEnabled(False)
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon4)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy3)
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.Cookies_Page = QWidget()
        self.Cookies_Page.setObjectName(u"Cookies_Page")
        self.verticalLayout_20 = QVBoxLayout(self.Cookies_Page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.Cookies_widget = QWidget(self.Cookies_Page)
        self.Cookies_widget.setObjectName(u"Cookies_widget")
        sizePolicy3.setHeightForWidth(self.Cookies_widget.sizePolicy().hasHeightForWidth())
        self.Cookies_widget.setSizePolicy(sizePolicy3)
        self.Cookies_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_15 = QVBoxLayout(self.Cookies_widget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.CK_InputFrame = QFrame(self.Cookies_widget)
        self.CK_InputFrame.setObjectName(u"CK_InputFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.CK_InputFrame.sizePolicy().hasHeightForWidth())
        self.CK_InputFrame.setSizePolicy(sizePolicy4)
        self.CK_InputFrame.setFrameShape(QFrame.StyledPanel)
        self.CK_InputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.CK_InputFrame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_title_wid = QFrame(self.CK_InputFrame)
        self.frame_title_wid.setObjectName(u"frame_title_wid")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_title_wid.sizePolicy().hasHeightForWidth())
        self.frame_title_wid.setSizePolicy(sizePolicy5)
        self.frame_title_wid.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_title_wid)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        sizePolicy2.setHeightForWidth(self.labelBoxBlenderInstalation_2.sizePolicy().hasHeightForWidth())
        self.labelBoxBlenderInstalation_2.setSizePolicy(sizePolicy2)
        self.labelBoxBlenderInstalation_2.setMinimumSize(QSize(0, 20))
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.labelBoxBlenderInstalation_2, 0, Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.frame_title_wid, 0, Qt.AlignTop)

        self.frame_content_wid = QFrame(self.CK_InputFrame)
        self.frame_content_wid.setObjectName(u"frame_content_wid")
        sizePolicy5.setHeightForWidth(self.frame_content_wid.sizePolicy().hasHeightForWidth())
        self.frame_content_wid.setSizePolicy(sizePolicy5)
        self.frame_content_wid.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_content_wid)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.CK_Input_textedit = QLineEdit(self.frame_content_wid)
        self.CK_Input_textedit.setObjectName(u"CK_Input_textedit")
        sizePolicy3.setHeightForWidth(self.CK_Input_textedit.sizePolicy().hasHeightForWidth())
        self.CK_Input_textedit.setSizePolicy(sizePolicy3)
        self.CK_Input_textedit.setMinimumSize(QSize(0, 30))
        self.CK_Input_textedit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_2.addWidget(self.CK_Input_textedit, 0, 0, 1, 1, Qt.AlignTop)

        self.CK_Input_btn = QPushButton(self.frame_content_wid)
        self.CK_Input_btn.setObjectName(u"CK_Input_btn")
        self.CK_Input_btn.setMinimumSize(QSize(150, 30))
        self.CK_Input_btn.setFont(font)
        self.CK_Input_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.CK_Input_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CK_Input_btn.setIcon(icon5)

        self.gridLayout_2.addWidget(self.CK_Input_btn, 0, 1, 1, 1, Qt.AlignTop)


        self.horizontalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_26.addWidget(self.frame_content_wid)


        self.verticalLayout_15.addWidget(self.CK_InputFrame)

        self.CK_ButtonFrame_2 = QFrame(self.Cookies_widget)
        self.CK_ButtonFrame_2.setObjectName(u"CK_ButtonFrame_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(200)
        sizePolicy6.setHeightForWidth(self.CK_ButtonFrame_2.sizePolicy().hasHeightForWidth())
        self.CK_ButtonFrame_2.setSizePolicy(sizePolicy6)
        self.CK_ButtonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.CK_ButtonFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.CK_ButtonFrame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.CKSearch_btn = QPushButton(self.CK_ButtonFrame_2)
        self.CKSearch_btn.setObjectName(u"CKSearch_btn")
        sizePolicy5.setHeightForWidth(self.CKSearch_btn.sizePolicy().hasHeightForWidth())
        self.CKSearch_btn.setSizePolicy(sizePolicy5)
        self.CKSearch_btn.setMinimumSize(QSize(48, 48))
        self.CKSearch_btn.setMaximumSize(QSize(48, 48))
        self.CKSearch_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.horizontalLayout_10.addWidget(self.CKSearch_btn, 0, Qt.AlignTop)

        self.CKCheck_btn = QPushButton(self.CK_ButtonFrame_2)
        self.CKCheck_btn.setObjectName(u"CKCheck_btn")
        sizePolicy2.setHeightForWidth(self.CKCheck_btn.sizePolicy().hasHeightForWidth())
        self.CKCheck_btn.setSizePolicy(sizePolicy2)
        self.CKCheck_btn.setMinimumSize(QSize(48, 48))
        self.CKCheck_btn.setMaximumSize(QSize(48, 48))
        self.CKCheck_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-reload.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.CKCheck_btn.setAutoDefault(False)

        self.horizontalLayout_10.addWidget(self.CKCheck_btn, 0, Qt.AlignTop)

        self.CKDelete_btn = QPushButton(self.CK_ButtonFrame_2)
        self.CKDelete_btn.setObjectName(u"CKDelete_btn")
        sizePolicy2.setHeightForWidth(self.CKDelete_btn.sizePolicy().hasHeightForWidth())
        self.CKDelete_btn.setSizePolicy(sizePolicy2)
        self.CKDelete_btn.setMinimumSize(QSize(48, 48))
        self.CKDelete_btn.setMaximumSize(QSize(48, 48))
        self.CKDelete_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/images/images/images/test.png);")

        self.horizontalLayout_10.addWidget(self.CKDelete_btn, 0, Qt.AlignTop)

        self.CKCopy_btn = QPushButton(self.CK_ButtonFrame_2)
        self.CKCopy_btn.setObjectName(u"CKCopy_btn")
        sizePolicy2.setHeightForWidth(self.CKCopy_btn.sizePolicy().hasHeightForWidth())
        self.CKCopy_btn.setSizePolicy(sizePolicy2)
        self.CKCopy_btn.setMinimumSize(QSize(48, 48))
        self.CKCopy_btn.setMaximumSize(QSize(48, 48))
        self.CKCopy_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/icon_restore.png);")

        self.horizontalLayout_10.addWidget(self.CKCopy_btn, 0, Qt.AlignTop)

        self.CKSave_btn = QPushButton(self.CK_ButtonFrame_2)
        self.CKSave_btn.setObjectName(u"CKSave_btn")
        self.CKSave_btn.setMinimumSize(QSize(48, 48))
        self.CKSave_btn.setMaximumSize(QSize(48, 48))
        self.CKSave_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_10.addWidget(self.CKSave_btn, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.CK_ButtonFrame_2, 0, Qt.AlignRight)

        self.CK_Table = QTableWidget(self.Cookies_widget)
        if (self.CK_Table.columnCount() < 4):
            self.CK_Table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.CK_Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.CK_Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.CK_Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.CK_Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.CK_Table.rowCount() < 1):
            self.CK_Table.setRowCount(1)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.CK_Table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.CK_Table.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.CK_Table.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.CK_Table.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.CK_Table.setItem(0, 3, __qtablewidgetitem8)
        self.CK_Table.setObjectName(u"CK_Table")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.CK_Table.sizePolicy().hasHeightForWidth())
        self.CK_Table.setSizePolicy(sizePolicy7)
        self.CK_Table.setMinimumSize(QSize(0, 0))
        self.CK_Table.setBaseSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 44, 52, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(221, 221, 221, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.CK_Table.setPalette(palette)
        self.CK_Table.setStyleSheet(u"border-color: rgb(102, 204, 255);\n"
"")
        self.CK_Table.setFrameShape(QFrame.NoFrame)
        self.CK_Table.setFrameShadow(QFrame.Sunken)
        self.CK_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.CK_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.CK_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.CK_Table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.CK_Table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.CK_Table.setShowGrid(True)
        self.CK_Table.setGridStyle(Qt.SolidLine)
        self.CK_Table.setSortingEnabled(True)
        self.CK_Table.setRowCount(1)
        self.CK_Table.horizontalHeader().setVisible(False)
        self.CK_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.CK_Table.horizontalHeader().setMinimumSectionSize(200)
        self.CK_Table.horizontalHeader().setDefaultSectionSize(250)
        self.CK_Table.horizontalHeader().setHighlightSections(True)
        self.CK_Table.horizontalHeader().setStretchLastSection(True)
        self.CK_Table.verticalHeader().setVisible(False)
        self.CK_Table.verticalHeader().setCascadingSectionResizes(False)
        self.CK_Table.verticalHeader().setDefaultSectionSize(30)
        self.CK_Table.verticalHeader().setHighlightSections(False)
        self.CK_Table.verticalHeader().setProperty("showSortIndicator", False)
        self.CK_Table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.CK_Table)


        self.verticalLayout_20.addWidget(self.Cookies_widget, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.Cookies_Page)
        self.Home_Page = QWidget()
        self.Home_Page.setObjectName(u"Home_Page")
        self.verticalLayout_21 = QVBoxLayout(self.Home_Page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Home_widget = QWidget(self.Home_Page)
        self.Home_widget.setObjectName(u"Home_widget")
        sizePolicy3.setHeightForWidth(self.Home_widget.sizePolicy().hasHeightForWidth())
        self.Home_widget.setSizePolicy(sizePolicy3)
        self.verticalLayout_17 = QVBoxLayout(self.Home_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_2 = QFrame(self.Home_widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.MainLogo_Label = QLabel(self.frame_2)
        self.MainLogo_Label.setObjectName(u"MainLogo_Label")
        sizePolicy3.setHeightForWidth(self.MainLogo_Label.sizePolicy().hasHeightForWidth())
        self.MainLogo_Label.setSizePolicy(sizePolicy3)
        self.MainLogo_Label.setStyleSheet(u"background-image: url(:/images/images/images/MainPage.jpg);\n"
"background-position:centertop;\n"
"background-repeat: no-repeat;")

        self.verticalLayout_25.addWidget(self.MainLogo_Label)


        self.verticalLayout_17.addWidget(self.frame_2)

        self.frame = QFrame(self.Home_widget)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.MainInfo_Label = QLabel(self.frame)
        self.MainInfo_Label.setObjectName(u"MainInfo_Label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.MainInfo_Label.sizePolicy().hasHeightForWidth())
        self.MainInfo_Label.setSizePolicy(sizePolicy8)
        self.MainInfo_Label.setStyleSheet(u"font: 14pt \"\u5b8b\u4f53\";\n"
"color:rgb(102, 204, 255);\n"
"")
        self.MainInfo_Label.setTextFormat(Qt.AutoText)
        self.MainInfo_Label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_24.addWidget(self.MainInfo_Label, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.frame)


        self.verticalLayout_21.addWidget(self.Home_widget)

        self.stackedWidget.addWidget(self.Home_Page)
        self.Charts_Page = QWidget()
        self.Charts_Page.setObjectName(u"Charts_Page")
        self.verticalLayout_23 = QVBoxLayout(self.Charts_Page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.Charts_widget = QWidget(self.Charts_Page)
        self.Charts_widget.setObjectName(u"Charts_widget")
        self.Charts_widget.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.Charts_widget.sizePolicy().hasHeightForWidth())
        self.Charts_widget.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.Charts_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ChartsToolframe = QFrame(self.Charts_widget)
        self.ChartsToolframe.setObjectName(u"ChartsToolframe")
        sizePolicy4.setHeightForWidth(self.ChartsToolframe.sizePolicy().hasHeightForWidth())
        self.ChartsToolframe.setSizePolicy(sizePolicy4)
        self.ChartsToolframe.setFrameShape(QFrame.StyledPanel)
        self.ChartsToolframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.ChartsToolframe)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.ChartsToolframeleft = QFrame(self.ChartsToolframe)
        self.ChartsToolframeleft.setObjectName(u"ChartsToolframeleft")
        sizePolicy4.setHeightForWidth(self.ChartsToolframeleft.sizePolicy().hasHeightForWidth())
        self.ChartsToolframeleft.setSizePolicy(sizePolicy4)
        self.ChartsToolframeleft.setFrameShape(QFrame.StyledPanel)
        self.ChartsToolframeleft.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.ChartsToolframeleft)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label = QLabel(self.ChartsToolframeleft)
        self.label.setObjectName(u"label")
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)
        self.label.setStyleSheet(u"font: 14pt ;")

        self.horizontalLayout_18.addWidget(self.label)

        self.ChartsChoose_Combox = QComboBox(self.ChartsToolframeleft)
        self.ChartsChoose_Combox.setObjectName(u"ChartsChoose_Combox")
        sizePolicy4.setHeightForWidth(self.ChartsChoose_Combox.sizePolicy().hasHeightForWidth())
        self.ChartsChoose_Combox.setSizePolicy(sizePolicy4)
        self.ChartsChoose_Combox.setMinimumSize(QSize(160, 0))
        self.ChartsChoose_Combox.setStyleSheet(u"border-color: rgb(102, 204, 255);\n"
"font: 14pt ;")

        self.horizontalLayout_18.addWidget(self.ChartsChoose_Combox)


        self.horizontalLayout_17.addWidget(self.ChartsToolframeleft, 0, Qt.AlignLeft)

        self.label_prograss = QLabel(self.ChartsToolframe)
        self.label_prograss.setObjectName(u"label_prograss")
        self.label_prograss.setMinimumSize(QSize(200, 0))
        self.label_prograss.setStyleSheet(u"color: rgb(255, 255, 0);")
        self.label_prograss.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_prograss, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.ChartsToolframeright = QFrame(self.ChartsToolframe)
        self.ChartsToolframeright.setObjectName(u"ChartsToolframeright")
        sizePolicy4.setHeightForWidth(self.ChartsToolframeright.sizePolicy().hasHeightForWidth())
        self.ChartsToolframeright.setSizePolicy(sizePolicy4)
        self.ChartsToolframeright.setFrameShape(QFrame.StyledPanel)
        self.ChartsToolframeright.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.ChartsToolframeright)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.CK_ButtonFrame = QFrame(self.ChartsToolframeright)
        self.CK_ButtonFrame.setObjectName(u"CK_ButtonFrame")
        sizePolicy6.setHeightForWidth(self.CK_ButtonFrame.sizePolicy().hasHeightForWidth())
        self.CK_ButtonFrame.setSizePolicy(sizePolicy6)
        self.CK_ButtonFrame.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.CK_ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.CK_ButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.CK_ButtonFrame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.ChartImport_btn = QPushButton(self.CK_ButtonFrame)
        self.ChartImport_btn.setObjectName(u"ChartImport_btn")
        sizePolicy5.setHeightForWidth(self.ChartImport_btn.sizePolicy().hasHeightForWidth())
        self.ChartImport_btn.setSizePolicy(sizePolicy5)
        self.ChartImport_btn.setMinimumSize(QSize(48, 48))
        self.ChartImport_btn.setMaximumSize(QSize(48, 48))
        self.ChartImport_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/cil-input.png);")

        self.horizontalLayout_20.addWidget(self.ChartImport_btn, 0, Qt.AlignTop)

        self.ChartDraw_btn = QPushButton(self.CK_ButtonFrame)
        self.ChartDraw_btn.setObjectName(u"ChartDraw_btn")
        self.ChartDraw_btn.setMinimumSize(QSize(48, 48))
        self.ChartDraw_btn.setMaximumSize(QSize(48, 48))
        self.ChartDraw_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/cil-chart-pie.png);")

        self.horizontalLayout_20.addWidget(self.ChartDraw_btn)

        self.ChartRenew_btn = QPushButton(self.CK_ButtonFrame)
        self.ChartRenew_btn.setObjectName(u"ChartRenew_btn")
        sizePolicy2.setHeightForWidth(self.ChartRenew_btn.sizePolicy().hasHeightForWidth())
        self.ChartRenew_btn.setSizePolicy(sizePolicy2)
        self.ChartRenew_btn.setMinimumSize(QSize(48, 48))
        self.ChartRenew_btn.setMaximumSize(QSize(48, 48))
        self.ChartRenew_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-reload.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.ChartRenew_btn.setAutoDefault(False)

        self.horizontalLayout_20.addWidget(self.ChartRenew_btn, 0, Qt.AlignTop)

        self.ChartDelete_btn = QPushButton(self.CK_ButtonFrame)
        self.ChartDelete_btn.setObjectName(u"ChartDelete_btn")
        sizePolicy2.setHeightForWidth(self.ChartDelete_btn.sizePolicy().hasHeightForWidth())
        self.ChartDelete_btn.setSizePolicy(sizePolicy2)
        self.ChartDelete_btn.setMinimumSize(QSize(48, 48))
        self.ChartDelete_btn.setMaximumSize(QSize(48, 48))
        self.ChartDelete_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/images/images/images/test.png);")

        self.horizontalLayout_20.addWidget(self.ChartDelete_btn, 0, Qt.AlignTop)

        self.ChartCopy_btn = QPushButton(self.CK_ButtonFrame)
        self.ChartCopy_btn.setObjectName(u"ChartCopy_btn")
        sizePolicy2.setHeightForWidth(self.ChartCopy_btn.sizePolicy().hasHeightForWidth())
        self.ChartCopy_btn.setSizePolicy(sizePolicy2)
        self.ChartCopy_btn.setMinimumSize(QSize(48, 48))
        self.ChartCopy_btn.setMaximumSize(QSize(48, 48))
        self.ChartCopy_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/icon_restore.png);")

        self.horizontalLayout_20.addWidget(self.ChartCopy_btn, 0, Qt.AlignTop)

        self.ChartSave_btn = QPushButton(self.CK_ButtonFrame)
        self.ChartSave_btn.setObjectName(u"ChartSave_btn")
        self.ChartSave_btn.setMinimumSize(QSize(48, 48))
        self.ChartSave_btn.setMaximumSize(QSize(48, 48))
        self.ChartSave_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_20.addWidget(self.ChartSave_btn, 0, Qt.AlignTop)


        self.horizontalLayout_19.addWidget(self.CK_ButtonFrame, 0, Qt.AlignRight)


        self.horizontalLayout_17.addWidget(self.ChartsToolframeright)


        self.verticalLayout.addWidget(self.ChartsToolframe)

        self.progressBar = QProgressBar(self.Charts_widget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy9)
        self.progressBar.setMinimumSize(QSize(1290, 3))
        self.progressBar.setMaximumSize(QSize(1272, 3))
        self.progressBar.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.progressBar.setStyleSheet(u"QProgressBar::chunk{\n"
"background: rgb(255,0,0);\n"
"}\n"
"")
        self.progressBar.setInputMethodHints(Qt.ImhNone)
        self.progressBar.setMaximum(4)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout.addWidget(self.progressBar, 0, Qt.AlignHCenter)

        self.Charts_frame = QFrame(self.Charts_widget)
        self.Charts_frame.setObjectName(u"Charts_frame")
        sizePolicy1.setHeightForWidth(self.Charts_frame.sizePolicy().hasHeightForWidth())
        self.Charts_frame.setSizePolicy(sizePolicy1)
        self.Charts_frame.setMinimumSize(QSize(0, 430))
        self.Charts_frame.setStyleSheet(u"background-color: rgb(40, 44, 53);")
        self.Charts_frame.setFrameShape(QFrame.StyledPanel)
        self.Charts_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.Charts_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Chart_1 = QWebEngineView(self.Charts_frame)
        self.Chart_1.setObjectName(u"Chart_1")
        sizePolicy3.setHeightForWidth(self.Chart_1.sizePolicy().hasHeightForWidth())
        self.Chart_1.setSizePolicy(sizePolicy3)
        self.Chart_1.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"QScrollBar\n"
"{\n"
"    width:0px;\n"
"    background:rgb(0,0,0,0%);\n"
"    margin:0px,0px,0px,0px;\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.Chart_1)

        self.Chart_2 = QWebEngineView(self.Charts_frame)
        self.Chart_2.setObjectName(u"Chart_2")
        sizePolicy3.setHeightForWidth(self.Chart_2.sizePolicy().hasHeightForWidth())
        self.Chart_2.setSizePolicy(sizePolicy3)
        self.Chart_2.setStyleSheet(u"background-color: rgb(40, 44, 52);")

        self.horizontalLayout_12.addWidget(self.Chart_2)

        self.Chart_3 = QWebEngineView(self.Charts_frame)
        self.Chart_3.setObjectName(u"Chart_3")
        sizePolicy3.setHeightForWidth(self.Chart_3.sizePolicy().hasHeightForWidth())
        self.Chart_3.setSizePolicy(sizePolicy3)
        self.Chart_3.setStyleSheet(u"background-color: rgb(40, 44, 52);")

        self.horizontalLayout_12.addWidget(self.Chart_3)


        self.verticalLayout.addWidget(self.Charts_frame)

        self.ChartsText_frame = QFrame(self.Charts_widget)
        self.ChartsText_frame.setObjectName(u"ChartsText_frame")
        sizePolicy3.setHeightForWidth(self.ChartsText_frame.sizePolicy().hasHeightForWidth())
        self.ChartsText_frame.setSizePolicy(sizePolicy3)
        self.ChartsText_frame.setFrameShape(QFrame.StyledPanel)
        self.ChartsText_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.ChartsText_frame)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, -1)
        self.ChartsText_label_1 = QLabel(self.ChartsText_frame)
        self.ChartsText_label_1.setObjectName(u"ChartsText_label_1")
        sizePolicy3.setHeightForWidth(self.ChartsText_label_1.sizePolicy().hasHeightForWidth())
        self.ChartsText_label_1.setSizePolicy(sizePolicy3)
        self.ChartsText_label_1.setMaximumSize(QSize(430, 16777215))
        self.ChartsText_label_1.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 0);\n"
"border-color: rgb(102, 204, 255);\n"
"border-style: solid;\n"
"border-radius:7;\n"
"border-width:2px;\n"
"")

        self.horizontalLayout_21.addWidget(self.ChartsText_label_1, 0, Qt.AlignTop)

        self.ChartsText_label_2 = QLabel(self.ChartsText_frame)
        self.ChartsText_label_2.setObjectName(u"ChartsText_label_2")
        sizePolicy3.setHeightForWidth(self.ChartsText_label_2.sizePolicy().hasHeightForWidth())
        self.ChartsText_label_2.setSizePolicy(sizePolicy3)
        self.ChartsText_label_2.setMaximumSize(QSize(430, 16777215))
        self.ChartsText_label_2.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 0);\n"
"border-color: rgb(102, 204, 255);\n"
"border-style: solid;\n"
"border-radius:7;\n"
"border-width:2px;\n"
"")

        self.horizontalLayout_21.addWidget(self.ChartsText_label_2, 0, Qt.AlignTop)

        self.ChartsText_label_3 = QLabel(self.ChartsText_frame)
        self.ChartsText_label_3.setObjectName(u"ChartsText_label_3")
        sizePolicy3.setHeightForWidth(self.ChartsText_label_3.sizePolicy().hasHeightForWidth())
        self.ChartsText_label_3.setSizePolicy(sizePolicy3)
        self.ChartsText_label_3.setMaximumSize(QSize(430, 16777215))
        self.ChartsText_label_3.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 0);\n"
"border-color: rgb(102, 204, 255);\n"
"border-style: solid;\n"
"border-radius:7;\n"
"border-width:2px;\n"
"")

        self.horizontalLayout_21.addWidget(self.ChartsText_label_3, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.ChartsText_frame)


        self.verticalLayout_23.addWidget(self.Charts_widget)

        self.stackedWidget.addWidget(self.Charts_Page)
        self.Links_Page = QWidget()
        self.Links_Page.setObjectName(u"Links_Page")
        self.verticalLayout_22 = QVBoxLayout(self.Links_Page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.Links_widget = QWidget(self.Links_Page)
        self.Links_widget.setObjectName(u"Links_widget")
        sizePolicy2.setHeightForWidth(self.Links_widget.sizePolicy().hasHeightForWidth())
        self.Links_widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_19 = QVBoxLayout(self.Links_widget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.URL_InputFrame = QFrame(self.Links_widget)
        self.URL_InputFrame.setObjectName(u"URL_InputFrame")
        sizePolicy7.setHeightForWidth(self.URL_InputFrame.sizePolicy().hasHeightForWidth())
        self.URL_InputFrame.setSizePolicy(sizePolicy7)
        self.URL_InputFrame.setFrameShape(QFrame.StyledPanel)
        self.URL_InputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.URL_InputFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_title_wid_2 = QFrame(self.URL_InputFrame)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        sizePolicy5.setHeightForWidth(self.labelBoxBlenderInstalation.sizePolicy().hasHeightForWidth())
        self.labelBoxBlenderInstalation.setSizePolicy(sizePolicy5)
        self.labelBoxBlenderInstalation.setMinimumSize(QSize(0, 20))
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_16.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.URL_InputFrame)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        sizePolicy4.setHeightForWidth(self.frame_content_wid_2.sizePolicy().hasHeightForWidth())
        self.frame_content_wid_2.setSizePolicy(sizePolicy4)
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.URL_Input_btn = QPushButton(self.frame_content_wid_2)
        self.URL_Input_btn.setObjectName(u"URL_Input_btn")
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.URL_Input_btn.sizePolicy().hasHeightForWidth())
        self.URL_Input_btn.setSizePolicy(sizePolicy10)
        self.URL_Input_btn.setMinimumSize(QSize(150, 30))
        self.URL_Input_btn.setFont(font)
        self.URL_Input_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.URL_Input_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.URL_Input_btn.setIcon(icon5)

        self.gridLayout.addWidget(self.URL_Input_btn, 1, 1, 1, 1)

        self.URL_Input_textedit = QLineEdit(self.frame_content_wid_2)
        self.URL_Input_textedit.setObjectName(u"URL_Input_textedit")
        self.URL_Input_textedit.setMinimumSize(QSize(0, 30))
        self.URL_Input_textedit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.URL_Input_textedit, 1, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_16.addWidget(self.frame_content_wid_2)


        self.verticalLayout_19.addWidget(self.URL_InputFrame)

        self.URL_ButtonFrame = QFrame(self.Links_widget)
        self.URL_ButtonFrame.setObjectName(u"URL_ButtonFrame")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(200)
        sizePolicy11.setHeightForWidth(self.URL_ButtonFrame.sizePolicy().hasHeightForWidth())
        self.URL_ButtonFrame.setSizePolicy(sizePolicy11)
        self.URL_ButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.URL_ButtonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.URL_ButtonFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_3 = QFrame(self.URL_ButtonFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy8)
        self.label_2.setStyleSheet(u"font: 14pt ;")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.ServersChoose_Combox = QComboBox(self.frame_3)
        self.ServersChoose_Combox.addItem("")
        self.ServersChoose_Combox.setObjectName(u"ServersChoose_Combox")
        self.ServersChoose_Combox.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.ServersChoose_Combox.sizePolicy().hasHeightForWidth())
        self.ServersChoose_Combox.setSizePolicy(sizePolicy8)
        self.ServersChoose_Combox.setMinimumSize(QSize(160, 0))
        self.ServersChoose_Combox.setStyleSheet(u"border-color: rgb(102, 204, 255);\n"
"font: 14pt ;")

        self.horizontalLayout_8.addWidget(self.ServersChoose_Combox)


        self.horizontalLayout_6.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_4 = QFrame(self.URL_ButtonFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.URLSearch_btn = QPushButton(self.frame_4)
        self.URLSearch_btn.setObjectName(u"URLSearch_btn")
        sizePolicy5.setHeightForWidth(self.URLSearch_btn.sizePolicy().hasHeightForWidth())
        self.URLSearch_btn.setSizePolicy(sizePolicy5)
        self.URLSearch_btn.setMinimumSize(QSize(48, 48))
        self.URLSearch_btn.setMaximumSize(QSize(48, 48))
        self.URLSearch_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/cil-find-in-page.png);")

        self.horizontalLayout_13.addWidget(self.URLSearch_btn)

        self.URLCheck_btn = QPushButton(self.frame_4)
        self.URLCheck_btn.setObjectName(u"URLCheck_btn")
        sizePolicy2.setHeightForWidth(self.URLCheck_btn.sizePolicy().hasHeightForWidth())
        self.URLCheck_btn.setSizePolicy(sizePolicy2)
        self.URLCheck_btn.setMinimumSize(QSize(48, 48))
        self.URLCheck_btn.setMaximumSize(QSize(48, 48))
        self.URLCheck_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-reload.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.URLCheck_btn.setAutoDefault(False)

        self.horizontalLayout_13.addWidget(self.URLCheck_btn)

        self.URLDelete_btn = QPushButton(self.frame_4)
        self.URLDelete_btn.setObjectName(u"URLDelete_btn")
        sizePolicy2.setHeightForWidth(self.URLDelete_btn.sizePolicy().hasHeightForWidth())
        self.URLDelete_btn.setSizePolicy(sizePolicy2)
        self.URLDelete_btn.setMinimumSize(QSize(48, 48))
        self.URLDelete_btn.setMaximumSize(QSize(48, 48))
        self.URLDelete_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/images/images/images/test.png);")

        self.horizontalLayout_13.addWidget(self.URLDelete_btn)

        self.URLCopy_btn = QPushButton(self.frame_4)
        self.URLCopy_btn.setObjectName(u"URLCopy_btn")
        sizePolicy2.setHeightForWidth(self.URLCopy_btn.sizePolicy().hasHeightForWidth())
        self.URLCopy_btn.setSizePolicy(sizePolicy2)
        self.URLCopy_btn.setMinimumSize(QSize(48, 48))
        self.URLCopy_btn.setMaximumSize(QSize(48, 48))
        self.URLCopy_btn.setStyleSheet(u"background-position:center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/icon_restore.png);")

        self.horizontalLayout_13.addWidget(self.URLCopy_btn)

        self.URLSave_btn = QPushButton(self.frame_4)
        self.URLSave_btn.setObjectName(u"URLSave_btn")
        sizePolicy8.setHeightForWidth(self.URLSave_btn.sizePolicy().hasHeightForWidth())
        self.URLSave_btn.setSizePolicy(sizePolicy8)
        self.URLSave_btn.setMinimumSize(QSize(48, 48))
        self.URLSave_btn.setMaximumSize(QSize(48, 48))
        self.URLSave_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")

        self.horizontalLayout_13.addWidget(self.URLSave_btn)


        self.horizontalLayout_6.addWidget(self.frame_4, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.URL_ButtonFrame)

        self.Links_Table = QTableWidget(self.Links_widget)
        if (self.Links_Table.columnCount() < 4):
            self.Links_Table.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Links_Table.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Links_Table.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Links_Table.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Links_Table.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        if (self.Links_Table.rowCount() < 1):
            self.Links_Table.setRowCount(1)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.Links_Table.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Links_Table.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Links_Table.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Links_Table.setItem(0, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Links_Table.setItem(0, 3, __qtablewidgetitem17)
        self.Links_Table.setObjectName(u"Links_Table")
        sizePolicy7.setHeightForWidth(self.Links_Table.sizePolicy().hasHeightForWidth())
        self.Links_Table.setSizePolicy(sizePolicy7)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.Links_Table.setPalette(palette1)
        self.Links_Table.setStyleSheet(u"border-color: rgb(102, 204, 255);\n"
"")
        self.Links_Table.setFrameShape(QFrame.NoFrame)
        self.Links_Table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Links_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Links_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Links_Table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Links_Table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.Links_Table.setShowGrid(True)
        self.Links_Table.setGridStyle(Qt.SolidLine)
        self.Links_Table.setSortingEnabled(True)
        self.Links_Table.setRowCount(1)
        self.Links_Table.horizontalHeader().setVisible(False)
        self.Links_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Links_Table.horizontalHeader().setMinimumSectionSize(200)
        self.Links_Table.horizontalHeader().setDefaultSectionSize(250)
        self.Links_Table.horizontalHeader().setStretchLastSection(True)
        self.Links_Table.verticalHeader().setVisible(False)
        self.Links_Table.verticalHeader().setCascadingSectionResizes(False)
        self.Links_Table.verticalHeader().setMinimumSectionSize(25)
        self.Links_Table.verticalHeader().setDefaultSectionSize(30)
        self.Links_Table.verticalHeader().setHighlightSections(False)
        self.Links_Table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_19.addWidget(self.Links_Table)


        self.verticalLayout_22.addWidget(self.Links_widget, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.Links_Page)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.Main_widget = QWidget(self.content)
        self.Main_widget.setObjectName(u"Main_widget")
        sizePolicy3.setHeightForWidth(self.Main_widget.sizePolicy().hasHeightForWidth())
        self.Main_widget.setSizePolicy(sizePolicy3)
        self.Main_widget.setMaximumSize(QSize(0, 16777215))
        self.horizontalLayout_7 = QHBoxLayout(self.Main_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.horizontalLayout_4.addWidget(self.Main_widget)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel, 0, Qt.AlignLeft)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version, 0, Qt.AlignRight)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u6708\u6d77\u4ed9\u9e9f", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"v2.0.0.Beta", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Cookies.setText(QCoreApplication.translate("MainWindow", u"Cookies", None))
        self.btn_Links.setText(QCoreApplication.translate("MainWindow", u"Links", None))
        self.btn_Pie.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText("")
        self.extraLabel.setText("")
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.Setting_btn.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.More_btn.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.LeftInfo_TextEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">\u6708\u6d77\u4ed9\u9e9f</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u539f\u795e\u62bd\u5361\u94fe\u63a5\u548c\u7c73\u6e38\u793eCookies\u7684\u7efc\u5408\u5de5\u5177</span></p"
                        ">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: \u5357\u8fb0\u71cf\u709a</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"TEST INFO", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Import File Or Cookies String From Browser\uff1a</span></p></body></html>", None))
        self.CK_Input_textedit.setText("")
        self.CK_Input_textedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Path Or Cookies", None))
        self.CK_Input_btn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.CKSearch_btn.setText("")
        self.CKCheck_btn.setText("")
        self.CKDelete_btn.setText("")
        self.CKCopy_btn.setText("")
        self.CKSave_btn.setText("")
        ___qtablewidgetitem = self.CK_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"UID", None));
        ___qtablewidgetitem1 = self.CK_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668", None));
        ___qtablewidgetitem2 = self.CK_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u53ef\u7528", None));
        ___qtablewidgetitem3 = self.CK_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Cookies", None));
        ___qtablewidgetitem4 = self.CK_Table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.CK_Table.isSortingEnabled()
        self.CK_Table.setSortingEnabled(False)
        self.CK_Table.setSortingEnabled(__sortingEnabled)

        self.MainLogo_Label.setText("")
        self.MainInfo_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u7948\u613f\u8bb0\u5f55\u94fe\u63a5\u66f4\u65b0\u65b9\u5f0f\uff1a</span></p><p>\u8fdb\u5165 \u539f\u795e-&gt;\u62bd\u5361\u754c\u9762-&gt;\u5386\u53f2\u8bb0\u5f55-&gt;\u62bd\u5361\u754c\u9762-&gt;\u8f6f\u4ef6\u5185\u70b9\u51fb\u5de6\u4fa7Charts-&gt;\u53f3\u4fa7\u5237\u65b0\u6309\u94ae</p><p>\u7b2c\u4e00\u6b21\u4f7f\u7528\u9700\u8981\u9009\u62e9\u6e38\u620f\u5b89\u88c5\u76ee\u5f55\uff08\u5305\u542bYuanShen.exe\u6216GenshinImpact.exe\uff09</p><p><br/></p><p><span style=\" font-weight:700;\">\u7c73\u6e38\u793eCookie\u83b7\u53d6\u65b9\u5f0f\uff1a</span></p><p>\u4f7f\u7528Chrome\u6d4f\u89c8\u5668\u767b\u5f55\u7c73\u6e38\u793e-&gt;\u8f6f\u4ef6\u5185\u70b9\u51fb\u5de6\u4fa7Cookies-&gt;\u53f3\u4fa7\u70b9\u51fb\u6700\u5de6\u8fb9\u6309\u94ae</p><p><span style=\" font-size:10pt;\">\u6ce8\uff1a\u591a\u8d26\u53f7\u8bf7\u6253\u5f00\u6d4f\u89c8\u5668\u9690\u8eab\u6a21\u5f0f\uff0c\u5f00\u53d1\u8005\u6a21\u5f0f\u8f93\u5165\u2018document.cookie\u2019\u590d\u5236\u8f93\u51fa"
                        "\u4fe1\u606f\u540e\u624b\u52a8\u5bfc\u5165</span></p><p><br/></p><p><br/><a href=\"https://github.com/LingXuanYin\"><span style=\" text-decoration: underline; color:#66ccff;\">\u5357\u8fb0\u71cf\u709a@github</span></a></p><p><a href=\"https://github.com/LingXuanYin\"><span style=\" text-decoration: underline; color:#66ccff;\">\u5357\u8fb0\u71cf\u709a@</span></a><a href=\"https://space.bilibili.com/162599415\"><span style=\" text-decoration: underline; color:#66ccff;\">bilibili</span></a></p><p><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"UID : ", None))
        self.label_prograss.setText("")
        self.ChartImport_btn.setText("")
        self.ChartDraw_btn.setText("")
        self.ChartRenew_btn.setText("")
        self.ChartDelete_btn.setText("")
        self.ChartCopy_btn.setText("")
        self.ChartSave_btn.setText("")
        self.ChartsText_label_1.setText("")
        self.ChartsText_label_2.setText("")
        self.ChartsText_label_3.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Import File Or URL\uff1a</span></p></body></html>", None))
        self.URL_Input_btn.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.URL_Input_textedit.setText("")
        self.URL_Input_textedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"File Path Or URL", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Server : ", None))
        self.ServersChoose_Combox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Servers", None))

        self.URLSearch_btn.setText("")
        self.URLCheck_btn.setText("")
        self.URLDelete_btn.setText("")
        self.URLCopy_btn.setText("")
        self.URLSave_btn.setText("")
        ___qtablewidgetitem5 = self.Links_Table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"UID", None));
        ___qtablewidgetitem6 = self.Links_Table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668", None));
        ___qtablewidgetitem7 = self.Links_Table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u53ef\u7528", None));
        ___qtablewidgetitem8 = self.Links_Table.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"URL", None));
        ___qtablewidgetitem9 = self.Links_Table.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled1 = self.Links_Table.isSortingEnabled()
        self.Links_Table.setSortingEnabled(False)
        self.Links_Table.setSortingEnabled(__sortingEnabled1)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \u5357\u8fb0\u71cf\u709a", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v2.0.0.Beta", None))
    # retranslateUi

