import re
import struct

binDict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
           'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}


def is_valid_hex_string(s):
    # 正则表达式模式，匹配16个十六进制字符（0-9, a-f, A-F）
    pattern = r'^[0-9a-fA-F]{16}$'
    # 使用re.match检查字符串是否符合模式
    match = re.match(pattern, s)
    # 如果匹配成功，返回True；否则返回False
    return match is not None


class canData:
    def __init__(self, data: str):
        self.data = ""
        if len(data) > 16:
            self.data = data[-16:]
        elif len(data) < 16:
            self.data = data.zfill(16)
        else:
            self.data = data

    def hexStr2binStr(self, intel=True):
        out = ""
        if is_valid_hex_string(self.data) is None:
            return None
        for i in self.data:
            out += binDict.get(i)
        return out


class transRule:
    def __init__(self, ID, name="", begin=0, bits=16, signed=True, pu=1.0, offset=0, intel=True, color=""):
        self.ID = ID
        self.name = name
        self.begin = begin
        self.bits = bits
        self.signed = signed
        self.pu = pu
        self.offset = offset
        self.intel = intel
        self.color = color
        self.timeList = []
        self.dataList = []

    def __str__(self):
        return f'ID:{self.ID}\tName:{self.name}\tBegin:{self.begin}\tBits:{self.bits}\tSigned:{self.signed}\tPu:{self.pu}\tOffset:{self.offset}\tIntel:{self.intel}'


class dataTrans:
    def __init__(self, data: str, rule: transRule):
        self.data = data
        self.rule = rule

    def out(self):
        binTemp = self.data[self.rule.begin:self.rule.begin + self.rule.bits]
        # print(binTemp)
        dataTemp = Bin2Dec(binTemp, self.rule.signed, self.rule.intel) * self.rule.pu + self.rule.offset
        return float(dataTemp)


def Bin2Dec(binStrIn: str, signed=True, intel=True):
    # 使用 bytearray 就地构建 bytes 对象
    byte_array = bytearray()
    binStr = binStrIn
    if len(binStrIn) > 32:
        binStr = binStr.zfill(64)
        for i in range(8):
            byte_value = int(binStr[i * 8:(i + 1) * 8], 2)
            byte_array.append(byte_value)
        single_byte_object = bytes(byte_array)
        # print(single_byte_object)
        format_string = ''
        if intel:
            format_string = '<'
        else:
            format_string = '>'
        if signed:
            format_string += 'q'
        else:
            format_string += 'Q'
        signed_integer = struct.unpack(format_string, single_byte_object)[0]
    elif len(binStrIn) > 16:
        binStr = binStr.zfill(32)
        for i in range(4):
            byte_value = int(binStr[i * 8:(i + 1) * 8], 2)
            byte_array.append(byte_value)
        single_byte_object = bytes(byte_array)
        # print(single_byte_object)
        format_string = ''
        if intel:
            format_string = '<'
        else:
            format_string = '>'
        if signed:
            format_string += 'i'
        else:
            format_string += 'I'
        signed_integer = struct.unpack(format_string, single_byte_object)[0]
    elif len(binStrIn) > 8:
        binStr = binStr.zfill(16)
        for i in range(2):
            byte_value = int(binStr[i * 8:(i + 1) * 8], 2)
            byte_array.append(byte_value)
        single_byte_object = bytes(byte_array)
        # print(single_byte_object)
        format_string = ''
        if intel:
            format_string = '<'
        else:
            format_string = '>'
        if signed:
            format_string += 'h'
        else:
            format_string += 'H'
        signed_integer = struct.unpack(format_string, single_byte_object)[0]
    else:
        binStr = binStr.zfill(8)
        byte_value = int(binStr[0:8], 2)
        byte_array.append(byte_value)
        single_byte_object = bytes(byte_array)
        # print(single_byte_object)
        format_string = ''
        if intel:
            format_string = '<'
        else:
            format_string = '>'
        if signed:
            format_string += 'b'
        else:
            format_string += 'B'
        signed_integer = struct.unpack(format_string, single_byte_object)[0]
    return signed_integer


if __name__ == "main":
    pass
    # data = '471B000000004C50'
    # q = canData(data).hexStr2binStr()
    # rule = transRule("18EF1120", "电压", 0, 16, True, 0.1, 0)
    # print(dataTrans(q, rule).out())
    #
    # data = '471B000000004C50'
    # q = canData(data).hexStr2binStr()
    # rule = transRule("18EF1120", "温度", 48, 8, False, 1.0, -50)
    # print(dataTrans(q, rule).out())
