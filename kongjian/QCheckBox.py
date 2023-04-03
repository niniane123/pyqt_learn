from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # QCheckBox 组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景。
        # cb.toggle()`函数将其初始状态改为选中
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    # 在执行时，`changeTitle`函数的第一个参数`state`将自动接收新的状态值。
    # 因此，当用户点击复选框时，程序将会自动调用`changeTitle`函数，并将新的状态值作为参数传递给它。
    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
