import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Git Explorer")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Create the three-pane layout
        splitter = QSplitter(Qt.Horizontal)

        # Left pane: Repository and file explorer
        from .repo_explorer import RepoExplorer
        repo_file_explorer = RepoExplorer()

        # Middle pane: Commit history and git graph
        from .commit_view import CommitView
        commit_view = CommitView()

        # Right pane: Diff view
        from .diff_view import DiffView
        diff_view = DiffView()

        splitter.addWidget(repo_file_explorer)
        splitter.addWidget(commit_view)
        splitter.addWidget(diff_view)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        splitter.setStretchFactor(2, 2)

        main_layout.addWidget(splitter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
