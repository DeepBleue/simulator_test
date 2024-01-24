import sys
import sys
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication, QTableWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QProgressBar

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)  # Set this to the number of data points you have
        self.tableWidget.setColumnCount(2)  # One column for the bar chart

        row_height = 12  # Height of each row
        column_width = 120  # Width of the column
        font = QFont()
        font.setPointSize(8)

        for i in range(20):
            self.tableWidget.setRowHeight(i, row_height)

        self.tableWidget.setColumnWidth(1, column_width)
        self.tableWidget.setColumnWidth(0, 50)
        
        
        # Data points for the bar chart
        data_points = [20, 55, 80, 30, 70, 65, 85, 40, 50, 60 , 20, 55, 80, 30, 70, 65, 85, 40, 50, 60]
        price = [2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050, 2055, 2060 , 2065, 2070, 2075, 2080, 2085, 2090, 2095, 2100, 2105, 2110]

        # Set up the bar chart
        for i, value in enumerate(data_points):
            
            
            text_item = QTableWidgetItem(f"{price[len(price)-(i+1)]}")
            text_item.setFont(font)
            text_item.setTextAlignment(Qt.AlignCenter)
            text_item.setFlags(text_item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEditable)
            self.tableWidget.setItem(i, 0, text_item)
            
            
            
            # Create the progress bar
            progress_bar = QProgressBar()
            progress_bar.setMaximum(max(data_points))  # Set the scale of the chart
            progress_bar.setValue(value)
            progress_bar.setAlignment(Qt.AlignVCenter)  # Center the text

            progress_bar.setFormat(f"  {value}")
            
            if i < 10 : 
            
                progress_bar.setStyleSheet("""
                    QProgressBar {
                        border: 1px solid grey;
                        border-radius: 1px;
                        background-color: #FFFFFF;
                        padding : 0px;
                        margin : 0px;
                        font-size: 10px;
                    }
                    QProgressBar::chunk {
                        background-color: #87CEFA;  /* Red color */
                        width: 10px;  /* Chunk size */
                        border-left: 3px solid transparent;
                    }
                """)
                
            else : 
                progress_bar.setStyleSheet("""
                    QProgressBar {
                        border: 1px solid grey;
                        border-radius: 1px;
                        background-color: #FFFFFF;
                        padding = 0px;
                        font-size: 10px;
                    }
                    QProgressBar::chunk {
                        background-color: #e5a3a3;  /* Red color */
                        width: 10px;  /* Chunk size */
                        border-left: 3px solid transparent;
                    }
                """)
                
                # Insert the progress bar into the table
            self.tableWidget.setCellWidget(i, 1, progress_bar)

        # Layout for the widget
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('Progress Bar Chart')
        self.setGeometry(300, 300, 300, 600)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
