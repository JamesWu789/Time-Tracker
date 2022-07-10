# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Self_App.ui'
# Created by: PyQt5 UI code generator 5.15.6
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(470, 20, 296, 229))
        self.calendarWidget.setObjectName("calendarWidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(210, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(490, 340, 91, 201))
        self.listView.setObjectName("listView")
        self.listView_time = QtWidgets.QListView(self.centralwidget)
        self.listView_time.setGeometry(QtCore.QRect(590, 340, 81, 201))
        self.listView_time.setObjectName("listView_time")
        self.listView_time_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_time_2.setGeometry(QtCore.QRect(680, 340, 81, 201))
        self.listView_time_2.setObjectName("listView_time_2")
        self.show_date = QtWidgets.QPushButton(self.centralwidget)
        self.show_date.setGeometry(QtCore.QRect(470, 280, 141, 28))
        self.show_date.setObjectName("show_date")
        self.add_new_event = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_event.setGeometry(QtCore.QRect(60, 130, 93, 28))
        self.add_new_event.setObjectName("add_new_event")
        self.input_event = QtWidgets.QLineEdit(self.centralwidget)
        self.input_event.setGeometry(QtCore.QRect(60, 60, 121, 41))
        self.input_event.setText("")
        self.input_event.setObjectName("input_event")
        self.edit_event = QtWidgets.QPushButton(self.centralwidget)
        self.edit_event.setGeometry(QtCore.QRect(60, 170, 93, 28))
        self.edit_event.setObjectName("edit_event")
        self.remove_event = QtWidgets.QPushButton(self.centralwidget)
        self.remove_event.setGeometry(QtCore.QRect(50, 190, 93, 28))
        self.remove_event.setObjectName("remove_event")
        self.start_time = QtWidgets.QPushButton(self.centralwidget)
        self.start_time.setGeometry(QtCore.QRect(70, 337, 141, 51))
        self.start_time.setObjectName("start_time")
        self.end_time = QtWidgets.QPushButton(self.centralwidget)
        self.end_time.setGeometry(QtCore.QRect(70, 400, 141, 51))
        self.end_time.setObjectName("end_time")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(490, 310, 71, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 310, 191, 22))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 10, 71, 22))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.create_piechart()
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_piechart(self):
        # 创建QPieSeries对象，它用来存放饼图的数据
        series = QPieSeries()
        # append方法中的数字，代表的是权重，完成可以改成其它，如80,70,60等等
        series.append("Python", 8)
        series.append("Java", 7)
        series.append("C", 6)
        series.append("C++", 5)
        series.append("PHP", 4)
        series.append("Swift", 3)
        # 单独处理某个扇区
        slice = QPieSlice()
        # 这里要处理的是python项，是依据前面append的顺序，如果是处理C++项的话，那索引就是3
        slice = series.slices()[0]
        # 突出显示，设置颜色
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.red, 2))
        slice.setBrush(Qt.red)
        # 创建QChart实例，它是PyQt5中的类
        chart = QChart()
        # QLegend类是显示图表的图例，先隐藏掉
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        # 设置动画效果
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 设置标题
        #chart.setTitle("饼图示例")
        #chart.legend().setVisible(True)
        # 对齐方式
        chart.legend().setAlignment(Qt.AlignBottom)
        # 创建ChartView，它是显示图表的控件
        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        #self.setCentralWidget(chartview)        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_new_event.setText(_translate("MainWindow", "新增事件"))
        self.edit_event.setText(_translate("MainWindow", "修改事件"))
        self.start_time.setText(_translate("MainWindow", "開始計時"))
        self.end_time.setText(_translate("MainWindow", "結束計時"))
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() #主要任務為繼承MainWindow
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) #一定要打，建立Ui的動作，它要告訴你的呼叫程式說，這個 Ui 我都要用到哪些功能這樣的概念。
    MainWindow.show()
    sys.exit(app.exec_())'''