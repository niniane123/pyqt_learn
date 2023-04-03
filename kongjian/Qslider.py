from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        """
          self.label = QLabel(self) 创建了一个 QLabel 对象，并将它添加到当前窗口中（因为 self 是当前窗口对象）。
          self.label.setPixmap(QPixmap('mute.png')) 将 QPixmap 类型的图片 'mute.png' 设置为 QLabel 控件的内容。QPixmap 是 PyQt 中用于处理图像的类，它可以从文件、缓存或其他数据源中加载图像，并提供一些方法来操作和转换图像数据。
          在这里，'mute.png' 指定了要显示的图片文件名，QPixmap 会自动加载该文件并将其转换为可用于 QLabel 显示的格式。然后，setPixmap() 方法将转换后的图像数据设置为 QLabel 的内容，从而在 GUI 界面上显示出来。    
        """
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))


        '''
            这段代码设置了 QLabel 控件在 GUI 界面上的位置和大小。具体地，
            self.label 是一个 QLabel 控件对象，通过调用它的 setGeometry() 方法来设置其位置和大小。
            (160, 40) 是指定控件左上角坐标的二元组，表示该控件在窗口中的水平位置和垂直位置。这里的数值是像素单位，即 (x, y) 坐标分别为 (160, 40)。
            (80, 30) 是指定控件的大小的二元组，表示该控件在窗口中的宽度和高度。同样的，这里的数值也是像素单位，即宽度为 80 像素，高度为 30 像素。
            综上所述，self.label.setGeometry(160, 40, 80, 30) 相当于将 QLabel 控件放置在 GUI 界面上的 (160, 40) 坐标处，并将其大小设置为 80 像素宽、30 像素高。
        '''
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
