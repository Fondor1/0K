__author__ = 'rakai'

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In this program, we can press on a button
with a left mouse click or drag and drop the
button with  the right mouse click.

author: Jan Bodnar
website: zetcode.com
last edited: October 2013
"""

import sys
from PyQt4 import QtCore, QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)

        self.main_layout = QtGui.QVBoxLayout(self)
        self.setLayout(self.main_layout)


        # Set up the top section
        self.top_frame = QtGui.QFrame(self)
        self.top_frame.setFrameStyle(6)
        self.top_layout = QtGui.QVBoxLayout(self.top_frame)

        self.add_button = QtGui.QPushButton('Add')
        self.add_button.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum))
        self.add_button.clicked.connect(self.add)
        self.delete_button = QtGui.QPushButton('Remove')
        self.delete_button.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum))
        self.delete_button.clicked.connect(self.delete)
        self.top_layout.addWidget(self.add_button)
        self.top_layout.addWidget(self.delete_button)

        # Set up the bottom section
        self.bottom_frame = QtGui.QGraphicsView(self)
        self.bottom_frame.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding))
        self.bottom_frame.setScene(QtGui.QGraphicsScene())
        self.bottom_layout = QtGui.QVBoxLayout(self.bottom_frame)

        item = self.bottom_frame.scene().addPixmap(QtGui.QPixmap(r'E:\Project Directory\0K\trunk\resource\GuildSymbol.png'))
        item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

        # Combine everything into the main widget
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)

        self.setWindowTitle('Move')
        self.setGeometry(300, 300, 480, 350)
        self.topLevelWidget()


    def add(self):
        item = self.bottom_frame.scene().addPixmap(QtGui.QPixmap(r'E:\Project Directory\0K\trunk\resource\larry_the_cow-full.png'))
        item.setFlag(QtGui.QGraphicsItem.ItemIsMovable)

    def delete(self):
        print(self.bottom_frame.items()[-1])
        self.bottom_frame.scene().removeItem(self.bottom_frame.items()[-1])

def main():

    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()