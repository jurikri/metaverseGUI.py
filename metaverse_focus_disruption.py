# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:49:02 2022

@author: PC
"""

import pyautogui
import numpy as np
from PIL import Image
savepath = 'C:\\SynologyDrive\\worik in progress\\metaverse_project\\metaverse_focus_disruption\\'

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

# from time import sleep
from datetime import datetime

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.filepath = {}
        self.filepath = {'black': savepath + 'black_size.png', 'blue': savepath + 'blue_size.png', \
                         'red': savepath + 'red_size.png', 'green': savepath + 'green_size.png', 'gray': savepath + 'gray_size.png'}
        self.cnt = 0
        self.cnt_dice1 = 0
        self.cnt_dice2 = 999999999999
        self.cnt_dice1_clock_sw = False
        self.cnt_dice2_clock_sw = False
        
        self.lbl_img = QLabel()

        self.timer = QTimer(self)
        self.refresh_speed = 100
        self.compen_forsec = 1000 / self.refresh_speed
        self.timer.start(100) # refresh 속도 ms
        self.timer.timeout.connect(self.initUI)
        
        self.endtime = 360 * self.compen_forsec
        self.present_time = 5 * self.compen_forsec
        
        
        
        self.dice = None
        self.dice2_1 = None
        self.dice2_2 = None
        
        self.present_ready_1 = False
        self.present_ready_2 = False
        
        self.dice_ready_1 = True
        self.dice_ready_2 = False

    def initUI(self):
        def msScreenshot(savename):
            myScreenshot = pyautogui.screenshot()
            savepath2 = savepath + '\\screenshot_save\\'
            dt = datetime.today()   
            currenttime = dt.strftime("%Y_%m_%d__%H_%M")
            myScreenshot.save(savepath2 + savename + '_' + currenttime + '.jpg')
        
        base_sec = 5 * self.compen_forsec

        if self.cnt == 0:
            pixmap = QPixmap(self.filepath['black'])
            
            self.lbl_img.setPixmap(pixmap)
            vbox = QVBoxLayout()
            vbox.addWidget(self.lbl_img)
            
            self.setLayout(vbox)
            self.setWindowTitle('QPixmap')
            self.move(0, 0)
            self.show() 
            
        elif self.cnt >= base_sec and self.dice_ready_1 and (self.cnt_dice2 >= self.present_time): # dice 1
            self.dice = random.randint(0, 2)
            self.dice_ready_1 = False
            self.present_ready_1 = True
            
            self.cnt_dice2 = 0
            self.cnt_dice2_clock_sw = False
            
        elif self.cnt >= base_sec and self.dice_ready_2 and (self.cnt_dice1 >= self.present_time): # dice 2
            self.dice2_1 = random.randint(0, 1)
            self.dice2_2 = random.randint(0, 2)
            self.dice_ready_2 = False
            self.present_ready_2 = True
            
            self.cnt_dice1 = 0
            self.cnt_dice1_clock_sw = False
            
        elif self.cnt >= self.endtime + base_sec:
            pixmap = QPixmap(self.filepath['gray'])
            self.lbl_img.setPixmap(pixmap)
            self.ready_1 = False

         ##
        if self.cnt >= base_sec and self.cnt < self.endtime + base_sec and not(self.dice_ready_1) and self.present_ready_1:
            if self.dice == 0:
                pixmap = QPixmap(self.filepath['red'])
                self.lbl_img.setPixmap(pixmap)
                msScreenshot(str(int(self.cnt)) + '_red')
            
            elif self.dice == 1:
                pixmap = QPixmap(self.filepath['red'])
                self.lbl_img.setPixmap(pixmap)
                msScreenshot(str(int(self.cnt)) + '_red')
                
            elif self.dice == 2:
                pixmap = QPixmap(self.filepath['red'])
                self.lbl_img.setPixmap(pixmap)
                msScreenshot(str(int(self.cnt)) + '_red')
                
            self.cnt_dice1_clock_sw = True
            self.cnt_dice1 = 0
            self.present_ready_1 = False
            self.dice_ready_2 = True
            
        if self.cnt_dice1_clock_sw: self.cnt_dice1 += 1
            
        if self.cnt >= base_sec and self.cnt < self.endtime + base_sec and not(self.dice_ready_2) and self.present_ready_2:
            if not(self.dice2_1 == 0 ):
                if self.dice2_2 == 0:
                    pixmap = QPixmap(self.filepath['gray'])
                    self.lbl_img.setPixmap(pixmap)
                    msScreenshot(str(int(self.cnt)) + '_red')
                
                elif self.dice2_2 == 1:
                    pixmap = QPixmap(self.filepath['gray'])
                    self.lbl_img.setPixmap(pixmap)
                    msScreenshot(str(int(self.cnt)) + '_red')
                    
                elif self.dice2_2 == 2:
                    pixmap = QPixmap(self.filepath['gray'])
                    self.lbl_img.setPixmap(pixmap)
                    msScreenshot(str(int(self.cnt)) + '_red')
                    
            self.cnt_dice2_clock_sw = True
            self.cnt_dice2 = 0
            self.present_ready_2 = False
            self.dice_ready_1 = True
                    
        if self.cnt_dice2_clock_sw: self.cnt_dice2 += 1

                
                

        
            
            
            
        print(self.cnt)
        self.cnt += 1
           
        
#%%
app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())

#%%


cnt = 10

(cnt - 10) % 36 == 10
































