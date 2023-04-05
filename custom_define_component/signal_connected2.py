from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal
import sys


class MyWidget(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_clicked)

        self.setGeometry(300, 300, 390, 210)
        self.setWindowTitle('Testing widget')

        self.show()

    def on_button_clicked(self):
        # 发送信号并指定接收信号的对象为 self，即当前对象
        self.my_signal.emit()


# widget1 = MyWidget()
# widget2 = MyWidget()

# 将 widget1 对象的 my_signal 信号连接到 widget2 对象的 on_my_signal_received 槽函数上
# widget1.my_signal.connect(widget2.on_my_signal_received)
#
# # 在 widget2 对象上发射 my_signal 信号，并由 widget1 对象接收该信号
# widget2.my_signal.emit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())
