import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # `frameGeometry()`方法返回一个`QRect`对象，该对象包含了窗口在屏幕上的位置和大小信息。
        # `qr`是一个`QRect`对象，表示窗口的几何位置和大小；
        qr = self.frameGeometry()
        """
            qr.moveCenter(cp)这行代码的作用是将qr矩形对象的中心点移动到cp点的位置上。因为cp是屏幕的中心点，所以这样操作可以将窗口的中心点移动到屏幕的中心。
            self.move(qr.topLeft())这行代码的作用是将窗口移动到qr矩形对象的左上角位置。因为上一行代码已经将qr矩形对象的中心点移动到屏幕的中心了，所以这行代码实际上就是将窗口的中心点移动到屏幕的中心。
            因此，这两行代码实现的是将窗口移动到屏幕的中心位置，但是通过不同的方式实现。qr.moveCenter(cp)将窗口的中心点移动到屏幕中心点，然后self.move(qr.topLeft())将窗口的左上角移动到窗口中心点所在的位置，使得窗口居中显示。
        """
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
