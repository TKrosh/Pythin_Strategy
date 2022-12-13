import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLCDNumber, QLabel
from PyQt5.QtGui import QFont

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        self.setWindowTitle('перекидыватель слов')
        self.setGeometry(100, 100, 260, 430)

        self.table = QLCDNumber(self)
        self.table.resize(257, 55)
        self.table.move(1, 50)

        self.second_table = QLabel(self)
        self.second_table.setFont(QFont('Times New Roman', 22))
        self.table.resize(257, 55)
        self.second_table.move(1, 0)

        self.math_work = []

        self.btn1 = QPushButton('1', self)
        self.btn1.resize(65, 65)
        self.btn1.move(1, 235)
        self.btn1.clicked.connect(self.add_one)

        self.btn2 = QPushButton('2', self)
        self.btn2.resize(65, 65)
        self.btn2.move(66, 235)
        self.btn2.clicked.connect(self.add_two)

        self.btn3 = QPushButton('3', self)
        self.btn3.resize(65, 65)
        self.btn3.move(131, 235)
        self.btn3.clicked.connect(self.add_three)

        self.btn4 = QPushButton('4', self)
        self.btn4.resize(65, 65)
        self.btn4.move(1, 170)
        self.btn4.clicked.connect(self.add_four)

        self.btn5 = QPushButton('5', self)
        self.btn5.resize(65, 65)
        self.btn5.move(66, 170)
        self.btn5.clicked.connect(self.add_five)

        self.btn6 = QPushButton('6', self)
        self.btn6.resize(65, 65)
        self.btn6.move(131, 170)
        self.btn6.clicked.connect(self.add_six)

        self.btn7 = QPushButton('7', self)
        self.btn7.resize(65, 65)
        self.btn7.move(1, 105)
        self.btn7.clicked.connect(self.add_seven)

        self.btn8 = QPushButton('8', self)
        self.btn8.resize(65, 65)
        self.btn8.move(66, 105)
        self.btn8.clicked.connect(self.add_einght)

        self.btn9 = QPushButton('9', self)
        self.btn9.resize(65, 65)
        self.btn9.move(131, 105)
        self.btn9.clicked.connect(self.add_nine)

        self.btn0 = QPushButton('0', self)
        self.btn0.resize(65, 65)
        self.btn0.move(66, 300)
        self.btn0.clicked.connect(self.add_zero)

        self.btn0 = QPushButton('CE', self)
        self.btn0.resize(65, 65)
        self.btn0.move(131, 300)
        self.btn0.clicked.connect(self.clean_last)

        self.btn_plus = QPushButton('+', self)
        self.btn_plus.resize(65, 65)
        self.btn_plus.move(195, 300)
        self.btn_plus.clicked.connect(self.plus)

        self.btn_eq = QPushButton('=', self)
        self.btn_eq.resize(130, 65)
        self.btn_eq.move(130, 365)
        self.btn_eq.clicked.connect(self.result)

        self.btn_minus = QPushButton('-', self)
        self.btn_minus.resize(65, 65)
        self.btn_minus.move(195, 235)
        self.btn_minus.clicked.connect(self.minus)

        self.btn_mult = QPushButton('*', self)
        self.btn_mult.resize(65, 65)
        self.btn_mult.move(195, 170)
        self.btn_mult.clicked.connect(self.mult)

        self.btn_div = QPushButton('/', self)
        self.btn_div.resize(65, 65)
        self.btn_div.move(195, 105)
        self.btn_div.clicked.connect(self.div)

        self.btn_clear = QPushButton('С', self)
        self.btn_clear.resize(65, 65)
        self.btn_clear.move(1, 300)
        self.btn_clear.clicked.connect(self.clear)

        self.btn_pow = QPushButton('±', self)
        self.btn_pow.resize(65, 65)
        self.btn_pow.move(66, 365)
        self.btn_pow.clicked.connect(self.change)

        self.btn_dot = QPushButton('.', self)
        self.btn_dot.resize(65, 65)
        self.btn_dot.move(1, 365)
        self.btn_dot.clicked.connect(self.dot)
        self.num = ''

    def clean_last(self):
        if self.num[:-1] == '':
            self.num = self.num[:-1]
            self.table.display('0')
        else:
            self.num = self.num[:-1]
            self.table.display(self.num)

    def empty_check(self):
        if self.num != '' and self.num != 'Error':
            self.math_work.append(self.num)

    def dot(self):
        if '.' in self.num:
            self.table.display(self.num)
        else:
            self.num += '.'
            self.table.display(self.num)

    def change(self):
        self.num = str(int(self.num) * -1)
        self.table.display(self.num)

    def result(self):
        self.empty_check()
        print(self.math_work)
        try:
            fast_result = str(eval(' '.join(_ for _ in self.math_work)))
        except Exception:
            fast_result = 'Error'
            self.math_work = []
            print('!', self.num)
            print('Error')
        if fast_result != 'Error':
            self.num = fast_result
        else:
            self.num = ''
        self.second_table.setText('')
        self.table.display(fast_result)
        self.math_work = []

    def clear(self):
        self.math_work = []
        self.num = ''
        self.table.display('0')

    def div(self):
        self.empty_check()
        self.math_work.append('/')
        self.second_table.setText(' '.join(_ for _ in self.math_work))
        self.table.display('')
        self.num = ''

    def mult(self):
        self.empty_check()
        self.math_work.append('*')
        self.second_table.setText(' '.join(_ for _ in self.math_work))
        self.table.display('')
        self.num = ''

    def plus(self):
        self.empty_check()
        self.math_work.append('+')
        self.second_table.setText(' '.join(_ for _ in self.math_work))
        self.table.display('')
        self.num = ''

    def minus(self):
        self.empty_check()
        self.math_work.append('-')
        self.second_table.setText(' '.join(_ for _ in self.math_work))
        self.table.display('')
        self.num = ''

    def add_one(self):
        self.num += '1'
        self.table.display(self.num)

    def add_two(self):
        self.num += '2'
        self.table.display(self.num)

    def add_three(self):
        self.num += '3'
        self.table.display(self.num)

    def add_four(self):
        self.num += '4'
        self.table.display(self.num)

    def add_five(self):
        self.num += '5'
        self.table.display(self.num)

    def add_six(self):
        self.num += '6'
        self.table.display(self.num)

    def add_seven(self):
        self.num += '7'
        self.table.display(self.num)

    def add_einght(self):
        self.num += '8'
        self.table.display(self.num)

    def add_nine(self):
        self.num += '9'
        self.table.display(self.num)

    def add_zero(self):
        if not self.num == '' and not self.num == '':
            self.num += '0'
            self.table.display(self.num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
