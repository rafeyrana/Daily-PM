from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QObject, pyqtProperty

class AnimatedTreeWidgetItem(QObject):
    def __init__(self, item):
        super().__init__()
        self._item = item
        self._color = QColor("white")

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
        self._item.setBackground(0, color)
        self._item.setBackground(1, color)
        self._item.setBackground(2, color)
