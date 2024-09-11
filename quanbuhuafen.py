import os
import random


def read_files(path):
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def main():
    lines = []

    # 遍历文件夹下的所有txt文件
    for file in os.listdir('E:/111/222/PEAN'):
        if file.endswith('.txt'):
            path = os.path.join('E:/111/222/PEAN', file)
            lines += read_files(path)

    # 随机打乱所有行
    random.shuffle(lines)

    # 计算测试集和训练集的行数
    total_lines = len(lines)
    test_lines = int(total_lines * 0.2)
    train_lines = total_lines - test_lines

    # 写入测试集文件
    with open('E:/111/222/PEAN/test.txt', 'w', encoding='utf-8') as f:
        for line in lines[:test_lines]:
            f.write(line)

    # 写入训练集文件
    with open('E:/111/222/PEAN/train.txt', 'w', encoding='utf-8') as f:
        for line in lines[test_lines:]:
            f.write(line)

    print(f"Total lines: {total_lines}")
    print(f"Test lines: {test_lines}")
    print(f"Train lines: {train_lines}")


if __name__ == "__main__":
    main()