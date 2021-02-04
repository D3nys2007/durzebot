#Spam Bot
import pyautogui, time
import keyboard
time.sleep(5)
text = input('enter you desired file name with your spam text\nMAke Sure To Put .txt at the end:\n')
f = open(text, 'r')



while keyboard.is_pressed('q') == False:
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
        time.sleep(0.5)


quit()  
