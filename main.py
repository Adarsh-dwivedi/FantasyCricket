from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.uic import loadUi
import sys

##style = '''
##QPushButton {
##    background-color : lightblue;
##    border : 2px solid;
##    border-radius : 4px;
##    padding : 4px 4px;
##}
##
##QPushButton:hover{
##    background-color : blue;
##    border : 2px solid;
##    border-radius : 4px;
##    padding : 4px 4px;
##}
##QPushButton:pressed{
##    background-color : white;
##    border : 2px solid;
##    border-radius : 4px;
##    padding : 4px 4px;
##}
##'''
##label = '''
##    QLineEdit{
##    border : 0px;
##    border-bottom : 2px solid red;
##    }
##    QLineEdit:focus{
##    background-color : white;
##    border : 2px solid red;
##    }
##    
##'''
app = QApplication(sys.argv)
ui = loadUi("Evaluate.ui")
#ui.pushButton_2.setStyleSheet(style)
#ui.lineEdit.setStyleSheet(label)
ui.show()
sys.exit(app.exec_())
