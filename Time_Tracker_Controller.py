import time
import datetime
import pickle, json
import collections
import Time_Tracker_UI
from PyQt5 import QtWidgets, QtGui, QtCore#, QListWidget
from Time_Tracker_UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()     ###將 ui 設定為ui程式中的主程式
        self.ui.setupUi(self)
        self.setup_control()
        self.event_list = collections.defaultdict(int)
        self.start_time = 0
        self.is_recording = False
        self.selected_item = ''
        self.load_list = collections.defaultdict(int)
        self.location = r'C:\\Users\\USER\\Desktop\\PyQt_save_data\\'
        
    def setup_control(self):   ## 主控制，底下加入各種按鈕控制
        self.ui.add_new_event.clicked.connect(self.buttonClicked_add_event)  
        self.ui.listWidget.itemClicked.connect(self.Widget_clicked)          #listWidget按下項目
        self.ui.edit_event.clicked.connect(self.buttonClicked_edit_event)          #按下修改項目
        self.ui.remove_event.clicked.connect(self.buttonClicked_remove_event)        #刪除項目
        self.ui.start_time.clicked.connect(self.start_time)
        self.ui.end_time.clicked.connect(self.end_time)
        self.ui.calendarWidget.clicked.connect(self.data_clicked)
        self.ui.show_date.clicked.connect(self.load_data)

        
    def buttonClicked(self):
        msg = self.ui.input_event.text()
        self.ui.show_text.setText(msg)
        
    def not_in_listWidget(self, msg):       #檢查是否已在名單內
        all_items = self.ui.listWidget.findItems(str(msg), QtCore.Qt.MatchRegExp)
        if len(all_items) == 0:
            return True
        return False
        
    
    def buttonClicked_add_event(self):
        msg = self.ui.input_event.text()
        if msg=="": return
        if self.not_in_listWidget(msg):
            self.ui.listWidget.addItem(str(msg))
        else: print("Error: 重複事件名稱 !!")        
        
    def buttonClicked_edit_event(self):
        msg = self.ui.input_event.text()
        sel_items = self.ui.listWidget.selectedItems()   ## 輸出選取事件 list 資料
        
        ##(跳出新視窗)詢問是否確定要修改
        reply = QtWidgets.QMessageBox.question(self, 'Notice', '確定要修改嗎', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:      ##按確定後修改事件名稱
            print('Yes clicked.')
            if self.not_in_listWidget(msg):
                for item in sel_items:                       
                    item.setText(str(msg))
            else: print("Error: 重複事件名稱 !!")
        else:
            print('No clicked.')
    
    def buttonClicked_remove_event(self):
        if self.selected_item != None:
            reply = QtWidgets.QMessageBox.question(self, 'Notice', '你確定要刪除'+str(self.selected_item)+'?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            current_item = self.ui.listWidget.currentItem()
            if reply == QtWidgets.QMessageBox.Yes:
                self.ui.listWidget.takeItem(self.ui.listWidget.row(current_item))
    
    def data_clicked(self): #選擇日曆上的一天 
        date_picked = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        print(date_picked)
        
        
    def start_time(self):
        if self.selected_item == "":
            QtWidgets.QMessageBox.about(self ,"錯誤", "請先選擇工作項目!!")
            print("請先選擇工作項目!!")
        elif self.is_recording==False:
            reply = QtWidgets.QMessageBox.question(self, 'Notice', '你正要開始'+str(self.selected_item)+'嗎?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.start_time = time.time()
                self.is_recording=True
            #print(self.start_time)
    
    def end_time(self):
        if self.is_recording:
            end_time = time.time()
            event_time = end_time-self.start_time
            print("start time:",self.start_time,'\n',"end time",end_time,'\n',"event_time",event_time)
            current_item = self.ui.listWidget.currentItem()
            self.event_list[str(current_item.text())] += event_time
            print("dict:"+str(current_item.text()),self.event_list[str(current_item.text())])
            self.is_recording = False
            self.save_data()
        else: print("Error:還沒開始記錄，請先開始計時")
        
    def save_data(self):
        try:
            date = datetime.date.today() #self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            save = open(self.location + str(date)+'.json', 'w')
            json. dump(self.event_list, save)
            save.close()
        except:
            pass
    
    def load_data(self):    #秀出此天的資料
        try:
            date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            with open(self.location+str(date)+'.json','r') as l:
                self.load_list = json.load(l)
            slm = QtCore.QStringListModel()
            slm.setStringList(self.load_list.keys())
            self.ui.listView.setModel(slm)
            abc = QtCore.QStringListModel()
            value=list(self.load_list.values())
            b=[]
            c=[]
            for i in value:
                minu,sec=divmod(i,60)
                b.append(str(int(minu)))
                c.append(str(round(sec,1)))
            abc.setStringList(b)
            self.ui.listView_time.setModel(abc)
            de = QtCore.QStringListModel()
            de.setStringList(c)
            self.ui.listView_time_2.setModel(de)
        except:             #若無當天檔案
            no2 = QtCore.QStringListModel()
            no2.setStringList([''])         #裏頭必須是list
            self.ui.listView.setModel(no2)          
            self.ui.listView_time.setModel(no2)
            self.ui.listView_time_2.setModel(no2)
        

    def Widget_clicked(self): 
        current_item = self.ui.listWidget.currentItem()
        self.selected_item = current_item.text()
                                     
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())