from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel

class DiffView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel("Diff View")
        self.layout.addWidget(self.label)

        self.diff_text = QTextEdit()
        self.diff_text.setReadOnly(True)
        self.layout.addWidget(self.diff_text)

    def display_diff(self, diff):
        self.diff_text.setText(diff)
