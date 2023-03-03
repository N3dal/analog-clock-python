#!/usr/bin/python3
# -----------------------------------------------------------------
# simple try to make an analog clock;
#
#
#
# Author:N84.
#
# Create Date:Fri Mar  3 23:29:03 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------


from os import system
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    """
        application main window;
    """

    WIDTH = 300
    HEIGHT = 450
    STYLESHEET = """
        background-color: #f7f7f7;
    """
    TITLE = "Analog Clock"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setWindowTitle(MainWindow.TITLE)
        self.setStyleSheet(MainWindow.STYLESHEET)


def main():
    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
