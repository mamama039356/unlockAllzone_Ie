import os
import pyautogui
import time
import selenium import webdriver

def recognition():
	icon_internet = "C:/Users/190214/myProgram/unlockSafety/includes/internet.png
	icon_local = "C:/Users/190214/myProgram/unlockSafety/includes/local.png"
	icon_rely = "C:/Users/190214/myProgram/unlockSafety/includes/ok.png"

	pos_internet = pyautogui.locateCenterOnScreen(icon_internet)
	print(pos_internet)
	pos_local = pyautogui.locateCenterOnScreen(icon_local)
	print(pos_local)
	pos_rely = pyautogui.locateCenterOnScreen(icon_rely)
	print(pos_rely)
	return pos_internet, pos_local, pos_rely
	
def auto():
	pyautogui.hotkey("alt", "t")
	pyautogui.press("o")
	time.sleep(1)
	pyautogui.hotkey("ctrl", "tab")
	# recognition
	pos_internet, pos_local, pos_rely = recognition()
	# internet
	if (pos_internet == None or pos_rely == None):
		pyautogui.click(pos_local)
	pyautogui.press("tab")
	pyautogui.press("tab")
	pyautogui.press("space")
	# rely
	pyautogui.click(pos_rely)
	pyautogui.press("tab")
	pyautogui.press("tab")
	pyautogui.press("space")
	pyautogui.press("enter")
	
if __name__ == "__main__":
	ie = C:/Users/190214/IEDriverServer.exe"
	try:
		driver=webdriver.Ie(ie)
	except:
		pyautogui.hotkey("win", "3")
		time.sleep(4)
		auto()
		driver.close()
