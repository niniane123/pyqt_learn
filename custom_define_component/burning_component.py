from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import sys


class Communicate(QObject):
    # 自定义信号
    updateBW = pyqtSignal(int)


class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def setValue(self, value):
        self.value = value

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawWidget(self, qp):

        MAX_CAPACITY = 700
        OVER_CAPACITY = 750

        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w / 10))

        till = int(((w / OVER_CAPACITY) * self.value))
        full = int(((w / OVER_CAPACITY) * MAX_CAPACITY))

        if self.value >= MAX_CAPACITY:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till - full, h)

        else:

            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)

        pen = QPen(QColor(20, 20, 20), 1,
                   Qt.SolidLine)

        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w - 1, h - 1)

        j = 0

        for i in range(step, 10 * step, step):
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i - fw / 2, h / 2, str(self.num[j]))
            j = j + 1


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        OVER_CAPACITY = 750
        # 组件爱你初始化 信号机制的连接
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(1, OVER_CAPACITY)
        sld.setValue(75)
        sld.setGeometry(30, 40, 150, 30)

        self.c = Communicate()
        # 部件的初始化
        self.wid = BurningWidget()

        # 信号与槽的连接  这边已经制定了接受信号的对象以及信号的响应函数
        # 信号分为需要自动发出的 由qt发出 需要手动发出的：自定义信号
        sld.valueChanged[int].connect(self.changeValue)
        self.c.updateBW[int].connect(self.wid.setValue)

        # 布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Burning widget')
        self.show()


def changeValue(self, value):
    # todo  这段代码是什么意思
    # emit() 方法发出 c.updateBW 信号，该信号携带 value 参数，从而调用 self.wid.setValue() 槽函数。
    # 发送updateBW信号
    """
        当用户在 sld 滑块上移动时，将触发 sld.valueChanged[int] 信号，进而调用 changeValue() 槽函数。在 changeValue() 函数中，value 是滑块当前的值。
        然后，emit() 方法发出 c.updateBW 信号，该信号携带 value 参数，从而调用 self.wid.setValue() 槽函数。
        随后，repaint() 方法被调用以重绘 wid 组件。因此，self.wid.setValue() 槽函数会接受一个整数值，这个值用于更新 wid 组件的显示状态。
    """
    self.c.updateBW.emit(value)

    """
        在一个继承自QWidget的窗口对象self.wid中调用repaint()函数，通知系统重绘该窗口控件。
        具体来说，repaint()函数会发出一个QPaintEvent事件信号，表示该窗口控件需要重新绘制。当系统接收到该信号后，就会自动调用该窗口控件的paintEvent函数进行重绘。
        这样，就可以更新窗口控件的显示，让用户看到最新的内容
    """
    self.wid.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
