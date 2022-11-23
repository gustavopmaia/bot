import pyautogui as p
import time

time.sleep(2)
p.scroll(-600)
move_to_click(620, 893, 0)
time.sleep(2)
p.click(1142, 687)

time.sleep(2)
drag(1193, 340, 1400, 380, 'left')
p.hotkey('ctrl', 'c')

time.sleep(2)
change_tab(3)
time.sleep(2)
move_to_click(299, 65)
time.sleep(2)
copy_paste('v')
p.press('enter')
time.sleep(2)
change_tab(2)
time.sleep(2)
move_to_click(713,393)
copy_paste('v')
time.sleep(2)
move_to_click(908, 385)

def change_tab(tab):
    p.hotkey('ctrl', tab)

def get_position():
    time.sleep(4)
    print(p.position())

# def wait():
#     time.sleep(2)

def copy_paste(key):
    p.hotkey('ctrl', key)

def move_to_click(x, y):
    p.moveTo(x, y)
    p.click()

def drag(x_start, y_start, x_end, y_end, button):
    p.moveTo(x_start, y_start)
    p.dragTo(x_start, y_start, button=button)
    p.dragTo(x_end, _end, 1)  




# Point(x=756, y=391)
# Point(x=1142, y=687)
# Point(x=620, y=893)

# Point(x=283, y=125)
# Point(x=377, y=125)

# VALOR 1: Point(x=1193, y=340)
# VALOR 2: Point(x=1242, y=341)

# VSCODE: Point(x=1059, y=1047)


# SCROLL: Point(x=1911, y=583)

# Point(x=299, y=65)

# Point(x=908, y=385)

# https://medium.com/geekculture/how-to-solve-captcha-with-python-80959653dba2