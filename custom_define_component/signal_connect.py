from PyQt5.QtCore import QObject, Qt, pyqtSignal


# 定义一个QObject对象
class Sender(QObject):
    # 定义一个名为valueChanged的信号，信号带有一个int类型参数
    valueChanged = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def sendValue(self, value: int):
        # 当调用sendValue方法时，发射valueChanged信号，并将value作为参数传递
        self.valueChanged.emit(value)


# 定义另一个QObject对象
class Receiver(QObject):
    def __init__(self):
        super().__init__()

    # 定义一个名为updateValue的槽函数，接收一个int类型的参数
    def updateValue(self, value: int):
        print(self.sender())
        print("Received value:", value)


# 创建Sender和Receiver对象
senderObj1 = Sender()
senderObj2 = Sender()
receiverObj1 = Receiver()
receiverObj2 = Receiver()

# 将senderObj的valueChanged信号连接到receiverObj的updateValue槽函数上
senderObj1.valueChanged.connect(receiverObj1.updateValue)
senderObj2.valueChanged.connect(receiverObj2.updateValue)

# 发射valueChanged信号，这时updateValue槽函数将会被自动调用
"""
    <__main__.Sender object at 0x0000013C27EAE3A8>
    Received value: 100
    <__main__.Sender object at 0x0000013C27EAE438>
    Received value: 1000

"""
senderObj1.sendValue(100)
senderObj2.sendValue(1000)
