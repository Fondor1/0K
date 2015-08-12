__author__ = 'rakai'

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtWebKit import QWebView
from guildwars2api.v2.client import GuildWars2API
from guildwars2api.base import GuildWars2APIError


class ItemViewer(QtGui.QWidget):

    def __init__(self):
        super(ItemViewer, self).__init__()
        self.apiv2 = GuildWars2API(api_key='81668F5F-5866-8F41-81B8-6DF706417B5993297C30-5BAE-44E3-8715-5F94D84AFD8A')
        self.setup_ui()

    def setup_ui(self):

        # self.resize(800, 600)
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

        self.item_webview = QWebView()

        self.bottom_layout.addWidget(self.item_webview)
        self.bottom_frame.setHidden(True)

        self.main_layout.addWidget(self.bottom_frame)

        self.setWindowTitle('GW2 Item Viewer')
        self.topLevelWidget()

    def item_button_clicked(self):
        head = body = ''
        try:
            item = self.apiv2.items.get(id=self.item_entry.text())
        except GuildWars2APIError as e:
            body = '<p>{}</p>'.format(e)
        else:
            for key in item:
                # Do some formatting, cull out useless ones
                if key == 'icon':
                    # If it's the image, set it up to display properly
                    item[key] = '<img src="'+item[key]+'">'
                elif key == 'restrictions':
                    item[key] = ''
                elif key == 'description':
                    item[key] = ''
                elif key == 'details':
                    item[key] = ''
                elif key == 'game_types':
                    item[key] = ''
                elif key == 'default_skin':
                    item[key] = ''
                elif key == 'flags':
                    item[key] = ''

            head = '<html><head><style>body{font-family:sans-serif}</style></head>'
            body = '<body><table>'+''.join('<tr><td>{0}</td><td>{1}</td></tr>'.format(k, v)
                                           for k, v in item.items() if v != '')+'</table></body></html>'
        self.item_webview.setHtml(head+body)

        # Show the results if it's the first run
        if self.bottom_frame.isHidden():
            self.bottom_frame.setHidden(False)
            self.resize(800, 600)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = ItemViewer()
    window.show()
    sys.exit(app.exec_())