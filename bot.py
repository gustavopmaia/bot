import pyautogui as p
import time

time.sleep(2)
p.scroll(-600)
p.moveTo(620,893,0)
p.click()
time.sleep(3)
p.click(1142, 687)

time.sleep(2)
p.moveTo(1193, 340)
p.dragTo(1193, 340, button='left')
p.dragTo(1400, 380, 1)
p.hotkey('ctrl', 'c')

time.sleep(2)
p.hotkey('ctrl', '3')
time.sleep(2)
p.moveTo(299, 65)
p.click()
time.sleep(2)
p.hotkey('ctrl', 'v')
p.press('enter')
time.sleep(2)
p.hotkey('ctrl', '2')
time.sleep(2)
p.moveTo(713, 393)
p.click()
p.hotkey('ctrl', 'v')
time.sleep(2)
p.moveTo(908, 385)
p.click()


time.sleep(4)
print(p.position())


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
