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
from math import (sin, cos, pi)
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from random import randint


class MainWindow(QMainWindow):
    """
        application main window;
    """

    WIDTH = 380
    HEIGHT = 450
    STYLESHEET = """
        background-color: #282828;
    """

    CANVAS_BACKGROUND_COLOR = QColor(247, 247, 247, 255)
    CANVAS_STYLESHEET = """
        background-color: #f7f7f7;
    """
    TITLE = "Analog Clock"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setWindowTitle(MainWindow.TITLE)
        self.setStyleSheet(MainWindow.STYLESHEET)

        self.canvas = QPixmap(MainWindow.WIDTH - 20, MainWindow.HEIGHT - 100)
        self.canvas.fill(MainWindow.CANVAS_BACKGROUND_COLOR)

        self.label = QLabel(parent=self)
        self.label.setPixmap(self.canvas)
        self.label.setFixedSize(MainWindow.WIDTH, 400)
        self.label.move(10, 10)

        self.__seconds_degree = 0
        self.__minutes_degree = 0
        self.__hours_degree = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(250)

        self.draw_clock_frame()
        self.tick()

    def draw_clock_frame(self):
        """
            draw the circle frame and the numbers;
            and draw the center dot of the clock;

            return None;
        """

        # the frame circle radius
        RADIUS = 300

        # the numbers circle radius;
        NUMBER_RADIUS = RADIUS - 30

        # first draw the frame;
        pen = QPen()
        pen.setWidth(4)
        painter = QPainter(self.label.pixmap())
        painter.setPen(pen)
        painter.drawEllipse((self.canvas.width() - RADIUS) // 2,
                            (self.canvas.height() - RADIUS) // 2, RADIUS, RADIUS)

        # second draw the numbers;
        font = QFont()
        font.setBold(True)
        font.setPointSize(20)
        painter.setFont(font)

        deg = 0
        hour = 3

        for _ in range(12):
            # now draw the hours;

            if hour > 12:
                hour = 1

            painter.drawText(int(NUMBER_RADIUS//2 * cos(deg * pi / 180)) + (NUMBER_RADIUS + 75) // 2,
                             int(NUMBER_RADIUS//2 * sin(deg * pi / 180)) + (NUMBER_RADIUS + 100) // 2, f"{hour}")
            deg += 30
            hour += 1

        # first draw the frame;
        center_pen = QPen()
        center_pen.setWidth(8)
        center_pen.setColor(Qt.red)
        painter.setPen(center_pen)
        painter.drawEllipse((self.canvas.width() - RADIUS) // 2 + RADIUS//2,
                            (self.canvas.height() - RADIUS) // 2 + RADIUS//2,
                            5,
                            5)

        painter.end()

        return None

    def draw_line(self, degree: int, shifting: int = 0):
        """
            draw the line for clock wise.

            return None;
        """

        # Convert the degree into radians;
        degree *= (pi / 180)

        WISE_LENGTH = 150

        circle_center_x = self.canvas.width() // 2
        circle_center_y = self.canvas.height() // 2

        pen = QPen()
        pen.setWidth(4)
        painter = QPainter(self.label.pixmap())
        painter.setPen(pen)

        # debug;
        x2 = circle_center_x - int(WISE_LENGTH * cos(degree)) + shifting
        y2 = circle_center_y - int(WISE_LENGTH * sin(degree)) + shifting
        print(f"{x2=}, {y2=}")

        painter.drawLine(x2, y2, circle_center_x +
                         3, circle_center_y + 3)

        painter.end()

        return None

    def clear_canvas(self):
        """
            clear the canvas and fill it with the basic color;

            return None;
        """

        self.label.pixmap().fill(MainWindow.CANVAS_BACKGROUND_COLOR)

        return None

    def tick(self):
        """
            timeout event when the timer get 1 second;

            return None;
        """
        print("Tick!!")

        # in every tick we need to clear the main canvas;
        self.clear_canvas()

        # then we need to re-draw the main clock frame;
        self.draw_clock_frame()

        self.draw_line(self.__seconds_degree, shifting=10)
        self.draw_line(self.__minutes_degree, shifting=5)
        self.draw_line(self.__hours_degree, shifting=30)

        self.__seconds_degree += 6

        if self.__seconds_degree > 360:
            self.__seconds_degree = 0
            self.__minutes_degree += 6

        if self.__minutes_degree > 360:
            self.__minutes_degree = 0
            self.__hours_degree += 30

        # update the main window so the changes will appear;
        self.update()
        return None


def main():
    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
