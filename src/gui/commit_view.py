from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import plotly.graph_objects as go

class CommitView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel("Commit History")
        self.layout.addWidget(self.label)

        self.commit_tree = QTreeWidget()
        self.commit_tree.setHeaderLabels(["Date", "Author", "Message"])
        self.layout.addWidget(self.commit_tree)

        self.git_graph = QWebEngineView()
        self.layout.addWidget(self.git_graph)

    def display_commits(self, commits):
        self.commit_tree.clear()
        for commit in commits:
            item = QTreeWidgetItem(self.commit_tree)
            item.setText(0, commit['date'])
            item.setText(1, commit['author'])
            item.setText(2, commit['message'])

    def display_git_graph(self, commits):
        # This is a placeholder for the git graph generation
        fig = go.Figure()
        for i, commit in enumerate(commits):
            fig.add_trace(go.Scatter(x=[i], y=[0], mode='markers', name=commit['message']))

        self.git_graph.setHtml(fig.to_html(include_plotlyjs='cdn'))
