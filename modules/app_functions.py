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

# MAIN FILE
# ///////////////////////////////////////////////////////////////
import os
from glob import glob
from json import load, dump

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox, QFileDialog

import gachaAPI
import mysapi
from MAIN import *
# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
from MAIN import MainWindow
#from modules import Settings


def _reset_charts(window):
    _aubot_blank = """<html><body style=" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;background-color: rgb(40, 44, 52);"></body></html>"""
    window.ui.Chart_1.setHtml(_aubot_blank)
    window.ui.Chart_2.setHtml(_aubot_blank)
    window.ui.Chart_3.setHtml(_aubot_blank)
    window.ui.ChartsText_label_1.setText('')
    window.ui.ChartsText_label_2.setText('')
    window.ui.ChartsText_label_3.setText('')

class AppFunctions(MainWindow):

    def Cookies_Pageload(self):
        _d = gachaAPI.DatabaseManager('Cookies').DATA
        _current_list = []
        for i in range(self.ui.CK_Table.rowCount()):
            if self.ui.CK_Table.item(i, 0):
                _current_list.append(self.ui.CK_Table.item(i, 0).text())
        for _user in list(_d.keys()):
            if _user not in _current_list and _d[_user]!='':
                _mys = mysapi.mys(_d[_user])
                try:
                    mysapi.Cookie.checkCookie(_d[_user])
                    _server = _mys.getUserGameRoles().json()['data']['list'][0]["region_name"]
                    self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 0, QTableWidgetItem(_user))
                    self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 1, QTableWidgetItem(_server))
                    self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 2, QTableWidgetItem('可用'))
                    self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 3,
                                             QTableWidgetItem(mysapi.Cookie.dict_to_str(_d[_user])))
                    self.ui.CK_Table.setRowCount(self.ui.CK_Table.rowCount() + 1)
                except:
                    continue

    def Cookies_import_TextEditor(self):
        _text = self.ui.CK_Input_textedit.text()

        _current_list = []
        for i in range(self.ui.CK_Table.rowCount()):
            if self.ui.CK_Table.item(i, 0):
                _current_list.append(self.ui.CK_Table.item(i, 0).text())

        _cookie = mysapi.Cookie.fatchCookie(_text)
        try:
            mysapi.Cookie.checkCookie(_cookie)
        except:
            QMessageBox.warning(self, 'Cookies Error', 'Cookies无效,请重新登录！')
            return
        _mys = mysapi.mys(_cookie)
        _uid = _mys.UID_MYS
        _server = _mys.getUserGameRoles().json()['data']['list'][0]["region_name"]

        if _uid not in _current_list:
            gachaAPI.DatabaseManager('Cookies').set_NodeData(_uid, _cookie)
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 0, QTableWidgetItem(_uid))
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 1, QTableWidgetItem(_server))
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 2, QTableWidgetItem('可用'))
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 3,
                                     QTableWidgetItem(mysapi.Cookie.dict_to_str(_cookie)))
            self.ui.CK_Table.setRowCount(self.ui.CK_Table.rowCount() + 1)
            QMessageBox.information(self, 'Cookies Information', 'Cookies已导入')
        else:
            QMessageBox.information(self, 'Cookies Information', 'Cookies已存在')

    def Cookies_import_btn(self):
        QMessageBox.information(self, 'Cookies Information', '从文件导入尚不可用')

    def Cookies_save(self):
        QMessageBox.information(self, 'Cookies Information', '导出功能尚不可用，链接已保存')

    def Cookies_delete(self):
        _delrow_list = []
        if not self.ui.CK_Table.selectedItems(): return
        for _i in self.ui.CK_Table.selectedItems():
            if _i:
                _delrow_list.append(_i.row())
        _b = QMessageBox.warning(self, 'Cookies Warning !', f'此操作将会删除所选UID的本地Cookies！！！请确认！！！3',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        _b = QMessageBox.warning(self, 'Cookies Warning !', f'此操作将会删除所选UID的本地Cookies！！！请确认！！！2',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        _b = QMessageBox.warning(self, 'Cookies Warning !', f'此操作将会删除所选UID的本地Cookies！！！请确认！！！1',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        for _l in _delrow_list:
            gachaAPI.DatabaseManager('Cookies').set_NodeData(self.ui.CK_Table.item(_l, 0).text(), '')
            self.ui.CK_Table.removeRow(_l)

    def Cookies_copy(self):

        if not self.ui.CK_Table.selectedItems(): return
        for _i in self.ui.CK_Table.selectedItems():
            if _i:
                gachaAPI.Tool.set_clipboard(_i.text())
        QMessageBox.information(self, 'Copy to clipboard', '已复制选择Cookies到剪贴板')

    def Cookies_check(self):
        _current_list = []
        _d = gachaAPI.DatabaseManager('Cookies').DATA

        for i in range(self.ui.CK_Table.rowCount() - 1):
            _cookie =_d[self.ui.CK_Table.item(i, 0).text()]
            try:
                mysapi.Cookie.checkCookie(_cookie)
                self.ui.CK_Table.setItem(i, 2, QTableWidgetItem('可用'))
            except Exception as e:
                raise e
                self.ui.CK_Table.setItem(i, 2, QTableWidgetItem('不可用'))
        QMessageBox.information(self, '已检查Cookies有效性！', '已检查Cookies有效性！')

    def Cookies_search(self):
        _cookie = mysapi.Cookie().get_cookie_from_chrome()
        try:
            mysapi.Cookie.checkCookie(_cookie)
        except:
            QMessageBox.warning(self, 'Cookies Error', 'Cookies无效,请重新登录！')
            return
        _current_list = []
        for i in range(self.ui.CK_Table.rowCount()):
            if self.ui.CK_Table.item(i, 0):
                _current_list.append(self.ui.CK_Table.item(i, 0).text())
        _mys = mysapi.mys(_cookie)
        _uid = _mys.UID_MYS
        _server = _mys.getUserGameRoles().json()['data']['list'][0]["region_name"]
        if _uid not in _current_list:
            gachaAPI.DatabaseManager('Cookies').set_NodeData(_uid, _cookie)
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 0, QTableWidgetItem(_uid))
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 1, QTableWidgetItem(_server))
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 2, QTableWidgetItem('可用'))
            self.ui.CK_Table.setItem(self.ui.CK_Table.rowCount() - 1, 3,
                                     QTableWidgetItem(mysapi.Cookie.dict_to_str(_cookie)))
            self.ui.CK_Table.setRowCount(self.ui.CK_Table.rowCount() + 1)
            QMessageBox.information(self, 'Cookies Information ！', f'检索到共{self.ui.CK_Table.rowCount() - 1}个Cookies！')

    def Links_import_btn(self):
        _p = QFileDialog.getOpenFileName(self, '选择链接文件')[0]
        _url_class = gachaAPI._URL()
        #print(_p)
        if not os.path.exists(_p):
            return
        _current_list = []
        for i in range(self.ui.Links_Table.rowCount()):
            if self.ui.Links_Table.item(i, 0):
                _current_list.append(self.ui.Links_Table.item(i, 0).text())

        try:
            _text = open(_p, 'rb').read()
        except FileNotFoundError:
            return
        _start = _text.rfind(_url_class.HOST_CN.encode(encoding='UTF-8'))
        _end = _text.rfind('&game_biz=hk4e_cn'.encode(encoding='UTF-8')) + len('&game_biz=hk4e_cn')
        _url = _text[_start:_end].decode(encoding='UTF-8')
        _uid = _url_class.checkURL(_url)
        if _uid == 0:
            QMessageBox.warning(self, 'Links Error', '链接无效！')
        else:
            if _uid not in _current_list:
                _url_class.DBM.set_NodeData(_uid, _url)
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 0, QTableWidgetItem(_uid))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 1,
                                            QTableWidgetItem(_url_class.getServer(_url)))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 2, QTableWidgetItem('可用'))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 3, QTableWidgetItem(_url))
                self.ui.Links_Table.setRowCount(self.ui.Links_Table.rowCount() + 1)
                QMessageBox.information(self, 'URL Information', '链接已导入')
            else:
                QMessageBox.information(self, 'URL Exists', '链接已存在')

    def Links_import_TextEditor(self):
        _text = self.ui.URL_Input_textedit.text()
        _url_class = gachaAPI._URL()
        _current_list = []
        for i in range(self.ui.Links_Table.rowCount()):
            if self.ui.Links_Table.item(i, 0):
                _current_list.append(self.ui.Links_Table.item(i, 0).text())

        if _url_class.HOST_CN not in _text and _url_class.HOST_OS not in _text:
            if not os.path.exists(_text):
                return
            try:
                _text = open(_text, 'rb').read()
            except FileNotFoundError:
                return
            _start = _text.rfind(_url_class.HOST_CN.encode(encoding='UTF-8'))
            _end = _text.rfind('&game_biz=hk4e_cn'.encode(encoding='UTF-8')) + len('&game_biz=hk4e_cn')
            _url = _text[_start:_end].decode(encoding='UTF-8')
        else:
            _start = _text.rfind(_url_class.HOST_CN)
            _end = _text.rfind('&game_biz=hk4e_cn') + len('&game_biz=hk4e_cn')
            _url = _text[_start:_end]

        _uid = _url_class.checkURL(_url)
        if _uid == 0:
            QMessageBox.warning(self, 'Links Error', '链接无效！')
        else:
            if _uid not in _current_list:
                _url_class.DBM.set_NodeData(_uid, _url)
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 0, QTableWidgetItem(_uid))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 1,
                                            QTableWidgetItem(_url_class.getServer(_url)))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 2, QTableWidgetItem('可用'))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 3, QTableWidgetItem(_url))
                self.ui.Links_Table.setRowCount(self.ui.Links_Table.rowCount() + 1)
                QMessageBox.information(self, 'URL Information', '链接已导入')
            else:
                QMessageBox.information(self, 'URL Exists', '链接已存在')

    def Links_pageLoad(self):
        _url_class = gachaAPI._URL()
        _d = _url_class.DBM.DATA
        _current_list = []
        for i in range(self.ui.Links_Table.rowCount()):
            if self.ui.Links_Table.item(i, 0):
                _current_list.append(self.ui.Links_Table.item(i, 0).text())
        for _user in list(_d.keys()):
            if _user not in _current_list and _d[_user] !='':
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 0, QTableWidgetItem(_user))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 1,
                                            QTableWidgetItem(_url_class.getServer(_d[_user])))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 2, QTableWidgetItem(''))
                self.ui.Links_Table.setItem(self.ui.Links_Table.rowCount() - 1, 3, QTableWidgetItem(_d[_user]))
                self.ui.Links_Table.setRowCount(self.ui.Links_Table.rowCount() + 1)
        for i in range(self.ui.Links_Table.rowCount() - 1):
            _u = self.ui.Links_Table.item(i, 3).text()
            _url_class = gachaAPI._URL()
            if _url_class.checkURL(_u) != 0:
                self.ui.Links_Table.setItem(i, 2, QTableWidgetItem('可用'))
            else:
                self.ui.Links_Table.setItem(i, 2, QTableWidgetItem('不可用'))

    def Links_save(self):
        QMessageBox.information(self, 'Links Information', '导出功能尚不可用，链接已保存')

    def Links_copy(self):
        if not self.ui.Links_Table.selectedItems(): return
        for _i in self.ui.Links_Table.selectedItems():
            if _i:
                gachaAPI.Tool.set_clipboard(_i.text())
        QMessageBox.information(self, 'Copy to clipboard', '已复制选择链接到剪贴板')

    def Links_check(self):
        for i in range(self.ui.Links_Table.rowCount()):
            _u = self.ui.Links_Table.item(i, 3)
            if _u:
                _u = _u.text()
            else:
                break
            _url_class = gachaAPI._URL()
            if _url_class.checkURL(_u) != 0:
                self.ui.Links_Table.setItem(i, 2, QTableWidgetItem('可用'))
            else:
                self.ui.Links_Table.setItem(i, 2, QTableWidgetItem('不可用'))
        QMessageBox.information(self, '已检查链接有效性！', '已检查链接有效性！')

    def Links_delete(self):
        _delrow_list = []
        if not self.ui.Links_Table.selectedItems(): return
        for _i in self.ui.Links_Table.selectedItems():
            if _i:
                _delrow_list.append(_i.row())
        _b = QMessageBox.warning(self, 'Links Warning !', f'此操作将会删除所选UID的本地URL！！！请确认！！！3',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        _b = QMessageBox.warning(self, 'Links Warning !', f'此操作将会删除所选UID的本地URL！！！请确认！！！2',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        _b = QMessageBox.warning(self, 'Links Warning !', f'此操作将会删除所选UID的本地URL！！！请确认！！！1',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        for _l in _delrow_list:
            _url_class = gachaAPI._URL()
            _url_class.DBM.set_NodeData(self.ui.Links_Table.item(_l, 0).text(), '')
            self.ui.Links_Table.removeRow(_l)

    def Links_search(self):
        GAME_PATH = load(open('./DATA/GamePath.json', 'r', encoding='UTF-8'))
        _url_class = gachaAPI._URL()

        if self.ui.ServersChoose_Combox.currentText() == 'CN':
            if not GAME_PATH["CN"] or not os.path.exists(os.path.join(GAME_PATH["CN"], 'YuanShen.exe')):
                _p = QFileDialog.getExistingDirectory(self, '选择原神安装目录')
                if not _p:
                    return
                if not os.path.exists(os.path.join(_p, 'YuanShen.exe')):
                    QMessageBox.warning(self, 'Path Error !', '游戏路径错误')
                    return
                GAME_PATH["CN"] = _p
                dump(GAME_PATH, open('./DATA/GamePath.json', 'w+', encoding='UTF-8'))
                #_url_class = gachaAPI._URL()
                #return
            _U = _url_class.scanURL(GAME_PATH["CN"])
        elif self.ui.ServersChoose_Combox.currentText() == 'OS':
            if not GAME_PATH["OS"] or not os.path.exists(os.path.join(GAME_PATH["OS"], 'GenshinImpact.exe')):
                _p = QFileDialog.getExistingDirectory(self, '选择原神安装目录')
                if not _p: return
                if not os.path.exists(os.path.join(_p, 'GenshinImpact.exe')):
                    QMessageBox.warning(self, 'Path Error !', '游戏路径错误')
                    return
                GAME_PATH["OS"] = _p
                dump(GAME_PATH, open('./DATA/GamePath.json', 'w+', encoding='UTF-8'))
                #_url_class = gachaAPI._URL()
                #return
            _U = _url_class.scanURL(GAME_PATH["OS"])
        else:
            QMessageBox.warning(self, 'Error !', '请先选择服务器')
            return

        if _U == {}:
            QMessageBox.warning(self, 'Links Error !', '未检索到有效的链接')
            return
        _current_list = {}

        for i in range(self.ui.Links_Table.rowCount()):
            if self.ui.Links_Table.item(i, 0):
                _current_list[self.ui.Links_Table.item(i, 0).text()]=self.ui.Links_Table.item(i, 2).text()
        for _user in list(_U.keys()):
            _url_class.DBM.set_NodeData(_user, _U[_user])
            if _user not in list(_current_list.keys()):
                _index=self.ui.Links_Table.rowCount() - 1
                self.ui.Links_Table.setItem(_index, 0, QTableWidgetItem(_user))
                self.ui.Links_Table.setItem(_index, 1,QTableWidgetItem(self.ui.ServersChoose_Combox.currentText()))
                self.ui.Links_Table.setItem(_index, 2, QTableWidgetItem('可用'))
                self.ui.Links_Table.setItem(_index, 3, QTableWidgetItem(_U[_user]))
                self.ui.Links_Table.setRowCount(self.ui.Links_Table.rowCount() + 1)
            elif _current_list[_user]=='不可用':
                _index=list(_current_list.keys()).index(_user)
                self.ui.Links_Table.setItem(_index, 0, QTableWidgetItem(_user))
                self.ui.Links_Table.setItem(_index, 1,QTableWidgetItem(self.ui.ServersChoose_Combox.currentText()))
                self.ui.Links_Table.setItem(_index, 2, QTableWidgetItem('可用'))
                self.ui.Links_Table.setItem(_index, 3, QTableWidgetItem(_U[_user]))
        QMessageBox.information(self, 'Links Information', f'检索到共{self.ui.Links_Table.rowCount() - 1}条链接！')

    def Chart_pageLoad(self):
        _current_list = []
        _UD = gachaAPI.DatabaseManager('UserData').DATA
        _URL=gachaAPI.DatabaseManager('URL').DATA
        for i in range(self.ui.ChartsChoose_Combox.count()):
            _current_list.append(self.ui.ChartsChoose_Combox.itemText(i))
        for i in list(_URL.keys()):
            if gachaAPI._URL.checkURL(_URL[i])!=0 and i not in _current_list:
                self.ui.ChartsChoose_Combox.addItem(i)
                _current_list.append(i)
        for i in list(_UD.keys()):
            if i not in _current_list:
                if _UD[i] != {} and _UD[i] != {"char": [], "wap": [], "permanent": [], "novice": []}:
                    self.ui.ChartsChoose_Combox.addItem(i)
        # print(_uid_list)

    def Chart_draw(self):
        if self.ui.ChartsChoose_Combox.currentText() not in list(
                load(open('./DATA/UserData.json', 'r', encoding='UTF-8')).keys()):
            QMessageBox.warning(self, 'Charts Warning', f'{self.ui.ChartsChoose_Combox.currentText()}无数据！')
            return
        if load(open('./DATA/UserData.json', 'r', encoding='UTF-8'))[self.ui.ChartsChoose_Combox.currentText()] == {
            "char": [], "wap": [], "permanent": [], "novice": []}:
            QMessageBox.warning(self, 'Charts Warning', f'{self.ui.ChartsChoose_Combox.currentText()}无数据！')
            return
        _UD = gachaAPI.UserData(self.ui.ChartsChoose_Combox.currentText())
        _echarts = gachaAPI.echarts(_UD)

        _echarts.draw_charts()

        if os.path.exists(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c1.html')):
            self.ui.ChartsText_label_1.setText(_echarts._make_detail(_echarts._pre_process(_UD.char))[2])
            self.ui.Chart_1.load(QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c1.html')))
        if os.path.exists(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c2.html')):
            self.ui.ChartsText_label_2.setText(_echarts._make_detail(_echarts._pre_process(_UD.wap))[2])
            self.ui.Chart_2.load(QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c2.html')))
        if os.path.exists(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c3.html')):
            self.ui.ChartsText_label_3.setText(_echarts._make_detail(_echarts._pre_process(_UD.permanent))[2])
            self.ui.Chart_3.load(QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c3.html')))

        # print('finished')

    def Chart_copy(self):
        QMessageBox.warning(self, '别急', '复制图片功能还没做，别急')

    def Chart_save(self):
        QMessageBox.warning(self, '别急', '你的数据已经自动保存过了，这是图片保存功能，还没做')

    def Chart_delete(self):
        if self.ui.ChartsChoose_Combox.currentText() == '':
            QMessageBox.warning(self, 'Delete Error !', '选择一个要删除的UID')
            return
        _b = QMessageBox.warning(self, 'Delete Warning !', '此操作将会删除所选UID的本地数据！！！请确认！！！3',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        _b = QMessageBox.warning(self, 'Delete Warning !', '此操作将会删除所选UID的本地数据！！！请确认！！！2',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return
        _b = QMessageBox.warning(self, 'Delete Warning !', '此操作将会删除所选UID的本地数据！！！请确认！！！1',
                                 QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
        if _b == QMessageBox.StandardButton.No:
            return

        _UDBM=gachaAPI.UserData(self.ui.ChartsChoose_Combox.currentText())
        _gachaAPI = gachaAPI.GachaData(_UDBM)
        _gachaAPI.UDBM.DBM_UD.set_NodeData(_gachaAPI.UDBM.USER_ID, {'char': [], 'wap': [], 'permanent': [], 'novice': []})
        #_gachaAPI.UDBM.DBM_URL.set_NodeData(_gachaAPI.USER_ID, '')
        for _f in glob(f'./DATA/charts/{_gachaAPI.UDBM.USER_ID}_c*.html'):
            os.remove(_f)
        _reset_charts(self)
        self.ui.ChartsChoose_Combox.removeItem(self.ui.ChartsChoose_Combox.currentIndex())

    def Chart_import(self):
        _current_list = []
        for i in range(self.ui.ChartsChoose_Combox.count()):
            _current_list.append(self.ui.ChartsChoose_Combox.itemText(i))

        _UD = eval(open(QFileDialog.getOpenFileName(self, '选择数据文件')[0], 'r', encoding='UTF-8').read())

        if 'info' not in list(_UD.keys()):

            if _UD == []:
                QMessageBox.warning(self, 'Import Error !', '文件为空')
                return

            _gachaAPI = gachaAPI.GachaData(gachaAPI.UserData(_UD[0]['uid']))

        else:
            if _UD == []or _UD['info']=={}:
                QMessageBox.warning(self, 'Import Error !', '文件为空')
                return

            _gachaAPI = gachaAPI.GachaData(gachaAPI.UserData(_UD['info']['uid']))
            _UD=_UD['list']
            for _i  in range (len(_UD)):
                _UD[_i]['uid']=str(_gachaAPI.UDBM.USER_ID)
                _UD[_i]['id']=int(_UD[_i]['id'])
                _UD[_i]["item_id"]= ""
                _UD[_i]["count"]= "1"
                _UD[_i]["lang"]= "zh-cn"
                del _UD[_i]['uigf_gacha_type']
                #print(_UD[_i])
                #break
        _gachaAPI.UserData_import(_UD)
        if _gachaAPI.UDBM.USER_ID not in _current_list:
            self.ui.ChartsChoose_Combox.addItem(_gachaAPI.UDBM.USER_ID)
            self.ui.ChartsChoose_Combox.setCurrentIndex(self.ui.ChartsChoose_Combox.findText(_gachaAPI.UDBM.USER_ID))

        _echarts = gachaAPI.echarts(_gachaAPI.UDBM)
        _echarts.draw_charts()

        if os.path.exists(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c1.html')):
            self.ui.ChartsText_label_1.setText(_echarts._make_detail(_echarts._pre_process(_gachaAPI.UDBM.char))[2])
            self.ui.Chart_1.load(QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c1.html')))
        if os.path.exists(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c2.html')):
            self.ui.ChartsText_label_2.setText(_echarts._make_detail(_echarts._pre_process(_gachaAPI.UDBM.wap))[2])
            self.ui.Chart_2.load(QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c2.html')))
        if os.path.exists(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c3.html')):
            self.ui.ChartsText_label_3.setText(_echarts._make_detail(_echarts._pre_process(_gachaAPI.UDBM.permanent))[2])
            self.ui.Chart_3.load(QUrl.fromLocalFile(
                os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c3.html')))

    def Chart_renew(self):
        # print(threading.current_thread())
        if self.ui.ChartsChoose_Combox.currentText() == '':
            # print('test')
            _reset_charts(self)
            return
        else:
            _current_list = []
            for i in range(self.ui.ChartsChoose_Combox.count()):
                _current_list.append(self.ui.ChartsChoose_Combox.itemText(i))

            if self.ui.ChartsChoose_Combox.currentText() not in _current_list:
                QMessageBox.warning(self, 'Charts Warning', f'{self.ui.ChartsChoose_Combox.currentText()}无链接！')
                return
            _UDBM=gachaAPI.UserData(self.ui.ChartsChoose_Combox.currentText())
            _gachaAPI = gachaAPI.GachaData(_UDBM)
            _gachaAPI.Main_DataGetter()

            while True:
                #print(_gachaAPI.THREAD_FLAG)
                if _gachaAPI.THREAD_FLAG==0:
                    #print('end')
                    self.ui.progressBar.setValue(4 - _gachaAPI.THREAD_FLAG)
                    break
                else:
                    #print(_gachaAPI.THREAD_FLAG)
                    #pass
                    self.ui.progressBar.setValue(4 - _gachaAPI.THREAD_FLAG)
            _gachaAPI.UDBM.DBM_UD.set_NodeData(_gachaAPI.UDBM.USER_ID,
                                          {'char': _gachaAPI.UDBM.char, 'wap': _gachaAPI.UDBM.wap,
                                           'permanent': _gachaAPI.UDBM.permanent,
                                           'novice': _gachaAPI.UDBM.novice})

            _echarts = gachaAPI.echarts(_gachaAPI.UDBM)
            _echarts.draw_charts()

            if os.path.exists(
                    os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c1.html')):
                self.ui.ChartsText_label_1.setText(_echarts._make_detail(_echarts._pre_process(_UDBM.char))[2])
                self.ui.Chart_1.load(QUrl.fromLocalFile(
                    os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c1.html')))
            if os.path.exists(
                    os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c2.html')):
                self.ui.ChartsText_label_2.setText(_echarts._make_detail(_echarts._pre_process(_UDBM.wap))[2])
                self.ui.Chart_2.load(QUrl.fromLocalFile(
                    os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c2.html')))
            if os.path.exists(
                    os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c3.html')):
                self.ui.ChartsText_label_3.setText(_echarts._make_detail(_echarts._pre_process(_UDBM.permanent))[2])
                self.ui.Chart_3.load(QUrl.fromLocalFile(
                    os.path.join(os.getcwd(), f'DATA/charts/{self.ui.ChartsChoose_Combox.currentText()}_c3.html')))

            # self.ui.Charts_frame.repaint()

    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")
