import glob
import os

uifile = glob.glob('*.ui')
for file in uifile:
    open('./ui_main.py', 'w+').close()
    os.system(f'pyside6-uic {file} > ui_main.py')
