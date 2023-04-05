from PyQt5.QtWidgets import QMainWindow, QApplication, QAction


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建菜单栏
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        editMenu = menubar.addMenu('Edit')

        # 添加菜单项
        newAction = QAction('New', self)
        fileMenu.addAction(newAction)

        saveAction = QAction('Save', self)
        fileMenu.addAction(saveAction)

        exitAction = QAction('Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        copyAction = QAction('Copy', self)
        editMenu.addAction(copyAction)

        cutAction = QAction('Cut', self)
        editMenu.addAction(cutAction)

        pasteAction = QAction('Paste', self)
        editMenu.addAction(pasteAction)

        # 创建工具栏
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(newAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)

        # 创建中央窗口部件
        self.setCentralWidget(QApplication.desktop())

        # 设置状态栏
        self.statusBar().showMessage('Ready')

        # 设置窗口大小和标题
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('My MainWindow')




if __name__ == '__main__':
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
