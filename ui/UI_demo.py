import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置标题
    w.setWindowTitle("UIDEMO")

    # 展示窗口
    w.show()

    # 程序进入循环等待的状态
    app.exec_()
