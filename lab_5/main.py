import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import (QInputDialog, QApplication, QLineEdit, QGridLayout, QLabel, QWidget, QToolTip, QTextEdit, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow)
from algo import gauss

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600,600)        
        self.matrix = [[2,5,4,1,20],[1,3,2,1,11],[2,10,9,7,40],[3,8,9,2,37]]
        self.matrix_edit = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        lbl1 = QLabel('Лабораторна робота 5 - \nМетод Гауса\nЗ послідовним виключенням елементів - \n25 варіант')
        lbl2 = QLabel('Студент групи ІВ-82')
        lbl3 = QLabel('Троценко\nДанііл\nАнатолійович')
        
        btn1 = QPushButton('Вірішити')
        btn1.clicked.connect(self.solve)

        grid = QGridLayout()
        grid.setSpacing(1)

        for i in range(len(self.matrix_edit)):
            for j in range(len(self.matrix_edit[i])):
                self.matrix_edit[i][j] = QLineEdit(str( self.matrix[i][j] ))

        

        grid.addWidget(lbl1,0,0)
        grid.addWidget(lbl2,0,1)
        grid.addWidget(lbl3,0,2)

        for i in range(len(self.matrix_edit)):
            for j in range(len(self.matrix_edit[i])):
                print(self.matrix_edit[i][j])
                grid.addWidget(self.matrix_edit[i][j], i+1, j)

        self.l1 = QLabel()
        self.l2 = QLabel()
        self.l3 = QLabel()
        self.l4 = QLabel()

        grid.addWidget(btn1,8,1)
        grid.addWidget(self.l1,7,0)
        grid.addWidget(self.l2,7,1)
        grid.addWidget(self.l3,7,2)
        grid.addWidget(self.l4,7,3)

        self.setLayout(grid) 
        

        self.setWindowTitle('Lab-5')   
        self.show()


    def solve(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = float(str(self.matrix_edit[i][j].text()))
        solves = gauss(self.matrix)
        self.l1.setText("x1 = " + str(solves[0]))
        self.l2.setText("x2 = " + str(solves[1]))
        self.l3.setText("x3 = " + str(solves[2]))
        self.l4.setText("x4 = " + str(solves[3]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())