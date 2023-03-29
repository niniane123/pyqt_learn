import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建button text参数是想要显示的按钮名称，parent参数是放在按钮上的组件
        qbtn = QPushButton('Quit', self)
        """
            qbtn.clicked 是用于给按钮添加点击事件的方法
            connect() 是Qt框架中一个信号与槽机制的方法，它将qbtn的clicked信号连接到QCoreApplication的instance对象的quit槽上
            instance()是QCoreApplication类中的一个属性，它表示当前应用程序的实例。
        """
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
