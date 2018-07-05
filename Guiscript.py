from PyQt5 import QtGui,QtWidgets

import sys

class MyForm(QtGui.QWindow):
    
    def __init__(self):
        super(MyForm,self).__init__()
        
        lbl= QtWidgets.QLabel
        self.setGeometry(300, 300, 450, 150)
        self.setTitle('Ahmad Hamdy')
        self.show()
        
app = QtWidgets.QApplication(sys.argv)
mainwindow = MyForm()
status = app.exec_()
sys.exit(status)

