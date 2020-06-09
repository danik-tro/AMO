import numpy as np
import matplotlib.pyplot as plt
from lagranz_algo import lagranz
import sys
from PyQt5.QtWidgets import (QInputDialog, QApplication, QLineEdit, QGridLayout, QLabel, QWidget, QToolTip, QTextEdit, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow)
from algo import hord_nuton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        lbl1 = QLabel('Лабораторна робота №4 - \nКомбінований метод\n2xlnx-1 - \n25 варіант')
        lbl2 = QLabel('Студент групи ІВ-82')
        lbl3 = QLabel('Троценко\nДанііл\nАнатолійович')

        btn1 = QPushButton('Показати графік')
        btn1.clicked.connect(self.Lag)

        label_a = QLabel('a = ')
        label_b = QLabel('b = ')
        label_i = QLabel('i = ')
        

        self.edit_a = QLineEdit()
        self.edit_b = QLineEdit()
        self.edit_i = QLineEdit()

        self.edit_a.setText('1')
        self.edit_b.setText('3')
        self.edit_i.setText('10')

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(lbl1,0,0)
        grid.addWidget(lbl2,0,1)
        grid.addWidget(lbl3,0,2)

        grid.addWidget(label_a,1,0)
        grid.addWidget(self.edit_a,1,1)
        grid.addWidget(label_b,2,0)
        grid.addWidget(self.edit_b,2,1)
        grid.addWidget(label_i,3,0)
        grid.addWidget(self.edit_i,3,1)
        grid.addWidget(btn1, 4,1)

        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Lab-3')   
        self.show()

    def Lag(self):
        a = int(self.edit_a.text())
        b = int(self.edit_b.text())
        k = int(self.edit_i.text()) + 1

        f = lambda x: 2*x*np.log(x) - 1
        x=np.array([ a + i*(b-a)/10 for i in range(k)], dtype=float)
        y = f(x)

        xnew=np.linspace(np.min(x),np.max(x), k)
        ynew=[lagranz(x,y,i) for i in xnew]
        fig, ax = plt.subplots()

        ax.plot(x,y, label='2x-lnx')
        ax.plot(xnew,ynew,'o', label='Інтерполяція Многочленом Лагранжа')
        ax.plot(hord_nuton(), f(hord_nuton()),'o', label='Корінь')


        ax.legend()

        

        fig.set_figheight(5)
        fig.set_figwidth(8)

        plt.grid(True)
        plt.show()


        
        plt.plot(x_new_end, errors)
        plt.show



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())