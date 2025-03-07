# 程序UI 界面
from helpss import Help_UI
from MainUI import Ui_MainUI
import sys
from PyQt5.QtWidgets import *
from buildGraular import BuildGrau
from rongheSelectFrame import RHSFSelect
import pandas as pd
from optFunction import opt_Graular
from optFunctionValue import opt_Graular_Value
from solveProblem import solveByAttribute
import numpy as np
from utils import showFinal, show_acc
from re1 import RESelect
from solveProblem1 import solveByAttribute1
from wt import WTSelect
import multiprocessing
import os


class DemoUi(QWidget, Ui_MainUI):
    def __init__(self):
        super(DemoUi, self).__init__()
        self.setupUi(self)
        # 上传文件 由于并没有数据库，因此上传文件我们实际上传的是文件的名称
        self.data_path = ""
        # 记录融合算法的字典信息
        self.rhSF = {
            '0': '数据融合',
            '1': '结果融合',
            '2': '特征融合'
        }
        self.downtask = {
            '0': '决策树分类器',
            '1': 'K最近邻分类器',
            '2': '自适应增强分类器',
            '3': '支持向量机分类器'
        }
        self.tag = '0'
        #  记录各个阶段的结果输出
        self.result1 = ''  # 粒结构构建阶段
        self.result2 = ''  # 粒结构优化阶段
        self.result3 = ''  # 问题求解层选择
        pass

    # todo 实现上传数据文件的功能
    def importView(self):
        #  选择文件弹窗
        filename, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "All Files (*)")
        # print(filename)
        if filename == '' or filename is None:
            return
            pass
        #  如果文件不是.svn数据格式的，这提示上传失败
        print(filename.split(".")[-1])
        if filename.split(".")[-1] != "csv":
            QMessageBox.information(self, '提示信息', '上传文件格式不正确，请上传.csv类型的文件！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
            pass
        self.data_path = filename
        #  在文本框上显示所添加的数据集的信息
        # self.textView_1.setVisible(False)
        self.textView_1.setEnabled(True)
        filename = filename.split('/')[-1][:-4]
        # print(filename)
        self.textView_1.setText(filename)
        self.textView_1.setEnabled(False)
        QMessageBox.information(self, '提示信息', '添加成功！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        self.pushView_1.setEnabled(False)
        # self.buildGranular.setEnabled(True)
        self.btnConfig.setEnabled(True)
        pass

    # todo 实现重置功能
    def resetInfo(self):
        # print(111)
        # print(self.bg.textLevelDiv.toPlainText())
        # print(111)
        # 清空数据
        self.data_path = ""
        self.textView_1.setEnabled(True)
        self.textView_1.setText("")
        self.textView_1.setEnabled(False)
        self.textView_2.setEnabled(True)
        self.textView_2.setText("")
        self.textView_2.setEnabled(False)
        self.textView_3.setEnabled(True)
        self.textView_3.setText("")
        self.textView_3.setEnabled(False)
        self.textView_4.setEnabled(True)
        self.textView_4.setText("")
        self.textView_4.setEnabled(False)
        # 将除了导入数据集以外的按钮全部变成False
        self.buildGranular.setEnabled(False)
        self.optGranular.setEnabled(False)
        self.pushProblems.setEnabled(False)
        self.pushView_1.setEnabled(True)
        # todo 其他的一些清空操作
        self.textShow_1.setText("")
        self.textShow_1.setEnabled(False)
        self.btnConfig.setEnabled(False)
        self.optGranular.setEnabled(False)
        self.textShow_2.setText("")
        self.textShow_2.setEnabled(False)
        self.textShow_3.setEnabled(True)
        self.textShow_3.setText("")
        self.textShow_3.setEnabled(False)
        self.textShow_4.setEnabled(True)
        self.textShow_4.setText("")
        self.textShow_4.setEnabled(False)
        self.tabWidget.setCurrentIndex(0)
        pass

    # todo 实现粒结构的建立
    def buildGranularW(self):
        self.tabWidget.setCurrentIndex(0)
        self.textShow_1.setEnabled(True)
        self.textShow_1.setText(self.view_index_str)
        # self.result1 = self.view_index_str
        self.optGranular.setEnabled(True)
        #  将粒结构构建的按钮设置为false
        self.buildGranular.setEnabled(False)
        # self.textShow_1.math
        pass

    # todo 粒结构优化
    def optGranularW(self):
        if self.tag == False:
            str_data, level_res = opt_Graular(self.df, self.view_atr, self.ci_list, self.res_list, self.df2)
            pass
        else:
            str_data, level_res, new_df = opt_Graular_Value(self.df, self.view_index, self.ci_list, self.res_list, self.view_atr)
            self.df = new_df
            pass
        #  显示到页面上
        self.tabWidget.setCurrentIndex(1)
        self.textShow_2.setEnabled(True)
        self.textShow_2.setText(self.result1 + str_data)
        self.result2 = str_data
        # 将问题求解按钮进行显现
        self.pushProblems.setEnabled(True)
        self.level_res = level_res
        self.optGranular.setEnabled(False)
        pass

    # todo 问题求解层 选择界面
    def resolveProblemsW(self):
        self.bg = WTSelect()
        self.bg.subWindoSignel.connect(self.resolveProblemsW1)
        self.bg.show()
        pass

    # todo 问题求解具体业务逻辑
    def resolveProblemsW1(self, id):
        self.view_len = len(self.level_res)
        if id == '1':  # 满意度粒层选择
            self.textView_3.setEnabled(True)
            self.textView_3.setText('满意度粒层')
            self.textView_3.setEnabled(False)
            self.bg.close()
            best = solveByAttribute(self.df, self.level_res)
            pass
        else: # 最优粒层选择
            self.textView_3.setEnabled(True)
            self.textView_3.setText('最优粒度层')
            self.textView_3.setEnabled(False)
            self.bg.close()
            best = solveByAttribute1(self.df, self.level_res)
            pass
        self.best = best
        tag = 1  # 默认情况下为属性拼接
        if self.tag == '1':  # 结果融合
            tag = 2
            pass
        if self.tag == '2':  # 特征融合
            tag = 3
            pass
        # str_data = showFinal(self.level_res, best, self.df, methods, tag)
        # show_acc
        str_data = showFinal(self.level_res, best, self.df, tag)
        #  将结构信息进行显示
        self.tabWidget.setCurrentIndex(2)
        self.textShow_3.setEnabled(True)
        self.textShow_3.setText(self.result2 + str_data)
        self.result3 = str_data
        pass

    #  todo  粒结构配置信息
    def configGranular(self):
        # 打开一个新的窗口
        self.bg = BuildGrau()
        # 绑定上信息传递函数
        self.bg.subWindoSignel.connect(self.slot_emit_granular)
        self.bg.show()
        # 构建粒结构, 根据文件名称来读取文件
        df = pd.read_csv(self.data_path)
        self.df = df
        # print(df)
        fn = len(df.columns) - 1  # 染色体长度
        obn = len(df)  # 数据集样本个数
        # print(fn, obn)
        df1 = df.iloc[0:obn, 0:fn]
        self.df1 = df1
        # print(df1)
        df2 = np.mat(df1)
        # print(df2)
        self.df2 = df2
        print(type(df))
        # 将条件属性划分为两个视图（对称）
        self.obn = len(df)  # 样本个数
        self.abs_len = len(df.columns) - 1  # 记录条件属性的值
        # 将判断属性系那是在第二个窗口上
        self.bg.textCount.setEnabled(True)
        self.bg.textCount.setText(str(self.abs_len))
        self.bg.textCount.setEnabled(False)
        self.bg.btnResetCi.setEnabled(False)
        # 将数据信息进行传递
        self.bg.initData(df)
        pass

    # 用来接收子窗口传递过来的信息
    def slot_emit_granular(self, result, view_index, ci_list, res_list, tag, view_atr, multi_ans):
        self.view_index_str = result
        self.view_index = view_index
        self.ci_list = ci_list
        self.res_list = res_list
        self.tag = tag
        self.buildGranular.setEnabled(True)
        self.view_atr = view_atr
        self.result1 = multi_ans
        pass

    #  todo  用来显示帮助文档
    # 用来显示帮助文档
    #  todo  用来显示帮助文档
    def helps(self):
        self.helpss = Help_UI()
        self.helpss.show()
        pass

    #  todo  融合算法的选择
    def rhSelect(self):
        #  打开融合算法选择窗口界面
        self.rh = RHSFSelect()
        self.rh.subWindoSignel.connect(self.slot_emit_rh)
        self.rh.show()
        pass

    # todo  融合结果显现
    def rhResult(self):
        # print(1111)
        self.bg = RESelect()
        self.bg.subWindoSignel.connect(self.slot_emit_re)
        self.bg.show()
        pass

    # todo 融合结果分析显示
    def slot_emit_re(self, id):
        print('从下游任务传达来的信息', id)
        methods = self.downtask[id]
        self.textView_4.setEnabled(True)
        self.textView_4.setText(methods)
        self.textView_4.setEnabled(False)
        tag = 1  # 默认情况下为属性拼接
        if self.tag == '1':  # 结果融合
            tag = 2
            pass
        if self.tag == '2':  # 特征融合
            tag = 3
            pass
        str_data =  ''
        str_data += show_acc(self.level_res, self.best, self.df, methods, tag)
        self.tabWidget.setCurrentIndex(3)
        self.textShow_4.setEnabled(True)
        self.textShow_4.setText(self.result3 + str_data)
        pass

    #  todo 融合算法选择界面向主界面返回的信息
    def slot_emit_rh(self, str):
        print('融合算法选择界面返回的信息：', self.rhSF[str])
        self.tag = str
        #  同时向主界面进行显示
        self.textView_2.setEnabled(True)
        self.textView_2.setText(self.rhSF[str])
        self.textView_2.setEnabled(False)
        pass




if __name__ == '__main__':
    #  防止在打包时出现多个界面
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    dm = DemoUi()
    dm.show()
    sys.exit(app.exec())
    pass