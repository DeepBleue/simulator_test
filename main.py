from util.util import table_to_dataframe, get_table_names
import pandas as pd
from util.info import information
from util.df_processing import db_A_preprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from chaegul import Chaegul


class MyAPP(QWidget):
    
    def __init__(self):
        super().__init__()
        
        
        host = information.HOST
        user = information.USER
        password = information.PASSWORD
        
        
        databaseA = "A20240116"  # 체결
        databaseB = "B20240116"  # 호가
        
        
        self.table = get_table_names(host, user, password, databaseA)
        self.code = self.table[0][0]   # 005860
        
        
        
        df_A = table_to_dataframe(host, user, password, databaseA,self.code)
        time_A,chaegul_data = db_A_preprocess(df_A)
        
        # print(time_A,chaegul_data)
        
        
        chaegul_UI = Chaegul(time_A,chaegul_data)
        
        chaegul_UI_vbox = chaegul_UI.vbox
        
        
        self.setLayout(chaegul_UI_vbox)

        self.setWindowTitle('Dynamic QTableWidget')
        self.setGeometry(300, 300, 300, 300)
        self.show()

        
    
        


if __name__ == '__main__' :
    app = QApplication(sys.argv)
    ex = MyAPP()
    sys.exit(app.exec_())
    
    
    
    