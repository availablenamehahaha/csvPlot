import matplotlib
import matplotlib.pyplot as plt
from main import canData, transRule, dataTrans
import re

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题


class dataPlot:
    def __init__(self, path: str):
        self.pattern = r'(\d+\.\d+)\t([0-9A-Fa-f]+)\t([0-9A-Fa-f]+)'
        self.timeList = []
        self.IDList = []
        self.dataList = []
        self.path = path
        with open(self.path, 'r', encoding='utf-8') as file:
            for line in file:
                # print(line.strip())
                match = re.search(self.pattern, line)
                if match:
                    self.timeList.append(match.group(1))
                    self.IDList.append(match.group(2))
                    self.dataList.append(match.group(3))
        print('数据导入完成')

    def lineDraw(self, rules: list):
        plt.figure()
        rule: transRule
        xMaxs = []
        yMaxs = []
        yMins = []
        for rule in rules:
            rule.dataList.clear()
            rule.timeList.clear()
            for i in range(len(self.timeList)):
                if self.IDList[i] == rule.ID:
                    data = canData(self.dataList[i]).hexStr2binStr()
                    t = float(self.timeList[i]) - float(self.timeList[0])
                    d = dataTrans(data, rule).out()
                    rule.dataList.append(d)
                    rule.timeList.append(t)
            x_data = rule.timeList
            y_data = rule.dataList
            try:
                xMaxs.append(max(x_data))
                yMaxs.append(max(y_data) * 1.1)
                yMins.append(min(y_data) * 1.1)
            except:
                print('无数据内容')
            if rule.color == "":
                plt.plot(x_data, y_data, label=rule.name)
            else:
                plt.plot(x_data, y_data, color=rule.color, label=rule.name)

        try:
            xMax = max(xMaxs)
            yMax = max(yMaxs)
            yMin = min(yMins)
            if yMax == 0:
                yMax = abs(yMin) * 0.1
            if yMin > 0:
                yMin = 0
        except:
            print('无数据内容')
            xMax = 10
            yMin = -1
            yMax = 1
        # print(f"xMax:{xMax}yMax:{yMax}yMin:{yMin}")
        plt.legend(loc='upper right')
        plt.xlim(0, xMax)
        plt.ylim(yMin, yMax)
        plt.grid(True)
        plt.show()

# rule1 = transRule("18EF1120", "温度", 48, 8, False, 1.0, -50)
# rule2 = transRule("18EF1120", "电压", 0, 16, True, 0.01, -40)
# rule3 = transRule("18EF1020", "转速", 48, 16, True, 1.0, 0)
# p = dataPlot('CanRx.txt')
# p.lineDraw([rule3])
