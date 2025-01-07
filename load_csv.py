#encoding=utf8
import sys
import os
import chardet
import pandas as pd
from PyQt5.QtCore import QThread, pyqtSignal


class LoadCsvFile(QThread):
    '''加载csv文件'''
    trigger = pyqtSignal(str)

    def __init__(self, _fileName, _finish_call=None):
        super(LoadCsvFile, self).__init__()
        self.fileName = _fileName
        self.finish_call = _finish_call
        self.df = pd.DataFrame()  # 空数据框架
        pass

    def run(self):
        print('begin to read csv')
        # 判断文件是否存在
        if not os.path.exists(self.fileName):
            print('file not exist')
            # 弹窗提示 文件不存在
            return
        # 可能需要判断文件编码 获取实际的文件编码
        self.encoding = 'utf_8_sig'
        with open(self.fileName, 'rb') as code:
            dat = code.readline()
            self.encoding = chardet.detect(dat)['encoding']
        file = open(self.fileName, encoding=self.encoding)
        lines = []
        # 先用普通一行一行读文件的方式 获取文件的总行数
        while True:
            lines_t = file.readline()
            if lines_t:
                lines.append(lines_t)
            else:
                break
        file.close()
        total = len(lines)
        self.total_lines = total
        del lines
        chunks = []
        index = 0
        # 使用pandas 加载
        encoding = 'utf_8'
        with open(self.fileName, 'rb') as f:
            data = f.read(20000)
            encoding = chardet.detect(data)['encoding']
        print(encoding)
        reader = pd.read_csv(self.fileName, encoding=encoding, iterator=True)  # pandas对象
        while True:
            try:
                chunks.append(reader.get_chunk(10000))  # 获取10000行(DataFrame格式)添加到chunks
                index += 10000
                if index >= total:
                    index = total
                #进度条保留两位小数 作为百分比
                process = str('process:') + str(round(index / total, 2))
                print(process)
                self.trigger.emit(process)
            except:
                #此处是读取完成的except
                break
        self.df = pd.concat(chunks)  # 合并chunks
        self.df = self.df.dropna(axis=0, how='any')  # 删除缺失值的行
        self.total_lines = self.df.shape[0]
        print('total lines,', self.total_lines)
        self.trigger.emit('load finish')
        del chunks
        if self.finish_call != None:
            self.finish_call()
        pass

    def GetDataFrame(self):
        """获取数据"""
        return self.df

    def GetTotalLine(self):
        """"""
        return self.total_lines
