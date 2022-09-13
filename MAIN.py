# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
# from PySide6 import QtWebEngineCore
import sys
import os
from PySide6 import QtWebEngineCore
from PySide6.QtWidgets import QMainWindow, QHeaderView, QApplication

from modules import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

_doNOTHING_func_count = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        widgets.MainInfo_Label.setOpenExternalLinks(True)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        # Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "月海仙麟"
        description = "原神抽卡记录数据统计"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        #
        # web echarts setting
        _aubot_blank = """<html><body style=" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;background-color: rgb(40, 44, 52);"></body></html>"""
        widgets.Chart_1.setHtml(_aubot_blank)
        widgets.Chart_2.setHtml(_aubot_blank)
        widgets.Chart_3.setHtml(_aubot_blank)
        widgets.Chart_1.page().settings().setAttribute(QtWebEngineCore.QWebEngineSettings.ShowScrollBars, False)
        widgets.Chart_2.page().settings().setAttribute(QtWebEngineCore.QWebEngineSettings.ShowScrollBars, False)
        widgets.Chart_3.page().settings().setAttribute(QtWebEngineCore.QWebEngineSettings.ShowScrollBars, False)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        #
        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.Links_Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_Links.clicked.connect(self.buttonClick)
        widgets.btn_Cookies.clicked.connect(self.buttonClick)
        widgets.btn_Pie.clicked.connect(self.buttonClick)
        widgets.btn_exit.clicked.connect(self.buttonClick)
        widgets.Setting_btn.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        widgets.Links_Table.horizontalHeader().setVisible(True)
        widgets.CK_Table.horizontalHeader().setVisible(True)
        widgets.stackedWidget.setCurrentWidget(widgets.Home_Page)

        widgets.ChartRenew_btn.clicked.connect(self.buttonClick)
        widgets.ChartImport_btn.clicked.connect(self.buttonClick)
        widgets.ChartDelete_btn.clicked.connect(self.buttonClick)
        widgets.ChartCopy_btn.clicked.connect(self.buttonClick)
        widgets.ChartSave_btn.clicked.connect(self.buttonClick)
        widgets.ChartDraw_btn.clicked.connect(self.buttonClick)
        widgets.URLSearch_btn.clicked.connect(self.buttonClick)
        widgets.URLCheck_btn.clicked.connect(self.buttonClick)
        widgets.URLDelete_btn.clicked.connect(self.buttonClick)
        widgets.URLCopy_btn.clicked.connect(self.buttonClick)
        widgets.URLSave_btn.clicked.connect(self.buttonClick)
        widgets.URL_Input_btn.clicked.connect(self.buttonClick)
        widgets.CKSearch_btn.clicked.connect(self.buttonClick)
        widgets.CKCheck_btn.clicked.connect(self.buttonClick)
        widgets.CKDelete_btn.clicked.connect(self.buttonClick)
        widgets.CKCopy_btn.clicked.connect(self.buttonClick)
        widgets.CKSave_btn.clicked.connect(self.buttonClick)
        widgets.CK_Input_btn.clicked.connect(self.buttonClick)

        def URL_Input_texteditChanged():
            AppFunctions.Links_import_TextEditor(self)

        def CK_Input_texteditChanged():
            AppFunctions.Cookies_import_TextEditor(self)

        widgets.URL_Input_textedit.textChanged.connect(URL_Input_texteditChanged)
        widgets.CK_Input_textedit.textChanged.connect(CK_Input_texteditChanged)
        widgets.ChartsText_label_1.setWordWrap(True)
        widgets.ChartsText_label_2.setWordWrap(True)
        widgets.ChartsText_label_3.setWordWrap(True)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)

        def _doNOTHING_func():
            global _doNOTHING_func_count
            if _doNOTHING_func_count == 0:

                QMessageBox.warning(self, '这是一个没有卵用的警告', '这是一个没有卵用的按钮')
                _doNOTHING_func_count += 1
            elif _doNOTHING_func_count == 1:
                QMessageBox.warning(self, '这是一个没有卵用的警告!!!', '这是一个没有卵用的按钮!!!')
                _doNOTHING_func_count += 1
            elif _doNOTHING_func_count >= 2:
                if _doNOTHING_func_count >= 100:
                    QMessageBox.warning(self, '恭喜你解锁了一个成就', '这是一个赛博奖杯，谁也看不见，现在你可以重头开始了')
                    _doNOTHING_func_count = 0
                else:
                    QMessageBox.warning(self, '你还点!!!', '反正点了也没用')
                    _doNOTHING_func_count += 1

        widgets.settingsTopBtn.clicked.connect(_doNOTHING_func)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_dark.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.Home_Page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_Links":
            self.ui.stackedWidget.setCurrentWidget(self.ui.Links_Page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            AppFunctions.Links_pageLoad(self)
        # SHOW NEW PAGE
        if btnName == "btn_Cookies":
            self.ui.stackedWidget.setCurrentWidget(self.ui.Cookies_Page)
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            AppFunctions.Cookies_Pageload(self)

        # SHOW NEW PAGE
        if btnName == "btn_Pie":
            self.ui.stackedWidget.setCurrentWidget(self.ui.Charts_Page)
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            AppFunctions.Chart_pageLoad(self)

        # Exit Button
        if btnName == "btn_exit":
            widgets.closeAppBtn.click()
        # Setting Button
        if btnName == "Setting_btn":
            widgets.stackedWidget.setCurrentWidget(widgets.Setting_Page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
        # ChartRenew_btn
        if btnName == "ChartRenew_btn":
            AppFunctions.Chart_renew(self)
        if btnName == 'ChartImport_btn':
            AppFunctions.Chart_import(self)
        if btnName == 'ChartDelete_btn':
            AppFunctions.Chart_delete(self)
        if btnName == 'ChartCopy_btn':
            AppFunctions.Chart_copy(self)
        if btnName == 'ChartSave_btn':
            AppFunctions.Chart_save(self)
        if btnName == 'ChartDraw_btn':
            AppFunctions.Chart_draw(self)
        if btnName == 'URLSearch_btn':
            AppFunctions.Links_search(self)
        if btnName == 'URLCheck_btn':
            AppFunctions.Links_check(self)
        if btnName == 'URLDelete_btn':
            AppFunctions.Links_delete(self)
        if btnName == 'URLCopy_btn':
            AppFunctions.Links_copy(self)
        if btnName == 'URLSave_btn':
            AppFunctions.Links_save(self)
        if btnName == 'URL_Input_btn':
            AppFunctions.Links_import_btn(self)
        if btnName == 'CKSearch_btn':
            AppFunctions.Cookies_search(self)
        if btnName == 'CKCheck_btn':
            AppFunctions.Cookies_check(self)
        if btnName == 'CKDelete_btn':
            AppFunctions.Cookies_delete(self)
        if btnName == 'CKCopy_btn':
            AppFunctions.Cookies_copy(self)
        if btnName == 'CKSave_btn':
            AppFunctions.Cookies_save(self)
        if btnName == 'CK_Input_btn':
            AppFunctions.Cookies_import_btn(self)

        # PRINT BTN NAME
        # print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS

    # ///////////////////////////////////////////////////////////////
    # def resizeEvent(self, event):
    #     # Update Size Grips
    #     #UIFunctions.resize_grips(self)
    #     pass

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


def Initialization():

    jsonfile_init_list = {
        './DATA/Cookies.json': '{}',
        './DATA/GamePath.json': '{"CN":"","OS":""}',
        './DATA/URL.json': '{}',
        './DATA/UserData.json': '{}',
    }
    dir_init_list = [
        './cache',
        './DATA',
        './DATA/charts'
    ]
    for _i in dir_init_list:
        if not os.path.exists(_i):
            os.mkdir(_i)

    for _i in list(jsonfile_init_list.keys()):
        if not os.path.exists(_i):
            open(_i, 'w+', encoding='UTF-8').write(jsonfile_init_list[_i])


if __name__ == "__main__":
    Initialization()
    app = QApplication()  # app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
