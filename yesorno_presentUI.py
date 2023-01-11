# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:49:02 2022

@author: PC
"""

import pyautogui
import numpy as np
from PIL import Image
savepath = 'C:\\SynologyDrive\\worik in progress\\yes_or_no\\'

import sys; 
sys.path.append('D:\\mscore\\code_lab\\')
sys.path.append('C:\\mscode')
import msFunction
from datetime import datetime

dt = datetime.today()   
currenttime = dt.strftime("%Y_%m_%d__%H_%M_%S")
savepath2 = savepath + currenttime + '//'
msFunction.createFolder(savepath2)
#%%

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, QCoreApplication

# from time import sleep

import random
import pandas as pd

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.filepath = {}
        self.filepath = {'응': savepath + '응.png', '아니': savepath + '아니.png', \
                         'count_1': savepath + 'count_1.png', 'count_2': savepath + 'count_2.png', \
                         'count_3': savepath + 'count_3.png', 'gray': savepath + 'gray_size.png', \
                         'black': savepath + 'black_size.png'}
        self.cnt = 0
        
        self.lbl_img = QLabel()

        self.timer = QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self.initUI)
        self.random_waitsec = np.inf
        self.random_choice = 2
        self.sw1 = True
        self.sw2 = True
        self.sw3 = True
        
        self.mssave = []
        self.cnt2 = 0
        self.cnt3 = 0

    def initUI(self):
        def msScreenshot(savename):
            myScreenshot = pyautogui.screenshot()
            dt = datetime.today()   
            currenttime = dt.strftime("%Y_%m_%d__%H_%M_%S")
            myScreenshot.save(savepath2 + savename + '_' + currenttime + '.jpg')
        
        base_sec = 10
        if self.sw3 and self.cnt == base_sec*10:
            savename = 'startat'; msScreenshot(savename)
            self.sw3 = False
        
        if self.cnt3 == 2 and self.cnt > self.random_waitsec + 33:
            df = pd.DataFrame(self.mssave)
            dt = datetime.today()   
            currenttime = dt.strftime("%Y_%m_%d__%H_%M_%S")
            df.to_csv(savepath2 + currenttime + '_log.csv', header=False, index=False)
            
            self.cnt3 += 1
            
        elif self.cnt3 == 3 and self.cnt > self.random_waitsec + 43:
            pixmap = QPixmap(self.filepath['black'])
            self.lbl_img.setPixmap(pixmap)

        elif self.cnt3 < 2:
            if self.cnt == 0:
                pixmap = QPixmap(self.filepath['gray'])
                
                self.lbl_img.setPixmap(pixmap)
                vbox = QVBoxLayout()
                vbox.addWidget(self.lbl_img)
                
                self.setLayout(vbox)
                self.setWindowTitle('QPixmap')
                self.move(0, 0)
                self.show()
                
                self.random_waitsec = random.randint(30,50)
                if self.sw2: 
                    self.random_waitsec = self.random_waitsec + (base_sec * 10)
                print('self.random_waitsec', self.random_waitsec, self.sw2)
    
            
            if self.random_choice != 2:
                self.sw2 = False
                if self.cnt > self.random_waitsec + 33:   
                    self.cnt = -1
                    self.random_choice = 2
                    self.sw1 = True
                    
                elif self.cnt > self.random_waitsec + 23 and self.sw1:
                    if self.random_choice != 0:
                        pixmap = QPixmap(self.filepath['응'])
                        self.lbl_img.setPixmap(pixmap)
                        self.sw1 = False
                        savename = '응'; msScreenshot(savename)
                        self.cnt3 += 1
                        self.mssave.append([self.cnt3, self.cnt2, 1])
                        
                    elif self.random_choice != 1:
                        pixmap = QPixmap(self.filepath['아니'])
                        self.lbl_img.setPixmap(pixmap)
                        self.sw1 = False
                        savename = '아니'; msScreenshot(savename)
                        self.cnt3 += 1
                        self.mssave.append([self.cnt3, self.cnt2, 0])
                        
            else:
                if self.cnt > self.random_waitsec + 20:
                    pixmap = QPixmap(self.filepath['count_1'])
                    self.lbl_img.setPixmap(pixmap)
                    
                    self.random_choice = random.randint(0,1)
                    
                elif self.cnt > self.random_waitsec + 10:
                    pixmap = QPixmap(self.filepath['count_2'])
                    self.lbl_img.setPixmap(pixmap)
                    
                elif self.cnt > self.random_waitsec:
                    pixmap = QPixmap(self.filepath['count_3'])
                    self.lbl_img.setPixmap(pixmap)


        print(self.cnt)
        self.cnt += 1
        self.cnt2 += 1
        
        
#%%
app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())

#%%


cnt = 10

(cnt - 10) % 36 == 10
































