from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ronghe import Ui_Frame_RH



class RHSFSelect(QWidget, Ui_Frame_RH):

    # 自定义传递的消息的类型，默认传递过去的是list集合
    # 第一个是视图信息，另一个是层次信息
    subWindoSignel = pyqtSignal(str)

    def __init__(self):
        super(RHSFSelect, self).__init__()
        self.setupUi(self)
        self.data_path = ''
        pass

    #  todo  确定按钮相关操作
    def ok(self):
        #  属性拼接
        if self.r1.isChecked():
            # 传递信息
            self.subWindoSignel.emit('0')
            pass
        #  结果融合
        if self.r2.isChecked():
            # 传递信息
            self.subWindoSignel.emit('1')
            pass
        # 特征融合
        if self.r3.isChecked():
            # 传递信息
            self.subWindoSignel.emit('2')
            pass
        # 关闭窗口
        self.close()
        pass

    # todo  取消按钮相关操作
    def cancel(self):
        print("关闭窗口")
        self.close()
        pass


