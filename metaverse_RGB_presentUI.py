# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:49:02 2022

@author: PC
"""

import pyautogui
import numpy as np
from PIL import Image
savepath = 'C:\\SynologyDrive\\worik in progress\\metaverse_RGB_presentUI\\'

if False:
    myScreenshot = pyautogui.screenshot()    
    myScreenshot.save(savepath + 'test.jpg')


#%% color image gen
if False:
    
    template = np.zeros((1200-150, 1850, 3))
    
    black = np.array(template, dtype=np.uint8);
    img = Image.fromarray(black)
    img.save(savepath + 'black_size.png', 'png')
    
    red = np.array(template, dtype=np.uint8); red[:,:,0] = 255
    img = Image.fromarray(red)
    img.save(savepath + 'red_size.png', 'png')
    
    green = np.array(template, dtype=np.uint8); green[:,:,1] = 255
    img = Image.fromarray(green)
    img.save(savepath + 'green_size.png', 'png')
    
    blue = np.array(template, dtype=np.uint8); blue[:,:,2] = 255
    img = Image.fromarray(blue)
    img.save(savepath + 'blue_size.png', 'png')
    
    gray = np.array(template, dtype=np.uint8); gray[:,:,:] = 125
    img = Image.fromarray(gray)
    img.save(savepath + 'gray_size.png', 'png')


#%%

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, QCoreApplication

# from time import sleep
from datetime import datetime

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.filepath = {}
        self.filepath = {'black': savepath + 'black_size.png', 'blue': savepath + 'blue_size.png', \
                         'red': savepath + 'red_size.png', 'green': savepath + 'green_size.png', 'gray': savepath + 'gray_size.png'}
        self.cnt = 0
        
        self.lbl_img = QLabel()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.initUI)

    def initUI(self):
        def msScreenshot(savename):
            myScreenshot = pyautogui.screenshot()
            savepath = 'C:\\SynologyDrive\\worik in progress\\metaverse_RGB_presentUI\\'
            dt = datetime.today()   
            currenttime = dt.strftime("%Y_%m_%d__%H_%M")
            myScreenshot.save(savepath + savename + '_' + currenttime + '.jpg')
        
        base_sec = 10

        if self.cnt == 0:
            pixmap = QPixmap(self.filepath['black'])
            
            self.lbl_img.setPixmap(pixmap)
            vbox = QVBoxLayout()
            vbox.addWidget(self.lbl_img)
            
            self.setLayout(vbox)
            self.setWindowTitle('QPixmap')
            self.move(0, 0)
            self.show() 
            
        elif self.cnt >= base_sec and self.cnt < 360 + base_sec:
            if int(self.cnt - base_sec) % 36 == 0:
                pixmap = QPixmap(self.filepath['red'])
                self.lbl_img.setPixmap(pixmap)
                msScreenshot(str(int(self.cnt)) + '_red')
   
            elif int(self.cnt - base_sec) % 36 == 10:
                pixmap = QPixmap(self.filepath['black'])
                self.lbl_img.setPixmap(pixmap)
                
            elif int(self.cnt - base_sec) % 36 == 12:
                pixmap = QPixmap(self.filepath['blue'])
                self.lbl_img.setPixmap(pixmap)
                
            elif int(self.cnt - base_sec) % 36 == 22:
                pixmap = QPixmap(self.filepath['black'])
                self.lbl_img.setPixmap(pixmap)
                
            elif int(self.cnt - base_sec) % 36 == 24:
                pixmap = QPixmap(self.filepath['green'])
                self.lbl_img.setPixmap(pixmap)
                
            elif int(self.cnt - base_sec) % 36 == 34:
                pixmap = QPixmap(self.filepath['black'])
                self.lbl_img.setPixmap(pixmap)
                
        elif self.cnt >= 360 + base_sec:
            pixmap = QPixmap(self.filepath['gray'])
            self.lbl_img.setPixmap(pixmap)

        print(self.cnt)
        self.cnt += 1
           
        
#%%
app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())

#%%


cnt = 10

(cnt - 10) % 36 == 10
































