import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class ChildMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)  # 设置窗口类型为普通窗口，而不是主窗口类型
        self.setWindowTitle('Child MainWindow')
        self.setGeometry(200, 200, 300, 200)
        # 注意：这里通常不会给子QMainWindow添加菜单栏和工具栏，因为布局可能会混乱

        # 添加一个关闭按钮
        self.close_button = QPushButton('Close', self)
        self.close_button.setGeometry(100, 80, 100, 30)
        self.close_button.clicked.connect(self.close)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 400, 300)

        # 添加一个打开子窗口的按钮
        self.open_child_button = QPushButton('Open Child MainWindow', self)
        self.open_child_button.setGeometry(150, 120, 150, 30)
        self.open_child_button.clicked.connect(self.open_child_main_window)

        # 用于存储子窗口的引用，以便稍后能够访问它
        self.child_window = None

    def open_child_main_window(self):
        # 创建子窗口实例，并设置父窗口为当前 MainWindow 实例
        self.child_window = ChildMainWindow(self)
        self.child_window.show()
        # 隐藏主窗口
        self.hide()

        # 连接子窗口的关闭信号到主窗口的显示槽（注意：QMainWindow没有内置的关闭信号，但QDialog有）
        # 由于ChildMainWindow是QMainWindow的子类，它没有像QDialog那样的accepted()或rejected()信号
        # 因此，我们需要自己实现一个信号，或者在子窗口关闭时通过某种方式通知主窗口
        # 一种简单的方法是使用QApplication的aboutToQuit信号，但这通常用于应用程序退出时
        # 另一种方法是重写ChildMainWindow的closeEvent方法，并在其中发射一个自定义信号

        # 这里为了简化，我们使用QTimer和单次触发信号来模拟子窗口关闭后的行为
        # 这不是最佳实践，但在这个示例中足够说明问题
        from PyQt5.QtCore import QTimer, pyqtSignal

        class ChildMainWindowWithSignal(ChildMainWindow):
            closed = pyqtSignal()

            def closeEvent(self, event):
                super().closeEvent(event)
                self.closed.emit()

        # 使用带有信号的子窗口类
        if isinstance(self.child_window, ChildMainWindow):
            # 如果已经创建了不带信号的子窗口实例，则替换为带信号的实例
            # 注意：在实际应用中，你应该在open_child_main_window方法中直接创建带信号的实例
            self.child_window.close()  # 关闭旧的子窗口（如果有的话）
            del self.child_window  # 删除旧的子窗口引用
            self.child_window = ChildMainWindowWithSignal(self)  # 创建新的带信号的子窗口实例

        # 连接自定义的关闭信号到主窗口的显示方法
        self.child_window.closed.connect(self.show)

        # 显示子窗口（这行代码实际上在上面的self.child_window.show()中已经执行过了，这里只是为了说明）
        # self.child_window.show()

if __name__ == '__main__':
    import PyQt5.QtCore as QtCore
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())