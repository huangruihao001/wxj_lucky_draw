import random


def get_probability_from_txt(path):
    """
    获取TXT中设置的概率对应关系
    :param path:
    :return: 带概率描述的字典
    """
    # probability = {}
    f = open(path)             # 返回一个文件对象
    line = f.readline()             # 调用文件的 readline()方法
    a_list = []
    b_list = []
    while line:
        line_content = line.replace("\n", "")
        line_list = line_content.split("^")
        a_list.append(line_list[0])
        b_list.append(line_list[1])
        # print(line_list)
        # print(line, end = '')                 # 后面跟 ',' 将忽略换行符
        line = f.readline()
    # print("\n")
    # print(a_list)
    # print(b_list)
    probability = dict(zip(a_list, b_list))
    f.close()
    return probability

def num():
    """
    生成0-1之间的随机数
    :return:
    """
    return random.random()

def get_name():
    probability = get_probability_from_txt("概率设置.txt")
    # print(probability)
    this_probability = num()
    # print(this_probability)
    i = .0
    for key in probability:
        i += float(probability[key])
        if this_probability <= i:
            # print(i)
            return key


if __name__ == '__main__':
    while 1:
        print("本次抽奖结果：")
        print(get_name())
        input("按回车键继续下一次抽奖")