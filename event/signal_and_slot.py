import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


# 设置布局  组件摆放信号槽
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        # QVBoxLayout是一种用于在垂直方向上排列小部件的布局管理器
        vbox = QVBoxLayout()
        # addWidget是QLayout类的方法，用于将一个小部件添加到布局管理器中。添加的顺序会影响到小组件再布局中的位置
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        # 当sld的值(value)发生变化时，会触发一个信号(signal)。这个信号被连接到lcd.display槽(slot)上，也就是说，当sld的值发生变化时，lcd.display方法将被自动调用。
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
