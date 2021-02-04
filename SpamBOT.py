#Spam Bot
import pyautogui, time
import keyboard
time.sleep(5)
f = open('Reatrd.txt', 'r')



while keyboard.is_pressed('q') == False:
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(0.5)


quit()  
