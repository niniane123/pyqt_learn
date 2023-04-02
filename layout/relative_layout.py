import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addWidget(okButton)
        # 这边的add很重要  里面的参数叫做弹性因子
        # 它的值越大，说明这个元素更加具有弹性，能够在布局中占据更多的空间。如果你想要设置多个伸展元素，你可以将它们的弹性系数设置为不同的值，以实现不同程度的自适应布局。

        # add的顺序也很重要 addStretch中的srecth 本身就是一个组件
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)

        # 其实可以布局里面套布局，一个布局可以排列多部件，多个部件之间又可以按照垂直或者水平的方式排列
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        vbox.addStretch(1)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
