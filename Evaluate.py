# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import style

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(820, 596)
        Form.setStyleSheet(".QWidget{background-color:brown;}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(178, 46, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lb_up = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Lemon")
        font.setPointSize(14)
        self.lb_up.setFont(font)
        self.lb_up.setStyleSheet(style.labelStyle)
        self.lb_up.setObjectName("lb_up")
        self.horizontalLayout.addWidget(self.lb_up)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.cb_team = QtWidgets.QComboBox(Form)
        self.cb_team.setObjectName("cb_team")
        #self.cb_team.setStyleSheet(style.comboBoxStyle)
        self.horizontalLayout_2.addWidget(self.cb_team)
        self.cb_team.activated[str].connect(self.team_change)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cb_match = QtWidgets.QComboBox(Form)
        self.cb_match.setObjectName("cb_match")
        self.horizontalLayout_2.addWidget(self.cb_match)
        self.cb_match.activated[str].connect(self.match_change)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.lb_player = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Kalam")
        font.setPointSize(16)
        self.lb_player.setFont(font)
        self.lb_player.setObjectName("lb_player")
        self.lb_player.setStyleSheet(style.labelStyle)
        self.horizontalLayout_3.addWidget(self.lb_player)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.lb_point = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Kalam")
        font.setPointSize(16)
        self.lb_point.setFont(font)
        self.lb_point.setObjectName("lb_point")
        self.lb_point.setStyleSheet(style.labelStyle)
        self.horizontalLayout_3.addWidget(self.lb_point)
        self.le_point = QtWidgets.QLineEdit(Form)
        self.le_point.setObjectName("le_point")
        self.le_point.setEnabled(False)
        self.le_point.setStyleSheet(style.lineEditStyle)
        self.horizontalLayout_3.addWidget(self.le_point)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.lw_player = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_player.sizePolicy().hasHeightForWidth())
        self.lw_player.setSizePolicy(sizePolicy)
        self.lw_player.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.lw_player.setObjectName("lw_player")
        self.lw_player.setStyleSheet(style.listWidgetStyle)
        self.horizontalLayout_4.addWidget(self.lw_player)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.lw_point = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_point.sizePolicy().hasHeightForWidth())
        self.lw_point.setSizePolicy(sizePolicy)
        self.lw_point.setObjectName("lw_point")
        self.lw_point.setStyleSheet(style.listWidgetStyle)
        self.horizontalLayout_4.addWidget(self.lw_point)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.pb_cal = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.pb_cal.setFont(font)
        self.pb_cal.setObjectName("pb_cal")
        self.pb_cal.setStyleSheet(style.pushButtonStyle)
        self.horizontalLayout_5.addWidget(self.pb_cal)
        self.pb_cal.clicked.connect(self.calculate)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.pb_win = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pb_win.setFont(font)
        self.pb_win.setObjectName("pb_win")
        self.pb_win.setStyleSheet(style.pushButtonStyle)
        self.pb_win.clicked.connect(self.winner)
        self.horizontalLayout_5.addWidget(self.pb_win)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.add_team()
        self.add_match()
        self.previous = "select match"
        #Form.setFixedSize(Form.size())
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Evaluate"))
        self.lb_up.setText(_translate("Form", "Evaluate the Performance of Your Fantasy Team"))
        self.lb_player.setText(_translate("Form", "Players"))
        self.lb_point.setText(_translate("Form", "Points"))
        self.lw_player.setSortingEnabled(False)
        self.pb_cal.setText(_translate("Form", "Calculate"))
        self.pb_win.setText(_translate("Form", "Show Winner"))

    def add_team(self):
        team = sqlite3.connect('cricket.db')
        cur_team = team.cursor()
        cur_team.execute('select team_name from collection')
        self.cb_team.addItem("select team")
        rec = cur_team.fetchall()
        sor_rec = [value[0] for value in rec]
        sor_rec.sort()
        self.cb_team.addItems(sor_rec)
        team.close()

    def add_match(self):
        self.cb_match.addItem('select match')
        self.cb_match.addItem('match1')
        self.cb_match.addItem('match2')
        self.cb_match.addItem('match3')
        self.cb_match.addItem('match4')
        self.cb_match.addItem('match5')

    def team_change(self, text):
        team = sqlite3.connect("cricket.db")
        cur_team = team.cursor()
        cur_team.execute("select * from collection")
        while True:
            record = cur_team.fetchone()
            if record == None:
                break
            if record[0] == self.cb_team.currentText():
                index = self.cb_match.findText(record[1], QtCore.Qt.MatchFixedString)
                self.cb_match.setCurrentIndex(index)
        self.previous = self.cb_match.currentText()
        team.close()
        
    def match_change(self, text):
        if self.cb_team.currentText() != "select team":
            team = sqlite3.connect("cricket.db")
            cur_team = team.cursor()
            cur_team.execute("select * from collection")
            while True:
                record = cur_team.fetchone()
                if record == None:
                    break
                if record[0] == self.cb_team.currentText():
                    if text != record[1]:
                        QMessageBox.information(QtWidgets.QWidget(), "Information", "This team does not belong to this match")
                        QMessageBox.information(QtWidgets.QWidget(), "Information", "Restorring previous match name")
                        index = self.cb_match.findText(self.previous, QtCore.Qt.MatchFixedString)
                        self.cb_match.setCurrentIndex(index)
            team.close()

    def calculate(self):
        if self.cb_team.currentText() != "select team" and self.cb_match.currentText() != "select match":
            self.lw_player.clear()
            self.lw_point.clear()
            point = 0
            team = sqlite3.connect("cricket.db")
            match = sqlite3.connect("cricket.db")

            cur_team = team.cursor()
            cur_match = match.cursor()

            cur_team.execute(f"select Player_id, Name from [{self.cb_team.currentText()}]")
            while True:
                record_team = cur_team.fetchone()
                if record_team == None:
                    break
                cur_match.execute(f"select point from {self.cb_match.currentText()} where Player_id = {record_team[0]}")
                record_match = cur_match.fetchone()
                self.lw_player.addItem(record_team[1])
                self.lw_point.addItem(str(record_match[0]))
                point += record_match[0]
            self.le_point.setText(str(point))
            team.close()
            match.close()
        elif self.cb_team.currentText() == "select team":
            QMessageBox.information(QtWidgets.QWidget(), "Information", "Select your team")
        elif self.cb_match.currentText() == "select match":
            QMessageBox.information(QtWidgets.QWidget(), "Information", "Select the match")

    def winner(self):
        if self.cb_match.currentText() != "select match":
            check = sqlite3.connect('cricket.db')
            cur_check = check.cursor()
            cur_check.execute(f"select team_name from collection where match = '{self.cb_match.currentText()}'")
            record = cur_check.fetchone()
            if record:
                win, result = [], []
                team = sqlite3.connect("cricket.db")
                cur_team = team.cursor()

                match = sqlite3.connect('cricket.db')
                cur_match = match.cursor()

                player = sqlite3.connect('cricket.db')
                cur_player = player.cursor()

                cur_team.execute(f"Select team_name, match from collection where match = '{self.cb_match.currentText()}'")

                while True:
                    point = 0
                    record_team = cur_team.fetchone()
                    if record_team == None:
                        break
                    cur_player.execute(f"select Player_id, Name from [{record_team[0]}]")
                    while True:
                        record_player = cur_player.fetchone()
                        if record_player == None:
                            break
                        cur_match.execute(f"select point from {self.cb_match.currentText()} where Player_id = {record_player[0]}")
                        record_match = cur_match.fetchone()
                        point += record_match[0]
                    win.append((point, record_team[0]))

                winner = max(win, key = lambda x: x[0])
                win.remove(winner)
                for value in win:
                    if winner[0] == value[0]:
                        result.append(value)
                result.append(winner)
                team.close()
                match.close()
                player.close()
                if len(result) > 1:
                    QMessageBox.information(QtWidgets.QWidget(), "Winner", f"match is draw between these team {', '.join([value[1] for value in result])} and having score {result[0][0]}")
                else:
                    QMessageBox.information(QtWidgets.QWidget(), "Winner", f"team '{result[0][1]}' win the {self.cb_match.currentText()} and having score {result[0][0]}")
            else:
                QMessageBox.information(QtWidgets.QWidget(), "Information", "No team belong to this match")
            check.close()

            
        else:
            QMessageBox.information(QtWidgets.QWidget(), "Information", "Select the match")
                
                
            
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setStyleSheet(".QWidget{background-color:brown;}")
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

