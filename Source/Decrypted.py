import subprocess
from tkinter import *
import sys
import webbrowser
import time
import os
import urllib.request

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)
path = 'rickroll.jpg'

with urllib.request.urlopen('https://i.ibb.co/jWvQKpJ/rickroll-4k.jpg') as response:
    content = response.read()
    file = open(path, "wb")
    file.write(content)
    file.close()

try:
    import ctypes
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, os.path.join(desktop, path), 3)
except:
    pass  # In case the user is not on windows

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
for i in range(10):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

for i in range(70):
    with open(f'index{i}.html', 'w') as file:
        file.write("""<iframe width="100%" height="100%" src="https://www.youtube.com/embed/GtL1huin9EE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>""")

for i in range(15):
    root = Tk()
    root.geometry('650x650')
    root.title('Never gonna give you up Lyrics')
    a = Label(root, text="""
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you
    """, font=('Arial', 20), anchor='w', justify=LEFT).pack()
    root.mainloop()

subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQt5'])
subprocess.check_call([sys.executable, "-m", "pip", "install", 'PyQtWebEngine'])

from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(
            QUrl('https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


app = QApplication(sys.argv)
QApplication.setApplicationName('You have been rickrolled')
for i in range(15):
    window = MainWindow()
    app.exec_()
