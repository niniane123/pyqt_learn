from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        # todo 这段代码是什么意思
        """
            这段代码是创建了一个 QFrame 控件（即 topleft）并将其添加到 Example 的子控件中，然后设置该控件的外观样式。
            具体来说，QFrame 是一个 Qt 控件，它可以用于呈现框架、分隔符线等简单的图形元素。在这个例子中，我们创建了一个名为 topleft 的 QFrame 子控件，并使用 setFrameShape() 方法将其外观样式设置为 QFrame.StyledPanel。
            QFrame 类定义了一些常量值，例如 QFrame.NoFrame、QFrame.Panel、QFrame.Box 等，来指定 QFrame 的外观样式。其中，QFrame.StyledPanel 表示一个带有边框的矩形面板，类似于传统的窗口部件。因此，通过调用 topleft.setFrameShape(QFrame.StyledPanel)，我们将 topleft 控件的外观设置为一个带有边框的矩形面板。
            需要注意的是，在这个例子中，我们没有为 topleft 控件设置具体的大小或位置。因此，它默认采用父控件 Example 的布局管理器（即 QHBoxLayout），并根据布局管理器的规则自动调整其大小和位置。
        """
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        # 这行代码是可以不加的
        # self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
