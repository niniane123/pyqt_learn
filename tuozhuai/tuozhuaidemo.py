from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)
import sys


# 把一个文本从编辑框里拖到按钮上，更新按钮上的标签（文字）。
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        # self.setDragEnabled(True)
        # 接受拖拽事件的发生  accept
        """
            这段代码是用来设置控件是否接受拖放操作的。在Qt中，只有设置了控件接受拖放操作，该控件才能被作为拖放源或目标。
            通过调用QWidget的setAcceptDrops方法并将其参数设置为True，
            可以使该控件接受拖放操作。这意味着在该控件上可以将其他控件拖放到该控件上或者将该控件上的内容拖放到其他控件上。
        """
        self.setAcceptDrops(True)

    # `dragEnterEvent`方法主要用于处理控件接收拖拽事件的情况，根据需要决定接收或忽略该事件，并进行相应的操作。

    # `dragEnterEvent` 函数在拖拽进入目标区域时被调用，用于设置目标区域的一些样式或属性，比如将目标区域高亮显示等
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

        """
        dropEvent() 处理拖拽释放事件，即当拖拽物被释放在控件区域内时被触发的事件。在这个函数中，我们可以获取拖拽物的数据并进行相应的处理。
        因此，为了能够更好地响应用户的操作，我们需要在 dragEnterEvent() 函数中设置控件的外观，提示用户可以进行拖拽操作，并在 dropEvent() 函数中获取拖拽物的数据并进行处理。这两个函数的合理配合可以实现更好的用户交互体验。
        """

    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        # 启用拖拽功能
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
