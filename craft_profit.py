__author__ = 'rakai'

import sys
from PyQt4 import QtGui, QtCore
from guildwars2api.v2.client import GuildWars2API
from guildwars2api.base import GuildWars2APIError
# import sqlite3


class Item:

    def __init__(self, item):
        for k, v in item.items():
            setattr(self, k, v)


class CraftProfit(QtGui.QWidget):

    def __init__(self):
        super(CraftProfit, self).__init__()

        bank_materials = [item['id'] for item in apiv2.bank_materials.get_all()]
        print(apiv2.items.get(46682))
        self.items = [Item(item) for item in apiv2.items.get(ids=bank_materials)]

        self.setup_ui()

        self.text.setPlainText('\n'.join(str(id) for id in self.bank_materials))

    def setup_ui(self):

        self.main_layout = QtGui.QVBoxLayout(self)

        self.top_frame = QtGui.QFrame(self)
        self.top_layout = QtGui.QHBoxLayout(self.top_frame)

        self.text = QtGui.QPlainTextEdit()

        self.top_layout.addWidget(self.text)

        self.main_layout.addWidget(self.top_frame)

        self.setWindowTitle('GW2 Craft Profit Calculator')
        self.topLevelWidget()



if __name__ == '__main__':

    apiv2 = GuildWars2API(api_key='81668F5F-5866-8F41-81B8-6DF706417B5993297C30-5BAE-44E3-8715-5F94D84AFD8A')

    app = QtGui.QApplication(sys.argv)
    window = CraftProfit()
    window.show()
    sys.exit(app.exec_())
