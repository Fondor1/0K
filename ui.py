__author__ = 'rakai'

from PyQt4 import QtGui, QtCore
import sys


class ItemViewer(QtGui.QWidget):

    def __init__(self):
        super(ItemViewer, self).__init__()
        self.setup_ui()

    def setup_ui(self):

        self.resize(800, 600)
        self.main_layout = QtGui.QVBoxLayout(self)

        self.top_frame = QtGui.QFrame(self)
        self.top_layout = QtGui.QHBoxLayout(self.top_frame)

        self.item_entry = QtGui.QLineEdit()
        self.item_entry.returnPressed.connect(self.item_button_clicked)
        self.item_button = QtGui.QPushButton('Lookup ID')
        self.item_button.clicked.connect(self.item_button_clicked)

        self.top_layout.addWidget(self.item_entry)
        self.top_layout.addWidget(self.item_button)

        self.main_layout.addWidget(self.top_frame)

        self.bottom_frame = QtGui.QFrame(self)
        self.bottom_layout = QtGui.QHBoxLayout(self.bottom_frame)

        self.item_text = QtGui.QTextBrowser()
        self.item_image = QtGui.QGraphicsView()

        item_size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        item_size_policy.setHorizontalStretch(0)
        item_size_policy.setVerticalStretch(0)
        item_size_policy.setHeightForWidth(self.item_image.sizePolicy().hasHeightForWidth())
        self.item_image.setSizePolicy(item_size_policy)

        self.bottom_layout.addWidget(self.item_text)
        self.bottom_layout.addWidget(self.item_image)

        self.main_layout.addWidget(self.bottom_frame)

        self.setWindowTitle('GW2 Item Viewer')
        self.topLevelWidget()

    def item_button_clicked(self):
        # Might want to validate proper inputs here with a regex
        print('clicked lookup button, text is: {}'.format(self.item_entry.text()))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = ItemViewer()
    window.show()
    sys.exit(app.exec_())