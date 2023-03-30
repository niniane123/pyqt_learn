from PyQt5.QtWidgets import QApplication

from tetris import Tetris
import sys

if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
