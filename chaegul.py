import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QApplication, QWidget
, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QTimer



class Chaegul(QWidget):
    
    def __init__(self,time,chaegul_data):
        super().__init__()
        
        self.chaegul_data = chaegul_data
        self.time = time
        print(self.chaegul_data)
        self.current_step = 0 
        self.initUI()

        
    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.append_text)
        self.startNextTimer()

        self.table = QTableWidget(0, 2)  # 0 rows and 2 columns
        self.table.setHorizontalHeaderLabels(['Price', 'Amount'])

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_table)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.table, 0)
        self.vbox.addWidget(self.clear_btn, 1)

        # self.setLayout(self.vbox)

        # self.setWindowTitle('Dynamic QTableWidget')
        # self.setGeometry(300, 300, 300, 300)
        # self.show()

    def append_text(self):
        price, amount = self.chaegul_data[self.current_step]
        print(price)
        
        # Insert a new row at the beginning
        self.table.insertRow(0)

        # Create QTableWidgetItem for price and amount
        price_item = QTableWidgetItem(str(price))
        amount_item = QTableWidgetItem(amount)

        # Set color based on condition
        if '+' in amount:
            color = QColor('red')
        elif '-' in amount:
            color = QColor('blue')
        
        # color_black = QColor('black')

        price_item.setForeground(color)
        amount_item.setForeground(color)

        # Add items to the table
        self.table.setItem(0, 0, price_item)
        self.table.setItem(0, 1, amount_item)

        self.current_step += 1
        self.startNextTimer()

    def startNextTimer(self):
        if self.current_step < len(self.time):
            interval = int(self.time[self.current_step] * 1000)
            self.timer.start(interval)
        else:
            self.timer.stop()

    def clear_table(self):
        self.table.setRowCount(0)
        
        
        
        