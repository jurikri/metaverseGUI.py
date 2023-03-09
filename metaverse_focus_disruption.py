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
            savepath2 = savepath + '\\screenshot_save\\'
            dt = datetime.today()   
            currenttime = dt.strftime("%Y_%m_%d__%H_%M")
            myScreenshot.save(savepath2 + savename + '_' + currenttime + '.jpg'
                                                
        if self.cnt in self.timeline_dice:
            self.dice1 = random.randint(0, 2)
            self.dice2 = random.randint(0, 1)
        
        if self.cnt in self.timeline_present_1:
            if self.dice1 == 0:
                print('첫 화면', '랜덤 1')
            elif self.dice1 == 1:
                print('첫 화면', '랜덤 2') 
            elif self.dice1 == 2:
                print('첫 화면', '랜덤 3')     
            self.mssave.append([self.cnt, self.dice1])
                
        if self.cnt in self.timeline_present_2:
            if self.dice2 == 1:
                if self.dice1 == 0:
                    print('두번째 화면', '랜덤 1')
                elif self.dice1 == 1:
                    print('두번째 화면', '랜덤 2') 
                elif self.dice1 == 2:
                    print('두번째 화면', '랜덤 3')   
                self.mssave.append([self.cnt, self.dice1])
                
        if self.cnt in self.timeline_present_3:
            print('interval 화면')
            self.mssave.append([self.cnt, 'interval'])
        
        print(self.cnt)
        self.cnt += 1
 
#%%
app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())

#%%


cnt = 10

(cnt - 10) % 36 == 10


#%%

import numpy as np
from PIL import Image
savepath = 'C:\\SynologyDrive\\worik in progress\\metaverse_project\\metaverse_focus_disruption\\'


filepath = {}
filepath = {'black': savepath + 'black_size.png', 'blue': savepath + 'blue_size.png', \
                 'red': savepath + 'red_size.png', 'green': savepath + 'green_size.png', 'gray': savepath + 'gray_size.png'}

refresh_speed = 100
compen_forsec = 1000 / refresh_speed

present_time = 5 * compen_forsec
base_time = 5 * compen_forsec
interval_time = 5 * compen_forsec

repeat = 40

one_epoch = ((present_time*2) + interval_time)
total_exp_time =  (base_time + (one_epoch * repeat)) / compen_forsec

print('total_exp_time', total_exp_time, 's')

template = np.array(np.arange(base_time, total_exp_time*compen_forsec, one_epoch))

timeline_dice = template + (4 * compen_forsec)
timeline_present_1 = template + (5 * compen_forsec)
timeline_present_2 = template + (10 * compen_forsec)
timeline_present_3  = template + (15 * compen_forsec)

mssave = []

for epoch in range(10000):
    
    if epoch in timeline_dice:
        dice1 = random.randint(0, 2)
        dice2 = random.randint(0, 1)
    
    if epoch in timeline_present_1:
        if dice1 == 0:
            print('첫 화면', '랜덤 1')
        elif dice1 == 1:
            print('첫 화면', '랜덤 2') 
        elif dice1 == 2:
            print('첫 화면', '랜덤 3')     
        mssave.append([epoch, dice1])
            
    if epoch in timeline_present_2:
        if dice2 == 1:
            if dice1 == 0:
                print('두번째 화면', '랜덤 1')
            elif dice1 == 1:
                print('두번째 화면', '랜덤 2') 
            elif dice1 == 2:
                print('두번째 화면', '랜덤 3')   
            mssave.append([epoch, dice1])
            
    if epoch in timeline_present_3:
        print('interval 화면')
        mssave.append([epoch, 'interval'])
        
                
                
                
    
            
    
    
    # timer.start(100) # refresh 속도 ms
    # timer.timeout.connect(self.initUI)
    
    base_sec = 5 * compen_forsec

    if cnt == 0:
        print('시작 화면')
        
    elif cnt >= base_sec and dice_ready_1 and (cnt_dice2 >= present_time): # dice 1
    
    
        dice = random.randint(0, 2)
        dice_ready_1 = False
        present_ready_1 = True
        
        cnt_dice2 = 0
        cnt_dice2_clock_sw = False
        
        print('dice 1 ->', dice)
        
    elif cnt >= base_sec and dice_ready_2 and (cnt_dice1 >= present_time): # dice 2
        dice2_1 = random.randint(0, 1)
        dice2_2 = random.randint(0, 2)
        dice_ready_2 = False
        present_ready_2 = True
        
        cnt_dice1 = 0
        cnt_dice1_clock_sw = False
        
        print('dice 2 ->', dice)
        
    elif cnt >= endtime + base_sec:
        # pixmap = QPixmap(filepath['gray'])
        # lbl_img.setPixmap(pixmap)
        ready_1 = False
        
        print('종료 화면')
        
     ##
    if cnt >= base_sec and cnt < endtime + base_sec and not(dice_ready_1) and present_ready_1:
        if dice == 0:
            print('첫 화면', '랜덤 1')
        
        elif dice == 1:
            print('첫 화면', '랜덤 2')
            
        elif dice == 2:
            print('첫 화면', '랜덤 3')
            
        cnt_dice1_clock_sw = True
        cnt_dice1 = 0
        present_ready_1 = False
        dice_ready_2 = True
        
    if cnt_dice1_clock_sw: cnt_dice1 += 1
        
    if cnt >= base_sec and cnt < endtime + base_sec and not(dice_ready_2) and present_ready_2:
        if not(dice2_1 == 0 ):
            if dice2_2 == 0:
                pixmap = QPixmap(filepath['gray'])
                lbl_img.setPixmap(pixmap)
                msScreenshot(str(int(cnt)) + '_red')
            
            elif dice2_2 == 1:
                pixmap = QPixmap(filepath['gray'])
                lbl_img.setPixmap(pixmap)
                msScreenshot(str(int(cnt)) + '_red')
                
            elif dice2_2 == 2:
                pixmap = QPixmap(filepath['gray'])
                lbl_img.setPixmap(pixmap)
                msScreenshot(str(int(cnt)) + '_red')
                
        cnt_dice2_clock_sw = True
        cnt_dice2 = 0
        present_ready_2 = False
        dice_ready_1 = True
                
    if cnt_dice2_clock_sw: cnt_dice2 += 1

            
            

    
        
        
        
    print(cnt)
    cnt += 1





























