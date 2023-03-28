import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

"""

`super().__init__()`用于在子类的`__init__`方法中调用父类的`__init__`构造方法，以便子类对象可以获得继承自父类的初始化行为和属性。这样的话，在子类定义自己的初始化方法时，可以不必重复父类的初始化操作，避免了代码的冗余。
在Python中，当一个类有父类时，子类如果定义了自己的`__init__`方法并且希望继承父类的初始化方法，则需要调用`super().__init__()`来确保父类的初始化操作被执行。例如：

```
class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
```
在上面的代码中，类`B`继承了类`A`的`__init__`方法，并增加了自己的`b`属性。在`B`的构造方法中，通过`super().__init__(a)`的方式调用了`A`类的构造方法来执行父类的初始化操作，然后再对自己的属性进行初始化。
"""


class Example(QWidget):

    def __init__(self):
        # super().__init__()`可以确保子类继承了父类的所有属性和方法，并对其进行了初始化。
        # super._init__()先让父类自己初始化一遍，避免子类重复的初始化父类属性和方法
        # 便子类对象可以获得继承自父类的初始化行为和属性。这样的话，在子类定义自己的初始化方法时，可以不必重复父类的初始化操作，避免了代码的冗余
        super().__init__()
        self.initUI()

    def initUI(self):
        # 参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('img.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
