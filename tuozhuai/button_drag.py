from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

    # 定义一个拖拽操作 ，让拖拽框跟随鼠标移动，其实我们不是直接拖拽按钮，而是先触发一个拖拽事件，之后再响应事件的函数中去设置对话框的按钮
    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()
        # `drag.exec_(Qt.MoveAction)` 用于执行拖拽操作，它返回一个 `QDrag` 枚举类型的值
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        # ，我们传入的参数为 `Qt.MoveAction`，表示拖放操作是移动操作，当拖拽的鼠标松开时，执行拖拽操作。
        drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')


# 响应拖拽事件的对象
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    # 拖拽事件响应函数 ——释放拖拽对象的时候的响应
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        #表示对原来的对象移动
        """
            这两行代码是在Qt框架中实现拖放操作时所必需的。
            在一个典型的拖放操作中，有两个对象：源对象和目标对象。
            源对象是被拖动的对象，而目标对象是拖放操作的目的地。
            在Qt中，通常使用`QDrag`类来实现源对象，并使用`QDropEvent`类来实现目标对象，当用户将源对象拖动到目标对象时，会发生拖放操作。
            
            在这个过程中，源对象的拖动事件会被触发，同时目标对象会接收拖放事件。`setDropAction()`函数用于指定放置拖放项时的行为（例如移动或复制），而`accept()`函数用于指示目标对象接受拖放项。
            总的来说，这两行代码的作用是让目标对象接受源对象的拖放操作，并指定在放置拖放项时的行为。如果没有这两行代码，拖放操作将无法在Qt框架中正常运行。
        """
        e.setDropAction(Qt.CopyAction)
        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
