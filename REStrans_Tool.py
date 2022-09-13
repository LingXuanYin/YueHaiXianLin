import glob
import os

uifile = glob.glob('*.qrc')
for file in uifile:
    open('./ui_main.py', 'w+').close()
    os.system(f'pyside6-rcc {file} -o resources_rc.py')
