# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FantasyCricket.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox
import sqlite3
from Evaluate import Ui_Form
import style

class Ui_FantasyCricket(object):
    def setupUi(self, FantasyCricket):
        FantasyCricket.setObjectName("FantasyCricket")
        FantasyCricket.resize(801, 600)
        self.bat_team = 0
        self.bow_team = 0
        self.wk_team = 0
        self.ar_team = 0
        self.fetch = {"bat": [], "bow": [], "wk": [], "ar": []}
        self.match = None
        self.centralwidget = QtWidgets.QWidget(FantasyCricket)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lb_selection = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_selection.setFont(font)
        self.lb_selection.setObjectName("lb_selection")
        self.lb_selection.setStyleSheet(style.labelStyle)
        self.horizontalLayout_7.addWidget(self.lb_selection)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lb_bat = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_bat.setFont(font)
        self.lb_bat.setObjectName("lb_bat")
        self.lb_bat.setStyleSheet(style.labelStyle)
        self.horizontalLayout_6.addWidget(self.lb_bat)
        self.le_bat = QtWidgets.QLineEdit(self.centralwidget)
        self.le_bat.setObjectName("le_bat")
        self.le_bat.setPlaceholderText("0")
        self.le_bat.setStyleSheet("font: 20px")
        self.le_bat.setEnabled(False)
        self.le_bat.setStyleSheet(style.lineEditStyle)
        self.horizontalLayout_6.addWidget(self.le_bat)
        self.lb_bow = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_bow.setFont(font)
        self.lb_bow.setObjectName("lb_bow")
        self.lb_bow.setStyleSheet(style.labelStyle)
        self.horizontalLayout_6.addWidget(self.lb_bow)
        self.le_bow = QtWidgets.QLineEdit(self.centralwidget)
        self.le_bow.setObjectName("le_bow")
        self.le_bow.setPlaceholderText("0")
        self.le_bow.setStyleSheet("font: 20px")
        self.le_bow.setEnabled(False)
        self.le_bow.setStyleSheet(style.lineEditStyle)
        self.horizontalLayout_6.addWidget(self.le_bow)
        self.lb_ar = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ar.setFont(font)
        self.lb_ar.setStyleSheet(style.labelStyle)
        self.lb_ar.setObjectName("lb_ar")
        self.horizontalLayout_6.addWidget(self.lb_ar)
        self.le_ar = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ar.setObjectName("le_ar")
        self.le_ar.setPlaceholderText("0")
        self.le_ar.setStyleSheet("font: 20px")
        self.le_ar.setEnabled(False)
        self.le_ar.setStyleSheet(style.lineEditStyle)
        self.horizontalLayout_6.addWidget(self.le_ar)
        self.lb_wk = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_wk.setFont(font)
        self.lb_wk.setObjectName("lb_wk")
        self.lb_wk.setStyleSheet(style.labelStyle)
        self.horizontalLayout_6.addWidget(self.lb_wk)
        self.le_wk = QtWidgets.QLineEdit(self.centralwidget)
        self.le_wk.setObjectName("le_wk")
        self.le_wk.setPlaceholderText("0")
        self.le_wk.setStyleSheet(style.lineEditStyle)
        self.le_wk.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.le_wk)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_poav = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_poav.setFont(font)
        self.lb_poav.setObjectName("lb_poav")
        self.lb_poav.setStyleSheet(style.labelStyle)
        self.horizontalLayout_2.addWidget(self.lb_poav)
        self.le_poav = QtWidgets.QLineEdit(self.centralwidget)
        self.le_poav.setStyleSheet(style.lineEditStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_poav.sizePolicy().hasHeightForWidth())
        self.le_poav.setSizePolicy(sizePolicy)
        self.le_poav.setObjectName("le_poav")
        self.le_poav.setPlaceholderText("0")
        self.le_poav.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.le_poav)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lb_pous = QtWidgets.QLabel(self.centralwidget)
        self.lb_pous.setStyleSheet(style.labelStyle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_pous.sizePolicy().hasHeightForWidth())
        self.lb_pous.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_pous.setFont(font)
        self.lb_pous.setObjectName("lb_pous")
        self.horizontalLayout_2.addWidget(self.lb_pous)
        self.le_pous = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pous.setObjectName("le_pous")
        self.le_pous.setText("0")
        self.le_pous.setStyleSheet(style.lineEditStyle)
        self.le_pous.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.le_pous)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.rb_bat = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rb_bat.setFont(font)
        self.rb_bat.setObjectName("rb_bat")
        self.rb_bat.clicked.connect(self.bat)
        self.rb_bat.setStyleSheet(style.radioButtonStyle)
        self.rb_bat.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.rb_bat)
        self.rb_bow = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rb_bow.setFont(font)
        self.rb_bow.setObjectName("rb_bow")
        self.rb_bow.clicked.connect(self.bow)
        self.rb_bow.setEnabled(False)
        self.rb_bow.setStyleSheet(style.radioButtonStyle)
        
        self.horizontalLayout_5.addWidget(self.rb_bow)
        self.rb_ar = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rb_ar.setFont(font)
        self.rb_ar.setObjectName("rb_ar")
        self.rb_ar.clicked.connect(self.ar)
        self.rb_ar.setEnabled(False)
        self.rb_ar.setStyleSheet(style.radioButtonStyle)
        
        self.horizontalLayout_5.addWidget(self.rb_ar)
        self.rb_wk = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.rb_wk.setFont(font)
        self.rb_wk.setObjectName("rb_wk")
        self.rb_wk.clicked.connect(self.wk)
        self.rb_wk.setEnabled(False)
        self.rb_wk.setStyleSheet(style.radioButtonStyle)
        self.horizontalLayout_5.addWidget(self.rb_wk)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.lb_tename = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lb_tename.setFont(font)
        self.lb_tename.setObjectName("lb_tename")
        self.lb_tename.setStyleSheet(style.labelStyle)
        self.horizontalLayout_5.addWidget(self.lb_tename)
        self.le_tename = QtWidgets.QLineEdit(self.centralwidget)
        self.le_tename.setObjectName("le_tename")
        self.le_tename.setPlaceholderText("No team")
        self.le_tename.setStyleSheet(style.lineEditStyle)
        self.le_tename.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.le_tename)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lw_enter = QtWidgets.QListWidget(self.centralwidget)
        self.lw_enter.setObjectName("lw_enter")
        self.lw_enter.setStyleSheet(style.listWidgetStyle)
        self.horizontalLayout.addWidget(self.lw_enter)
        self.lw_enter.itemDoubleClicked.connect(self.enter_list)
        spacerItem2 = QtWidgets.QSpacerItem(110, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lw_add = QtWidgets.QListWidget(self.centralwidget)
        self.lw_add.setObjectName("lw_add")
        self.lw_add.setStyleSheet(style.listWidgetStyle)
        self.horizontalLayout.addWidget(self.lw_add)
        self.lw_add.itemDoubleClicked.connect(self.add_list)
        self.verticalLayout.addLayout(self.horizontalLayout)
        FantasyCricket.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FantasyCricket)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Team = QtWidgets.QMenu(self.menubar)
        self.menuManage_Team.setObjectName("menuManage_Team")
        FantasyCricket.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FantasyCricket)
        self.statusbar.setObjectName("statusbar")
        FantasyCricket.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(FantasyCricket)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(FantasyCricket)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionSave_Team = QtWidgets.QAction(FantasyCricket)
        self.actionSave_Team.setObjectName("actionSave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(FantasyCricket)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.menuManage_Team.addAction(self.actionNew_Team)
        self.menuManage_Team.addAction(self.actionOpen_Team)
        self.menuManage_Team.addAction(self.actionSave_Team)
        self.menuManage_Team.addAction(self.actionEvaluate_Team)
        self.menubar.addAction(self.menuManage_Team.menuAction())
        self.menuManage_Team.triggered[QtWidgets.QAction].connect(self.new_team_act)

        self.retranslateUi(FantasyCricket)
        QtCore.QMetaObject.connectSlotsByName(FantasyCricket)
        #FantasyCricket.setFixedSize(FantasyCricket.size())

    def retranslateUi(self, FantasyCricket):
        _translate = QtCore.QCoreApplication.translate
        FantasyCricket.setWindowTitle(_translate("FantasyCricket", "Fantasy Cricket"))
        self.lb_selection.setText(_translate("FantasyCricket", "Yours Selections"))
        self.lb_bat.setText(_translate("FantasyCricket", "Batsmen(BAT)"))
        self.lb_bow.setText(_translate("FantasyCricket", "Bowlers(BOW)"))
        self.lb_ar.setText(_translate("FantasyCricket", "Allrounder(AR)"))
        self.lb_wk.setText(_translate("FantasyCricket", "Wicket-keeper(WK)"))
        self.lb_poav.setText(_translate("FantasyCricket", "Points Available"))
        self.lb_pous.setText(_translate("FantasyCricket", "Points Used"))
        self.rb_bat.setText(_translate("FantasyCricket", "BAT"))
        self.rb_bow.setText(_translate("FantasyCricket", "BOW"))
        self.rb_ar.setText(_translate("FantasyCricket", "AR"))
        self.rb_wk.setText(_translate("FantasyCricket", "WK"))
        self.lb_tename.setText(_translate("FantasyCricket", "Team  Name"))
        self.menuManage_Team.setTitle(_translate("FantasyCricket", "Manage Team"))
        self.actionNew_Team.setText(_translate("FantasyCricket", "New Team"))
        self.actionOpen_Team.setText(_translate("FantasyCricket", "Open Team"))
        self.actionSave_Team.setText(_translate("FantasyCricket", "Save Team"))
        self.actionEvaluate_Team.setText(_translate("FantasyCricket", "Evaluate Team"))


    def new_team_act(self, action):
        tx = action.text()
        if tx == "New Team":
            text_team, okPressed_team = QInputDialog.getText(QtWidgets.QWidget(), "Team Name", "Enter your team name:")
            if text_team != "match1" and text_team != "match2" and text_team != "match3" and text_team != "match4" and text_team != "match5":
                text_team = text_team.title()
                cric = sqlite3.connect('cricket.db')
                cur_cric = cric.cursor()
                cur_cric.execute("select team_name from collection")
                reply = True
                while True:
                    record = cur_cric.fetchone()
                    if record == None:
                        break
                    elif record[0] == text_team:
                        QMessageBox.information(QtWidgets.QWidget(), 'Information', "This team name already exists")
                        reply = False
                        break
                cric.close()
                if reply:
                    if okPressed_team and text_team:
                        text_match, okPressed_match = QInputDialog.getText(QtWidgets.QWidget(), "Match Name", "Enter name of the match either match1|match2|match3|match3|match4|match5:")
                        if text_match == "match1" or text_match == "match2" or text_match == "match3" or text_match == "match4" or text_match == "match5":
                            if text_match and okPressed_match:
                                self.match = text_match
                                self.lw_add.clear()
                                self.renew()
                                self.rb_bat.setEnabled(True)
                                self.rb_bow.setEnabled(True)
                                self.rb_ar.setEnabled(True)
                                self.rb_wk.setEnabled(True)
                                self.le_tename.setText(text_team)
                                self.le_poav.setText("160")
                        else:
                            QMessageBox.information(QtWidgets.QWidget(), 'Information', "This match name does not exists")
            else:
                QMessageBox.information(QtWidgets.QWidget(), 'Information', "Do not enter match name")
        if tx == "Save Team":
            if (self.bat_team + self.bow_team + self.wk_team + self.ar_team) == 11:
                cric = sqlite3.connect('cricket.db')
                cur_cric = cric.cursor()
                cur_cric.execute("select team_name from collection")
                reply = True
                while True:
                    record = cur_cric.fetchone()
                    if record == None:
                        break
                    elif record[0] == self.le_tename.text():
                        QMessageBox.information(QtWidgets.QWidget(), 'Information', "This team name already exists")
                        reply = False
                        break
                if reply:
                    cur_cric.execute("""create table if not exists [{}](Player_id integer Primary key , Name text, value integer)""".format(self.le_tename.text()))
                    for value in self.enter_list.__closure__[0].cell_contents.values():
                        for content in value:
                            cur_cric.execute("insert into [{}](Player_id, Name, value) values(?, ?, ?)".format(self.le_tename.text()), (content[1], content[0], content[2]))
                    cric.commit()
                    cur_cric.execute("insert into collection values (?, ?)", (self.le_tename.text(), self.match))
                    cric.commit()
                    QMessageBox.information(QtWidgets.QWidget(), "Information", "your team is saved")
                cric.close()
            else:
                QMessageBox.information(QtWidgets.QWidget(), "Information", "Complete your team")

        if tx == "Evaluate Team":
            self.otherWindow = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.otherWindow)
            self.otherWindow.show()

        if tx == "Open Team":
            text, okPressed = QInputDialog.getText(QtWidgets.QWidget(), "Team Name", "Enter your team name:")
            if text and okPressed:
                team = sqlite3.connect("cricket.db")
                cur_team = team.cursor()
                cur_team.execute("select * from collection")
                running = True
                while running:
                    record = cur_team.fetchone()
                    if record == None:
                        running = False
                    elif record[0] == text:
                        self.otherWindow = QtWidgets.QWidget()
                        self.ui = Ui_Form()
                        self.ui.setupUi(self.otherWindow)
                        self.otherWindow.show()
                        index = self.ui.cb_team.findText(text, QtCore.Qt.MatchFixedString)
                        self.ui.cb_team.setCurrentIndex(index)
                        self.ui.team_change(text)
                        self.ui.calculate()
                        break
                else:
                    QMessageBox.information(QtWidgets.QWidget(), "Information", "your team do not exist")
                team.close()
            
    def renew(self):
        for key in self.fetch.keys():
            if self.fetch[key]:
                self.fetch[key].clear()

        for key in self.enter_list.__closure__[0].cell_contents.keys():
            if self.enter_list.__closure__[0].cell_contents[key]:
                self.enter_list.__closure__[0].cell_contents[key].clear()

        self.bat_team = 0
        self.bow_team = 0
        self.wk_team = 0
        self.ar_team = 0
        self.le_bat.setText("0")
        self.le_bow.setText("0")
        self.le_wk.setText("0")
        self.le_ar.setText("0")
        self.le_pous.setText("0")
        self.bat.__closure__[0].cell_contents.count = 0
        self.wk.__closure__[0].cell_contents.count = 0
        self.bow.__closure__[0].cell_contents.count = 0
        self.ar.__closure__[0].cell_contents.count = 0
        if self.rb_bat.isChecked() == True:
            self.bat()
        elif self.rb_bow.isChecked() == True:
            self.bow()
        elif self.rb_wk.isChecked() == True:
            self.wk()
        elif self.rb_ar.isChecked() == True:
            self.ar()
        

    def extra(func, record = []):
        def check(args):
            if check.count == 0:
                value = func(args)
                if record:
                    record[0].remaining = value
                    record[0] = func
                else:
                    record.append(func)
                check.count += 1
            else:
                value = args.remove()
                record[0].remaining = value
                record[0] = func
                args.lw_enter.addItems(func.remaining)
        check.count = 0
        func.remaining = []
        return check


    def remove(self):
        index = self.lw_enter.takeItem(0)
        result = []
        while index:
            result.append(index.text())
            index = self.lw_enter.takeItem(0)
        return result
    
    @extra
    def bat(self):
        if self.rb_bat.isChecked() == True:
            remaining = self.remove()
            cric = sqlite3.connect('cricket.db')
            cur_cric = cric.cursor()
            cur_cric.execute(f"select Name, Player_id, given_point from {self.match} where ctg = 'BT'")
            while True:
                record = cur_cric.fetchone()
                if record == None:
                    break
                self.fetch["bat"].append(record)
                self.lw_enter.addItem(f"{record[2]:02}     {record[0]}")
            cric.close()
            return remaining

    @extra
    def bow(self):
        if self.rb_bow.isChecked() == True:
            remaining = self.remove()
            cric = sqlite3.connect('cricket.db')
            cur_cric = cric.cursor()
            cur_cric.execute(f"select Name, Player_id, given_point from {self.match} where ctg = 'BW'")
            while True:
                record = cur_cric.fetchone()
                if record == None:
                    break
                self.fetch["bow"].append(record)
                self.lw_enter.addItem(f"{record[2]:02}     {record[0]}")
            cric.close()
            return remaining

    @extra
    def wk(self):
        if self.rb_wk.isChecked() == True:
            remaining = self.remove()
            cric = sqlite3.connect('cricket.db')
            cur_cric = cric.cursor()
            cur_cric.execute(f"select Name, Player_id, given_point from {self.match} where ctg = 'WK'")
            while True:
                record = cur_cric.fetchone()
                if record == None:
                    break
                self.fetch["wk"].append(record)
                self.lw_enter.addItem(f"{record[2]:02}     {record[0]}")
            cric.close()
            return remaining
            

    @extra
    def ar(self):
        if self.rb_ar.isChecked() == True:
            remaining = self.remove()
            cric = sqlite3.connect('cricket.db')
            cur_cric = cric.cursor()
            cur_cric.execute(f"select Name, Player_id, given_point from {self.match} where ctg = 'AR'")
            while True:
                record = cur_cric.fetchone()
                if record == None:
                    break
                self.lw_enter.addItem(f"{record[2]:02}     {record[0]}")
                self.fetch["ar"].append(record)
            cric.close()
            return remaining

    def remove1(func1):
        def check1(args, item):
            nonlocal flag, count
            if flag == 0 and func1.__name__ == "enter_list":
                count = {args.bat.__closure__[1].cell_contents: [], args.bow.__closure__[1].cell_contents: [], args.wk.__closure__[1].cell_contents: [], args.ar.__closure__[1].cell_contents: []}
                flag += 1
            if func1.__name__ == "enter_list":
                if (int(args.le_poav.text()) - int(item.text().split()[0])) >= 0:
                    if args.rb_bat.isChecked() == True:
                        if args.bat_team < 5:
                            content = " ".join(item.text().split()[1:])
                            value = args.fetch["bat"]
                            for i in value:
                                if content in i:
                                    temp = i
                                    break
                            count[args.bat.__closure__[1].cell_contents].append(temp)
                            func1(args, item)
                            args.bat_team += 1
                            args.le_bat.setText(str(args.bat_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) - temp[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) + temp[2]))
                        else:
                            QMessageBox.information(QtWidgets.QWidget(), "Information", "You can't select more than 5 batsman")
                    elif args.rb_bow.isChecked() == True:
                        if args.bow_team < 3:
                            value = args.fetch["bow"]
                            content = " ".join(item.text().split()[1:])
                            for i in value:
                                if content in i:
                                    temp = i
                                    break
                            count[args.bow.__closure__[1].cell_contents].append(temp)
                            func1(args, item)
                            args.bow_team += 1
                            args.le_bow.setText(str(args.bow_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) - temp[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) + temp[2]))
                        else:
                            QMessageBox.information(QtWidgets.QWidget(), "Information", "You can't select more than 3 bowler")
                    elif args.rb_wk.isChecked() == True:
                        if args.wk_team < 1:
                            value = args.fetch["wk"]
                            content = " ".join(item.text().split()[1:])
                            for i in value:
                                if content in i:
                                    temp = i
                                    break
                            count[args.wk.__closure__[1].cell_contents].append(temp)
                            func1(args, item)
                            args.wk_team += 1
                            args.le_wk.setText(str(args.wk_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) - temp[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) + temp[2]))
                        else:
                            QMessageBox.information(QtWidgets.QWidget(), "Information", "You can't select more than 1 Wicketkeeper")
                    elif args.rb_ar.isChecked() == True:
                        if args.ar_team < 2:
                            value = args.fetch["ar"]
                            content = " ".join(item.text().split()[1:])
                            for i in value:
                                if content in i:
                                    temp = i
                                    break
                            count[args.ar.__closure__[1].cell_contents].append(temp)
                            func1(args, item)
                            args.ar_team += 1
                            args.le_ar.setText(str(args.ar_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) - temp[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) + temp[2]))
                        else:
                            QMessageBox.information(QtWidgets.QWidget(), "Information", "You can't select more than 2 allrounder")
                else:
                    QMessageBox.information(QtWidgets.QWidget(), "Information", "You can't select more player, point will become less than equal to 0")
                    
            else:
                if args.rb_bat.isChecked() == True:
                    content = " ".join(item.text().split()[1:])
                    for i in args.enter_list.__closure__[0].cell_contents[args.bat.__closure__[1].cell_contents]:
                        if content in i:
                            args.enter_list.__closure__[0].cell_contents[args.bat.__closure__[1].cell_contents].remove(i)
                            func1(args, item)
                            args.bat_team -= 1
                            args.le_bat.setText(str(args.bat_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) + i[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) - i[2]))
                            break
                    else:
                        args.re_ch1(item)
                elif args.rb_bow.isChecked() == True:
                    content = " ".join(item.text().split()[1:])
                    for i in args.enter_list.__closure__[0].cell_contents[args.bow.__closure__[1].cell_contents]:
                        if content in i:
                            args.enter_list.__closure__[0].cell_contents[args.bow.__closure__[1].cell_contents].remove(i)
                            func1(args, item)
                            args.bow_team -= 1
                            args.le_bow.setText(str(args.bow_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) + i[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) - i[2]))
                            break
                    else:
                        args.re_ch1(item)
                elif args.rb_wk.isChecked() == True:
                    content = " ".join(item.text().split()[1:])
                    for i in args.enter_list.__closure__[0].cell_contents[args.wk.__closure__[1].cell_contents]:
                        if content in i:
                            args.enter_list.__closure__[0].cell_contents[args.wk.__closure__[1].cell_contents].remove(i)
                            func1(args, item)
                            args.wk_team -= 1
                            args.le_wk.setText(str(args.wk_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) + i[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) - i[2]))
                            break
                    else:
                        args.re_ch1(item)
                elif args.rb_ar.isChecked() == True:
                    content = " ".join(item.text().split()[1:])
                    for i in args.enter_list.__closure__[0].cell_contents[args.ar.__closure__[1].cell_contents]:
                        if content in i:
                            args.enter_list.__closure__[0].cell_contents[args.ar.__closure__[1].cell_contents].remove(i)
                            func1(args, item)
                            args.ar_team -= 1
                            args.le_ar.setText(str(args.ar_team))
                            args.le_poav.setText(str(int(args.le_poav.text()) + i[2]))
                            args.le_pous.setText(str(int(args.le_pous.text()) - i[2]))
                            break
                    else:
                        args.re_ch1(item)
        count = {}
        flag = 0
        return check1
    
    @remove1
    def enter_list(self, item):
        self.lw_enter.takeItem(self.lw_enter.row(item))
        self.lw_add.addItem(item.text())

    @remove1
    def add_list(self, item):
        self.lw_add.takeItem(self.lw_add.row(item))
        self.lw_enter.addItem(item.text())

    def re_ch1(args, item):
        content = " ".join(item.text().split()[1:])
        for key, value in args.enter_list.__closure__[0].cell_contents.items():
            c = False
            for i in value:
                if content in i:
                    temp = i
                    c = True
                    key.remaining.append(item.text())
                    args.enter_list.__closure__[0].cell_contents[key].remove(temp)
                    args.lw_add.takeItem(args.lw_add.row(item))
                    args.le_poav.setText(str(int(args.le_poav.text()) + i[2]))
                    args.le_pous.setText(str(int(args.le_pous.text()) - i[2]))
                    if key == args.bat.__closure__[1].cell_contents:
                        args.bat_team -= 1
                        args.le_bat.setText(str(args.bat_team))
                    elif key == args.bow.__closure__[1].cell_contents:
                        args.bow_team -= 1
                        args.le_bow.setText(str(args.bow_team))
                    elif key == args.wk.__closure__[1].cell_contents:
                        args.wk_team -= 1
                        args.le_wk.setText(str(args.wk_team))
                    elif key == args.ar.__closure__[1].cell_contents:
                        args.ar_team -= 1
                        args.le_ar.setText(str(args.ar_team))
                    break
            if c:
                break

            
                
            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FantasyCricket = QtWidgets.QMainWindow()
    FantasyCricket.setStyleSheet("QMainWindow{background-color:brown;}")
    ui = Ui_FantasyCricket()
    ui.setupUi(FantasyCricket)
    FantasyCricket.show()
    sys.exit(app.exec_())

