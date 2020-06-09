import sys
from PyQt5.QtWidgets import (QInputDialog, QApplication, QLineEdit, QGridLayout, QLabel, QWidget, QToolTip, QTextEdit, QPushButton, QApplication, QMessageBox, QDesktopWidget, QMainWindow)
import algo
import numpy as np
import time
import matplotlib.pyplot as plt
import math

test_arrays = [10, 100, 500, 1000, 2000, 5000, 10000, 50000, 100000, 500000]
test_time = [0.0, 0.005987, 0.0643, 0.108,0.203, 0.7748, 2.137, 26.36, 73.45, 73.45*5.1]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        lbl1 = QLabel('Лабораторна робота №2 - Сортування Боуза-Нельсона - 25 варіант')
        lbl2 = QLabel('Студент групи ІВ-82')
        lbl3 = QLabel('Троценко\nДанііл\nАнатолійович')
        lbl4 = QLabel('Розміри масивів - 10 100 500 1000 2000 5000 10000 50000 100000 500000')
        lbl5 = QLabel('ВСього - 10 рандомних тестових масивів')

        ell1 = QLabel('Введіть розмір бажаного масиву:')
        self.el1 = QLineEdit()
        btn1 = QPushButton('Ввести та показати час')
        btn1.clicked.connect(self.show_own)

        ell2 = QLabel('Тестові рандомні масиви:')
        btn2 = QPushButton('Показати графіки теоретичних масивів')
        btn2.clicked.connect(self.show_theorical)
        self.label_time = QLabel('Час:')
        self.label_time2 = QLabel()

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(lbl1,0,0)
        grid.addWidget(lbl2,0,1)
        grid.addWidget(lbl3,0,2)
        grid.addWidget(lbl4,1,0)
        grid.addWidget(lbl5,1,2)

        grid.addWidget(ell1, 2,0)
        grid.addWidget(self.el1, 2,1)
        grid.addWidget(btn1, 2,2)


        grid.addWidget(ell2, 3,0)
        grid.addWidget(btn2, 3,2)
        grid.addWidget(self.label_time, 4,0)
        grid.addWidget(self.label_time2, 4,1)

        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Review')   
        self.show()

    def show_own(self):
        if not self.el1.text().isdigit():
            return
        tests = np.random.sample(int(self.el1.text())) * 200 - 100

        start_time = time.time()
        algo.bose_nelson(tests)
        end_time = time.time() - start_time
        print(float(end_time))
        self.label_time2.setText(str(end_time))


    def show_theorical(self):
        fig, ax = plt.subplots()
        ax.plot(test_arrays, test_time)
        ax.grid()
        ax.set_xlabel(' Розмір масиву',
              fontsize = 15,    #  размер шрифта
              color = 'red',    #  цвет шрифта
              #  параметры области с текстом
              bbox = {'boxstyle': 'rarrow',    #  вид области
                      'pad': 0.1,     #  отступы вокруг текста
                      'facecolor': 'white',    #  цвет области
                      'edgecolor': 'red',    #  цвет крайней линии
                      'linewidth': 3})

        ax.set_ylabel('Швидкість сортування',
              fontsize = 15,
              color = 'red',
              bbox = {'boxstyle': 'rarrow',
                      'pad': 0.1,
                      'facecolor': 'white',
                      'edgecolor': 'red',
                      'linewidth': 3})

        fig.set_figwidth(9)
        fig.set_figheight(9)
        plt.title(label='Сортування. Фактичний час')
        plt.show()


        tests = np.linspace(0, 500000)
        fig, ax = plt.subplots()
        ax.plot(tests, tests * np.log2(tests)  )
        ax.grid()
        ax.set_xlabel(' Розмір масиву',
              fontsize = 15,    #  размер шрифта
              color = 'red',    #  цвет шрифта
              #  параметры области с текстом
              bbox = {'boxstyle': 'rarrow',    #  вид области
                      'pad': 0.1,     #  отступы вокруг текста
                      'facecolor': 'white',    #  цвет области
                      'edgecolor': 'red',    #  цвет крайней линии
                      'linewidth': 3})

        ax.set_ylabel('Швидкість сортування',
              fontsize = 15,
              color = 'red',
              bbox = {'boxstyle': 'rarrow',
                      'pad': 0.1,
                      'facecolor': 'white',
                      'edgecolor': 'red',
                      'linewidth': 3})

        fig.set_figwidth(9)
        fig.set_figheight(9)
        plt.title(label='Сортування. Теоретичний час')
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())