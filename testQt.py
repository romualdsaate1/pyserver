# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:10:36 2019

@author: romua
"""


from tout import Listener
import myo
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel,  QFormLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import time


##listener = Listener()
#variable = a.output()
#print(variable)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Myo'
        self.left = 10
        self.top = 10
        self.width = 1100
        self.height = 250
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.l11 = QLineEdit(self)
        self.l12 = QLineEdit(self)
        self.l13 = QLineEdit(self)
        self.l14 = QLineEdit(self)

        label = QLabel('Orientation', self)
        label.move(30,20)
        label11 = QLabel('Orient_x:', self)
        self.l11.move(65, 40)
        label11.move(10,40)
        label12 = QLabel('Orient_y:', self)
        self.l12.move(65, 65)
        label12.move(10,65)
        label13 = QLabel('Orient_z:', self)
        self.l13.move(65, 90)
        label13.move(10,90)
        label14 = QLabel('Orient_w:', self)
        self.l14.move(65, 115)                 
        label14.move(10,115)

        #da = Output.parts[0]

        #self.l11.setText("ghsklk")
        
        
        self.l21 = QLineEdit(self)
        self.l22 = QLineEdit(self)
        self.l23 = QLineEdit(self)
        
        label2 = QLabel('Acceloremeter', self)
        label2.move(250,20)
        label21 = QLabel('Acc_x:', self)
        self.l21.move(290, 40)
        label21.move(240,40)
        label22 = QLabel('Acct_y:', self)
        self.l22.move(290, 65)
        label22.move(240,65)
        label23 = QLabel('Acc_z:', self)
        self.l23.move(290, 90)
        label23.move(240,90)
        
        
        self.l31 = QLineEdit(self)
        self.l32 = QLineEdit(self)
        self.l33 = QLineEdit(self)
        
        label3 = QLabel('Gyroscopy', self)
        label3.move(450,20)
        label31 = QLabel('Gyro_x:', self)
        self.l31.move(480, 40)
        label31.move(440,40)
        label32 = QLabel('Gyro_x:', self)
        self.l32.move(480, 65)
        label32.move(440,65)
        label33 = QLabel('Gyro_x:', self)
        self.l33.move(480, 90)
        label33.move(440,90)
        
        
        self.l41 = QLineEdit(self)
        self.l42 = QLineEdit(self)
        self.l43 = QLineEdit(self)
        self.l44 = QLineEdit(self)
        self.l45 = QLineEdit(self)
        self.l46 = QLineEdit(self)
        self.l47 = QLineEdit(self)
        self.l48 = QLineEdit(self)
        
        label4 = QLabel('Electromyographie', self)
        label4.move(850,20)
        label41 = QLabel('emg_1:', self)
        self.l41.move(730, 40)
        label41.move(690,40)
        label42 = QLabel('emg_2:', self)
        self.l42.move(730, 65)
        label42.move(690,65)
        label43 = QLabel('emg_3:', self)
        self.l43.move(730, 90)
        label43.move(690,90)
        label44 = QLabel('emg_4:', self)
        self.l44.move(730, 115)                 
        label44.move(690,115)
        
        label45 = QLabel('emg_5:', self)
        self.l45.move(930, 40)
        label45.move(890,40)
        label46 = QLabel('emg_6:', self)
        self.l46.move(930, 65)
        label46.move(890,65)
        label47 = QLabel('emg_7:', self)
        self.l47.move(930, 90)
        label47.move(890,90)
        label48 = QLabel('emg_8:', self)
        self.l48.move(930, 115)                 
        label48.move(890,115)

        self.lpo = QLineEdit(self)
        pose = QLabel('Pose:', self)
        self.lpo.move(680, 150)
        self.lpo.resize(200, 40)
        pose.move(650, 165)

        
        self.lre = QLineEdit(self)
        result = QLabel('Result:', self)
        self.lre.move(120, 150)   
        self.lre.resize(400, 50)              
        result.move(80,165)
        
        
        
        button = QPushButton('CNN_Calcul', self)
        button.setToolTip('This is an example CNN')
        button.move(900,200)
        button.clicked.connect(self.on_click)
        
        button1 = QPushButton('Cancel', self)
        button1.setToolTip('This is an example delete')
        button1.move(820,200)
        button1.clicked.connect(self.btn_press)
        
        
        
        self.show()



    @pyqtSlot()
    def on_click(self):
        # print('PyQt5 button click')
        #self.l11.setText("ggg")
        myo.init()
        feed = myo.ApiDeviceListener
        hub = myo.Hub()
        listener = Listener()
        listener.startListen(hub)

        #print(listener.output())
        #while hub.run(listener.on_event, 500):
            #print(listener.output())
            #if listener.output() != None:
                #tab = listener.output()
                #self.l11.setText(tab[0])
            
        #time.sleep(1000) 
         
        #pass
        
    def btn_press(self):
        sender = self.sender()
        if sender.text() == "Orient_x":  #if text == Press me
            x=self.l11.text()
            print(x)
                              #print the text in line edit
        else:
            self.l11.clear()
            self.l12.clear()
            self.l13.clear()
            self.l14.clear()
            self.l21.clear()
            self.l22.clear()
            self.l23.clear()
            self.l31.clear()
            self.l32.clear()
            self.l33.clear()
            self.l41.clear()
            self.l42.clear()
            self.l43.clear()
            self.l44.clear()
            self.l45.clear()
            self.l46.clear()
            self.l47.clear()
            self.l48.clear()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    
    
    
