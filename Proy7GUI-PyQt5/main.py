# -*- coding: utf-8 -*-

#!/usr/bin/python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self.__init__(parent))

        my_label = QLabel("This is a Label")
        Layout = QVBoxLayout()

        layout.addWidget(my_label)

        mainLayout = QGridLayout()
        mainLayout.addLayout(layout,0,1)

        self.setLayout(mainLayout)
        self.setWindowTitle("My first Qt app")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Page()
    window.show()

    sys.exit(app.exec_())