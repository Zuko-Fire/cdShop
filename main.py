from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit, QPlainTextEdit,QLineEdit
from PyQt5.QtCore import Qt
from  PostgreS import PostgreS


class Program():
    def __init__(self):
        self.postgres = None
        self.app = QApplication([])
        self.mainWidget = QWidget()
        self.table = QTableWidget()
        self.mainLayout = QVBoxLayout()
        self.girdlayout = QGridLayout()
        self.textEdit = QLineEdit('поиск')
        self.updateButton = QPushButton('Обновить')
        self.findButton = QPushButton('Найти')
        self.layoutTools = QHBoxLayout()
        self.widgets()

    def widgets(self):
        # self.textEdit.setFixedSize(1000,50)
        # self.textEdit.setFixedHeight(32)
        self.table = self.table
        self.table.setColumnCount(3)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(["Id", "Цена", "Название"])
        self.table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        self.table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        self.table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        self.mainWidget.setWindowTitle('Магазин дисков')

        # Set the alignment to the headers
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        self.table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        self.table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        self.table.setItem(1, 0, QTableWidgetItem('xxx'))
        self.table.resizeColumnToContents(2)
        self.table.resizeColumnToContents(1)
        self.table.resizeColumnToContents(0)
        self.girdlayout.addWidget(self.table)
        self.layoutTools.addWidget(self.updateButton, alignment=Qt.AlignLeft,stretch=4)
        self.layoutTools.addWidget(self.textEdit, alignment=Qt.AlignRight,stretch=1000)
        self.layoutTools.addWidget(self.findButton, alignment=Qt.AlignRight,stretch=4)
        self.layoutTools.setSpacing(10)
        self.mainLayout.addLayout(self.layoutTools)
        self.mainLayout.addLayout(self.girdlayout)
        self.mainWidget.resize(800, 600)
        self.updateButton.clicked.connect(self.update)
        self.findButton.clicked.connect(self.find)



    def connect(self):
        postgres = PostgreS()
        postgres.connect()
        self.postgres = postgres

    def update(self):
        data = self.postgres.getData()
        size = len(data)
        print(size)
        self.table.setRowCount(size)
        for i in range(size):
            for j in range(3):
                self.table.setItem(i, j, QTableWidgetItem(str(data[i][j])))
        # self.table.resizeColumnsToContents()


    def find(self):

        findPredicate = self.textEdit.text()
        result = self.postgres.findData(findPredicate)
        size = len(result)
        print(size)
        self.table.setRowCount(size)
        for i in range(size):
             for j in range(3):
                self.table.setItem(i, j, QTableWidgetItem(str(result[i][j])))

    def disconnect(self):
        self.postgres.close()






program = Program()
program.mainWidget.setLayout(program.mainLayout)
program.connect()
program.update()
print(program.postgres.getData())
program.mainWidget.show()
program.app.exec_()
program.disconnect()

