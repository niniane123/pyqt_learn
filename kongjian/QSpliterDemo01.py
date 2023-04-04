from PyQt5.QtWidgets import QApplication, QWidget, QSplitter, QLabel, QTextEdit, QHBoxLayout

app = QApplication([])

# 创建 QWidget 窗口，并在其中添加 QSplitter 控件
# 指定布局的父项
widget = QWidget()
layout = QHBoxLayout(widget)

splitter = QSplitter()
label = QLabel('左边的窗格')
textEdit = QTextEdit('右边的窗格')
splitter.addWidget(label)
splitter.addWidget(textEdit)
splitter.setSizes([200, 400])

# spliter作为水平布局中的子项
layout.addWidget(splitter)

widget.show()
app.exec_()
