import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        newAction = QAction('New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.newFile)
        fileMenu.addAction(newAction)

        saveAction = QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        editMenu = menubar.addMenu('Edit')

        copyAction = QAction('Copy', self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.triggered.connect(self.copyText)
        editMenu.addAction(copyAction)

        pasteAction = QAction('Paste', self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.triggered.connect(self.pasteText)
        editMenu.addAction(pasteAction)

        viewMenu = menubar.addMenu('View')

        zoomInAction = QAction('Zoom In', self)
        zoomInAction.setShortcut('Ctrl++')
        zoomInAction.triggered.connect(self.zoomIn)
        viewMenu.addAction(zoomInAction)

        zoomOutAction = QAction('Zoom Out', self)
        zoomOutAction.setShortcut('Ctrl+-')
        zoomOutAction.triggered.connect(self.zoomOut)
        viewMenu.addAction(zoomOutAction)

        helpMenu = menubar.addMenu('Help')

        aboutAction = QAction('About', self)
        aboutAction.triggered.connect(self.about)
        helpMenu.addAction(aboutAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QMenu and QAction Example')
        self.show()

    def newFile(self):
        print('New File')

    def saveFile(self):
        print('Save File')

    def copyText(self):
        print('Copy Text')

    def pasteText(self):
        print('Paste Text')

    def zoomIn(self):
        print('Zoom In')

    def zoomOut(self):
        print('Zoom Out')

    def about(self):
        print('About')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
