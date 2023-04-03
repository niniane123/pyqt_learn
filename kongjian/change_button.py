from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        """
            在 PyQt 中，QPushButton 组件有两种状态：选中状态和未选中状态。默认情况下，QPushButton 只能切换一次这两种状态，也就是说，当用户单击一个 QPushButton 时，它会改变自己的状态，并且会发出 clicked 信号，但是再次单击该按钮时不会再次发出 clicked 信号了。
            然而，如果您设置 QPushButton 的 checkable 属性为 True，那么这个按钮就成为了可检查按钮，也就是说，每次单击它时它都会发出一个 clicked 信号，并且每次切换自己的状态，从而使其可以多次切换选中和未选中状态。
            以复选框为例，一个复选框本质上就是一个可检查按钮，因为用户可以选择它来表示他们是否想使用某个选项。而非可检查按钮，例如普通的 push button 或 radio button，只能作为“一次性”操作执行，例如提交表单或切换到其他页面等。
            希望这样更容易理解一些。
        """
        # 可以反复切换状态的按钮
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        # .clicked[bool]是指在编程中用于检测某个控件（如按钮）是否被点击的信号。在PyQt或其他GUI框架中，当用户点击一个按钮时，该按钮会发出一个.clicked信号，该信号可以连接到一个槽函数中以实现特定的操作。[bool]表示该信号的参数是一个布尔值，
        # 即True或False，表示按钮的状态是否为被点击。
        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        # self.sender() 返回触发当前槽函数的控件对象。
        # source = self.sender() 将 sender() 方法返回的控件对象赋值给变量 source，以便在槽函数中使用。
        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
