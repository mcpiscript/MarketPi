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
import random



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from jsonparser import get_world_list



def url_to_qpixmap(url: str,  filename: str) -> QPixmap:
    """
    This function downloads an image from the URL you pass it. 
    It then saves it into a temporary file and returns a QPixmap loaded from that temporary file. 
    The temporary file is then deleted
    """
    
    image = None
    
    user = os.getenv("USER")
    
    with open(f"/home/{USER}/.marketpi/cache/{filename}.png") as file:
        file.write(urlopen(url).read())
        image = QPixmap(file.name)
        
    return image.scaled(100,100, Qt.KeepAspectRatio)
    
    
class QWorldDownloadWidget(QWidget):
    def __init__(self, name: str  = "NRC_History",  baseurl: str = "https://github.com/mcpiscript/marketpi-repo/raw/stable/"):
        super().__init__()
        layout = QGridLayout()
        
        label = QLabel()
        label.setStyleSheet(f"background-image : url({baseurl+name})")
        label.setText("          ")
        #label.setPixmap(url_to_qpixmap(baseurl + f"worlds/shots/scaled/{name}.png"))
        print(f"Downloaded image {name}")
        button = QPushButton("Download")
        if random.randint(0, 100) == 69: # hehe
            button.setIcon(QIcon("assets/icons/download-linux.png"))
        else:
            button.setIcon(QIcon("assets/icons/drive-download.png"))
        
        layout.addWidget(label,  0, 0)
        layout.addWidget(button, 0, 1)
        
        self.setLayout(layout)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        central = QWidget()
        
        centrallayout = QStackedLayout()
        
        mapwidget = QWidget()

        self.setWindowTitle("MarketPi")
        
        contenttabs = QTabWidget()
        
        contenttabs.setTabPosition(QTabWidget.West)
        contenttabs.setMovable(False)
        
        scroll = QScrollArea()
        
        maplayout = QGridLayout()
        
        #epic for loop going through all json entries here plz
        worldloop = 0
        
        print("getting the world list")
        
        worldlist = get_world_list("https://github.com/mcpiscript/marketpi-repo/raw/stable/worlds/worlds.json")
        random.shuffle(worldlist)
        
        for world in worldlist:
            print("adding world " + world["codename"])
            worldloop += 1
            maplayout.addWidget(QWorldDownloadWidget(world["codename"]), worldloop,  0)
            if worldloop == 7:
                break

        
        mapwidget.setLayout(maplayout)
        
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(mapwidget)
        
        contenttabs.addTab(scroll,  "Worlds")
        
        centrallayout.addWidget(contenttabs)
        
        centrallayout.setCurrentIndex(0)
        
        central.setLayout(centrallayout)
        
        
        
        self.setCentralWidget(central)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
