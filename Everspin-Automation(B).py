# pip install keyboard
# pip install schedule

import pyautogui
import time
import PySimpleGUI as sg
import keyboard as key
import schedule

# Relog Page 1
pyautogui.click(67, 10)
pyautogui.press("F5")
time.sleep(3)
pyautogui.click(580, 420)
key.write('qwe123Q!')
pyautogui.click(580, 500)
# tab 1
pyautogui.click(67, 10)
time.sleep(10)
pyautogui.press("printscreen")
pyautogui.click(1000, 10)
pyautogui.hotkey("ctrlleft", "v")
time.sleep(1)
# tab 2
pyautogui.click(320, 10)
pyautogui.press("F5")
time.sleep(7)
pyautogui.press("printscreen")
pyautogui.click(1000, 10)
pyautogui.hotkey("ctrlleft", "v")
time.sleep(1)
# tab 3
pyautogui.click(510, 10)
time.sleep(1)
pyautogui.press("printscreen")
pyautogui.click(1000, 10)
pyautogui.hotkey("ctrlleft", "v")
time.sleep(1)
# tab 3
pyautogui.click(650, 10)
time.sleep(1)
pyautogui.press("printscreen")
pyautogui.click(1000, 10)
pyautogui.hotkey("ctrlleft", "v")
time.sleep(1)
# tab 4
pyautogui.click(802, 10)
time.sleep(1)
pyautogui.press("printscreen")
pyautogui.click(1000, 10)
pyautogui.hotkey("ctrlleft", "v")
time.sleep(1)


def Lanjutkan():
    window1.Close()
    time.sleep(4)
    pyautogui.press("enter")
    # time.sleep(3000)
    time.sleep(15)
    layout2 = [[sg.Text(
        'Yuk Report', font='Default 30')]]

    # Create the window
    window2 = sg.Window("Continuous", layout2)
    window2.Finalize()
    window2.TKroot.focus_force()
    window2.Read()


sg.theme('BluePurple')
layout1 = [
    [sg.Text('Apakah Anda Yakin Tuan ?\n Klik Benar Jika Melanjutkan Tuan',
             font='Default 30')],
    [sg.Button('Benar!'), sg.Button('Cancel')]

]
window1 = sg.Window('Automation-B-', layout1, grab_anywhere=False, size=(
    800, 480), return_keyboard_events=True, finalize=True)

window1.BringToFront()
while True:
    event, values = window1.read()
    if event in (None, 'Cancel'):
        sg.Popup('Yaudah kalau ga jadi', '')
        break
    else:
        Lanjutkan()

# schedule.every(3000).seconds.dp(Capture)
