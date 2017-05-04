import subprocess
from PIL import ImageGrab
import cv2
import numpy as np
from numpy import array
import time
import pyautogui
from threading import Timer
from pynput import keyboard
import sys
from PIL import Image
from pytesseract import *

#Open Nox
subprocess.Popen([r'E:\Program Files (x86)\Nox\bin\Nox.exe'])
time.sleep(30)

#Makes Full Screen
try:
    x,y = pyautogui.locateCenterOnScreen('full_screen.png')
    pyautogui.click(x, y)
except:
    print 'Nox didn\'t open'

time.sleep(1)

#Open Endless Frontier
def openGame():
    try:
        x,y = pyautogui.locateCenterOnScreen('endless_frontier.png')
        pyautogui.click(x, y)
        loading = True
        while(loading):
            time.sleep(2)
            try:
                x,y = pyautogui.locateCenterOnScreen('open_game_confirm.png')
                pyautogui.click(x, y)
                loading = False
            except:
                try:
                    x,y = pyautogui.locateCenterOnScreen('open_game_x.png')
                    pyautogui.click(x, y)
                    loading = False
                except:    
                    pass
        time.sleep(3)
        try:
            x,y = pyautogui.locateCenterOnScreen('open_game_x.png')
            pyautogui.click(x, y)
        except:
            pass
    except:
        print 'Endless Frontier didn\'t open'

def closeGame():
    x,y = pyautogui.locateCenterOnScreen('minimize_game.png')
    pyautogui.click(x, y)
    time.sleep(3)
    x,y = pyautogui.locateCenterOnScreen('minimize_game_logo.png')
    pyautogui.mouseDown(x, y, button='left')
    pyautogui.moveRel(-300, 0, 1.5)
    pyautogui.mouseUp(x-300, y, button='left')
    time.sleep(2)
    
class wR():
    arenaBattling = False
    buyingUnits = False
    upgradingUnits = False
    xSpeeding = False
    reviving = False
    exiting = False
    questing = False

    autoReviveTimer=0
    upgradeUnitTimer=0
    buyUnitTimer=0
    arenaBattleTimer=0
    openChestsTimer=0
    xSpeedTimer=0
    autoQuestTimer = 0

    def startTimer(self):
        self.autoReviveTimer = Timer(15, autoRevive)
        self.autoReviveTimer.start()
        self.upgradeUnitTimer = Timer(60, upgradeUnit)
        self.upgradeUnitTimer.start()
        self.buyUnitTimer = Timer(30, buyUnit)
        self.buyUnitTimer.start()
        self.arenaBattleTimer = Timer(20, arenaBattle)
        #The auto Arena sometimes spent gems so I disabled it remove # to have it auto run
        #self.arenaBattleTimer.start()
        self.openChestsTimer = Timer(5, openChests)
        self.openChestsTimer.start()
        self.xSpeedTimer = Timer(5, xSpeed)
        self.xSpeedTimer.start()
        self.autoQuestTimer = Timer(30, autoQuest)
        self.autoQuestTimer.start()

    def stopTimer(self):
        self.autoReviveTimer.cancel()
        self.upgradeUnitTimer.cancel()
        self.buyUnitTimer.cancel()
        self.arenaBattleTimer.cancel()
        self.openChestsTimer.cancel()
        self.xSpeedTimer.cancel()
        self.autoQuestTimer.cancel()

w=wR()
       
def arenaBattle():
    if(wR.exiting):
        return
    wR.arenaBattling = True
    if(not wR.buyingUnits and not wR.upgradingUnits and not wR.xSpeeding and not wR.reviving and not wR.questing):
        print 'Battling in Arena'
        pyautogui.click(1083, 991)#Clicks battle
        time.sleep(2)
        pyautogui.click(1147, 589)#Enters Battle Arena
        try:
            x,y = pyautogui.locateCenterOnScreen('battle_arena_confirm.png')
            pyautogui.click(x, y)
            time.sleep(1)
            pyautogui.click(706, 992)#Back to quests
            wR.arenaBattling = False
            wR.arenaBattleTimer = Timer(60*30, arenaBattle)
            wR.arenaBattleTimer.start()
        except:
            pass
        time.sleep(2)
        while(wR.arenaBattling):
            try:
                time.sleep(5)
                x,y = pyautogui.locateCenterOnScreen('0_battle.png')
                print 'zero battles'
                pyautogui.click(1189, 222)#Hits x
                time.sleep(2)
                pyautogui.click(706, 992)#Back to quests
                wR.arenaBattling = False
                wR.arenaBattleTimer = Timer(60*30, arenaBattle)
                wR.arenaBattleTimer.start()
            except:
                pyautogui.click(1066, 880)#Hits Battle
                battling = True
                while(battling):
                    time.sleep(2)
                    try:
                        x,y = pyautogui.locateCenterOnScreen('battle_arena_confirm.png')
                        pyautogui.click(x, y)#Hits Confirm
                        time.sleep(1)
                        battling = False
                    except:
                        pass
                    try:
                        x,y = pyautogui.locateCenterOnScreen('battle_arena_confirm2.png')
                        pyautogui.click(x, y)#Hits Confirm
                        time.sleep(1)
                        battling = False
                    except:
                        pass
        print 'Finished Battling in Arena'          
    else:
        wR.arenaBattleTimer = Timer(20, arenaBattle)
        wR.arenaBattleTimer.start()    
        
def buyUnit():
    if(wR.exiting):
        return
    wR.buyingUnits = True
    if(not wR.arenaBattling and not wR.upgradingUnits and not wR.xSpeeding and not wR.reviving and not wR.questing):
        print 'Buying Units' 
        pyautogui.click(800, 1000)#Clicks unit
        time.sleep(1)
        pyautogui.click(1141, 508)#Clicks buy unit
        try:
            x,y = pyautogui.locateCenterOnScreen('refresh_unit.png')
            pyautogui.click(x, y)
            try:
                x,y = pyautogui.locateCenterOnScreen('cacel.png')
                pyautogui.click(x, y)
            except:
                pass
            for i in xrange(4):
                print 'Bought Unit:', i+1
                time.sleep(3)
                x,y = pyautogui.locateCenterOnScreen('unit_medal.png')
                pyautogui.click(x, y)
                time.sleep(1)
                pyautogui.click(928, 720)#Send unit to time shop
            
            wR.buyUnitTimer = Timer(3600, buyUnit)
            wR.buyUnitTimer.start()
        except:
            wR.buyUnitTimer = Timer(60, buyUnit)
            wR.buyUnitTimer.start()
            print 'Units not ready'
        time.sleep(1)    
        pyautogui.click(706, 992)#Back to quests
        print 'Finsihed buying Units'
    else:
        buyUnitTimer = Timer(20, buyUnit)
        buyUnitTimer.start()    
    wR.buyingUnits=False

def upgradeUnit():
    if(wR.exiting):
        return
    if(not wR.arenaBattling and not wR.buyingUnits and not wR.xSpeeding and not wR.reviving and not wR.questing):
        wR.upgradingUnits = True
        print 'Upgrading Units'
        pyautogui.click(800, 1000)#Clicks Unit
        for a in xrange(3):
            for b in xrange(2):
                time.sleep(.1)
                for i in pyautogui.locateAllOnScreen('coin.png'):
                    pyautogui.click(i[0], i[1], clicks=4, interval = .02)
            time.sleep(2.5)        
            pyautogui.moveTo(920,730)            
            pyautogui.dragRel(0, -450, .7, button='left')
            time.sleep(.5)
        for c in xrange(4):    
            pyautogui.moveTo(920,550)
            pyautogui.dragRel(0, 300, .7, button='left')
        time.sleep(.5)
        try:
            x,y = pyautogui.locateCenterOnScreen('x.png')
            pyautogui.click(x, y)#Back to quests
        except:
            pass
        pyautogui.click(706, 992)#Back to quests
        wR.upgradeUnitTimer = Timer(120, upgradeUnit)
        wR.upgradeUnitTimer.start()
        print 'Finished Upgrading Units'    
    else:
        wR.upgradeUnitTimer = Timer(20, upgradeUnit)
        wR.upgradeUnitTimer.start()
    wR.upgradingUnits = False    

def upgradeInitialQuests():
    for i in xrange(7):
        pyautogui.mouseDown(920, 650, button='left')
        pyautogui.moveRel(0, 400, .3)
        pyautogui.mouseUp(920, 650, button='left')
    for i in xrange(30):
        for x in pyautogui.locateAllOnScreen('coin.png'):
            if x[1] > 550: 
                pyautogui.click(x[0]+10, x[1]+10)
        pyautogui.mouseDown(920, 650, button='left')
        pyautogui.moveRel(0, -135, .3)
        pyautogui.mouseUp(920, 650, button='left')
        time.sleep(2)
        try:
            x,y = pyautogui.locateCenterOnScreen('unit_confirm.png')
            pyautogui.click(x, y)
        except:
            pass
    for i in xrange(23):
        time.sleep(.1)
        pyautogui.click(1144, 516)
    try:    
        x,y = pyautogui.locateCenterOnScreen('unit_confirm.png')
        pyautogui.click(x, y)
    except:
        pass
    try:
        x,y = pyautogui.locateCenterOnScreen('discover_omen_diamonds.png')
    except:
        try:
            x,y = pyautogui.locateCenterOnScreen('dispatch_omen_diamonds.png')
        except:
            try:
                x,y = pyautogui.locateCenterOnScreen('archdragon_diamonds.png')
            except:
                upgradeInitialQuests()

def openChests():
    if(wR.exiting):
        return
    time.sleep(.02)
    if(not wR.buyingUnits and not wR.upgradingUnits and not wR.arenaBattling and not wR.xSpeeding and not wR.reviving and not wR.reviving):
        pyautogui.click(950, 360)#Clicks for chests
    try:
        x,y = pyautogui.locateCenterOnScreen('view_ad.png')
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.click(947, 713)#Hits confirm button
    except:
        pass
        #print 'No Ad'
    wR.openChestsTimer = Timer(.05, openChests)    
    wR.openChestsTimer.start()

def xSpeed():
    if(wR.exiting):
        return
    if(not wR.buyingUnits and not wR.upgradingUnits and not wR.arenaBattling and not wR.reviving and not wR.questing):
        wR.xSpeeding = True
        pyautogui.click(1180, 984)#opens shop
        time.sleep(1)
        try:
            x,y = pyautogui.locateCenterOnScreen('view_ad2.png')
            pyautogui.click(x, y)
            time.sleep(3)
            x,y = pyautogui.locateCenterOnScreen('shop_confirm.png')
            pyautogui.click(x, y)
            time.sleep(1)
            wR.xSpeedTimer = Timer(5*60, xSpeed)
            wR.xSpeedTimer.start()
        except:
            wR.xSpeedTimer = Timer(60, xSpeed)
            wR.xSpeedTimer.start()
        pyautogui.click(706, 992)#Back to quests
        wR.xSpeeding = False
    else:
        wR.xSpeedTimer = Timer(60, xSpeed)
        wR.xSpeedTimer.start()

def autoQuest():
    if wR.exiting:
        return
    if(not wR.buyingUnits and not wR.upgradingUnits and not wR.arenaBattling and not wR.xSpeeding and not wR.reviving and not wR.reviving):
        wR.questing = True
        pyautogui.click(706, 992)#Back to quests
        for x in xrange(2):
            time.sleep(.2)
            for i in pyautogui.locateAllOnScreen('coin.png'):
                pyautogui.click(i[0]+10, i[1]+10, clicks=4, interval = .02)
        try:
            x,y = pyautogui.locateCenterOnScreen('auto_quest_confirm.png')
            pyautogui.click(x, y)
        except:
            pass
        time.sleep(.5)
        wR.questing = False
    wR.autoQuestTimer = Timer(20, autoQuest)
    wR.autoQuestTimer.start()        

def autoRevive():
    if(wR.exiting):
        return
    if(not wR.buyingUnits and not wR.upgradingUnits and not wR.arenaBattling and not wR.xSpeeding and not wR.questing):
        wR.reviving = True
        try:
            level = ImageGrab.grab(bbox=(925,38,969,62))
            text = int(image_to_string(level))
            print 'Checking Level'
            print 'You are at level', text
            if text >= 4300:
                print 'Reviving at level', text
                pyautogui.click(800, 1000)#Clicks Unit
                time.sleep(1)
                x,y = pyautogui.locateCenterOnScreen('revive.png')
                print 1
                pyautogui.click(x, y)
                time.sleep(1)
                x,y = pyautogui.locateCenterOnScreen('revive.png')
                print 2
                pyautogui.click(x, y)
                time.sleep(1)
                x,y = pyautogui.locateCenterOnScreen('revival_team.png')
                print 3
                pyautogui.click(x, y)
                time.sleep(15)
                x,y = pyautogui.locateCenterOnScreen('battle_arena_confirm.png')
                print 4
                pyautogui.click(x, y)
                time.sleep(1)
                closeGame()
                openGame()
                upgradeInitialQuests()      
        except:
            pass
        wR.reviving = False    
    wR.autoReviveTimer = Timer(60, autoRevive)
    wR.autoReviveTimer.start()

openGame()
#upgradeInitialQuests()
w.startTimer()
       
def on_press(key):
    if key == keyboard.KeyCode.from_char('p'):
        wR.exiting = not wR.exiting
        if wR.exiting:
            w.stopTimer()
            print 'Pausing'
        else:
            print 'UnPausing'
            w.startTimer()
    if key == keyboard.KeyCode.from_char('e'):
        print 'Exiting'
        #stopTimer()
        wR.exiting=True
        sys.exit()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


    
