import pyautogui
import time

pyautogui.PAUSE = 0.5

#ABRIR CRHOME
pyautogui.click(x=799,y=1068, button='right')
time.sleep(2)
pyautogui.click(x=785,y=967)

#ENTRAR NO SITE
pyautogui.write("https://docs.google.com/forms/d/1BuF8NmEFgT5mS6HJudUhmqalD_1dH5yJIR6cRPDZTek/preview")
pyautogui.press('enter')
time.sleep(4)

#EMAIL
pyautogui.click(x=243,y=413)
pyautogui.write("EduardoKlitzke@gmail.com")

#NUMERO
pyautogui.click(x=228,y=564)
pyautogui.write("27988784048")

#SALVAR
pyautogui.click(x=206,y=709)


