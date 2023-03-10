# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:49:02 2022

@author: PC
"""

import pyautogui
import numpy as np
from PIL import Image
savepath = 'C:\\SynologyDrive\\worik in progress\\metaverse_project\\metaverse_focus_disruption\\'
savepath = 'C:\\Users\\msbak\\SynologyDrive - work\\metaverse_focus_disruption\\'
savepath2 = savepath + 'focus_out_imgs\\'
savepath3 = savepath + '\\screenshot_save\\'

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
import random
import pandas as pd

# from time import sleep
from datetime import datetime

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.filepath = {}
        self.filepath = {'gray': savepath2 + 'gray_520.jpg', 'black': savepath2 + 'black.jpg', \
                         'dolphin': savepath2 + 'dolphin_resize.jpg', 'dolphin_outfocus': savepath2 + 'dolphin_out_focus.jpg', \
                         'sparrow': savepath2 + 'sparrow_resize.jpg', 'sparrow_outfocus': savepath2 + 'sparrow_out_focus.jpg', \
                         'sunflower': savepath2 + 'sunflower_resize.jpg', 'sunflower_outfocus': savepath2 + 'sunflower_out_focus.jpg'}

        self.lbl_img = QLabel()
        self.timer = QTimer(self)
        self.refresh_speed = 100
        self.compen_forsec = 1000 / self.refresh_speed
        self.timer.start(100) # refresh 속도 ms
        self.cnt = 0
        self.timer.timeout.connect(self.initUI)
        
        self.present_time = 5 * self.compen_forsec
        self.base_time = 5 * self.compen_forsec
        self.interval_time = 5 * self.compen_forsec

        self.repeat = 40

        self.one_epoch = ((self.present_time*2) + self.interval_time)
        self.total_exp_time =  (self.base_time + (self.one_epoch * self.repeat)) / self.compen_forsec
        
        # print('total_exp_time', total_exp_time, 's')

        self.template = np.array(np.arange(self.base_time, self.total_exp_time*self.compen_forsec, self.one_epoch))

        self.timeline_dice = self.template + (4 * self.compen_forsec)
        self.timeline_present_1 = self.template + (5 * self.compen_forsec)
        self.timeline_present_2 = self.template + (10 * self.compen_forsec)
        self.timeline_present_3  = self.template + (15 * self.compen_forsec)

        self.mssave = []

        self.dice1 = None
        self.dice2 = None
        
        print(self.timeline_dice)

    def initUI(self):
        def msScreenshot(savename):
            myScreenshot = pyautogui.screenshot()
            dt = datetime.today()   
            currenttime = dt.strftime("%Y_%m_%d__%H_%M")
            myScreenshot.save(savepath3 + savename + '_' + currenttime + '.jpg')
        
        if self.cnt == 0:
            pixmap = QPixmap(self.filepath['black'])
            self.lbl_img.setPixmap(pixmap)
            vbox = QVBoxLayout()
            vbox.addWidget(self.lbl_img)
            
            self.setLayout(vbox)
            self.setWindowTitle('QPixmap')
            self.move(0, 0)
            self.show() 
        
        
        if self.cnt in self.timeline_dice:
            self.dice1 = random.randint(0, 2)
            self.dice2 = random.randint(0, 99)
        
        if self.cnt in self.timeline_present_1:
            if self.dice1 == 0:
                pixmap = QPixmap(self.filepath['dolphin'])
                self.lbl_img.setPixmap(pixmap)
                
            elif self.dice1 == 1:
                pixmap = QPixmap(self.filepath['sparrow'])
                self.lbl_img.setPixmap(pixmap)
                
            elif self.dice1 == 2:
                pixmap = QPixmap(self.filepath['sunflower'])
                self.lbl_img.setPixmap(pixmap)
                
            msScreenshot(str(int(self.cnt)))    
            self.mssave.append([self.cnt, self.dice1, 0])
                
        if self.cnt in self.timeline_present_2:
            if self.dice2 < 70:
                if self.dice1 == 0:
                    pixmap = QPixmap(self.filepath['dolphin_outfocus'])
                    self.lbl_img.setPixmap(pixmap)
                    
                elif self.dice1 == 1:
                    pixmap = QPixmap(self.filepath['sparrow_outfocus'])
                    self.lbl_img.setPixmap(pixmap)
                    
                elif self.dice1 == 2:
                    pixmap = QPixmap(self.filepath['sunflower_outfocus'])
                    self.lbl_img.setPixmap(pixmap)
                    
                self.mssave.append([self.cnt, self.dice1, 1])
                
        if self.cnt in self.timeline_present_3:
            # print('interval 화면')
            pixmap = QPixmap(self.filepath['black'])
            self.lbl_img.setPixmap(pixmap)
            self.mssave.append([self.cnt, 9, 2])
            
            dt = datetime.today() 
            currenttime = dt.strftime("%Y_%m_%d__%H_%M")
            pd.DataFrame(self.mssave).to_csv(savepath3 + currenttime + '_mslog.csv')
            
        if self.cnt > (self.total_exp_time * self.compen_forsec) + (5 * self.compen_forsec):
            pixmap = QPixmap(self.filepath['gray'])
            self.lbl_img.setPixmap(pixmap)
            
        if self.cnt > (self.total_exp_time * self.compen_forsec) + (10 * self.compen_forsec):
            sys.exit(app.exec_())
        
        print(self.cnt)
        self.cnt += 1
 
#%%
app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())



















