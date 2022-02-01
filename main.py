"""
MarketPi (codename)

This is a client for downloading worlds for Minecraft Pi Edition.


MIT License

Copyright (c) 2022 mcpiscript

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import sys
from urllib.request import urlopen
import tempfile



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def url_to_qpixmap(url: str) -> QPixmap:
    image = None
    with tempfile.NamedTemporaryFile(suffix='_tempcache', prefix='marketpi_') as file:
        file.write(urlopen(url).read())
        image = QPixmap(file.name)
    return image 

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        label = QLabel()
        label.setPixmap(url_to_qpixmap("https://github.com/mcpiscript/marketpi-repo/raw/main/worlds/NRC_History/NRC_History.png"))
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
