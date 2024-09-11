import os
import random

def read_files(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

def distribute_lines_equally(file_to_lines, batch_size):
    # 计算每个类别需要多少行
    num_files = len(file_to_lines)
    lines_per_file = batch_size // num_files

    # 确保每个60行的块都有来自每个类别的行
    output_lines = []
    while True:
        # 对每个文件进行操作
        for file, lines in list(file_to_lines.items()):
            # 选择lines_per_file行，或者如果不够，选择剩余的所有行
            selected_lines = lines[:lines_per_file]
            output_lines.extend(selected_lines)
            # 更新字典中剩余的行
            file_to_lines[file] = lines[lines_per_file:]
            # 如果该文件的行已经用完，从字典中移除
            if not file_to_lines[file]:
                del file_to_lines[file]
        # 如果所有文件的行都用完了，就退出循环
        if not file_to_lines:
            break
    return output_lines

def main():
    file_to_lines = {}
    output_lines = []

    # 读取所有文件并存储它们的行
    for file in os.listdir('E:/newclassified_polished_appbased/full'):
        if file.endswith('.txt'):
            path = os.path.join('E:/newclassified_polished_appbased/full', file)
            file_to_lines[file] = read_files(path)

    # 检查是否至少有12个文件
    if len(file_to_lines) < 12:
        print("There are less than 12 text files.")
        return

    # 分配行，确保每个batch都有来自每个文件的行
    output_lines = distribute_lines_equally(file_to_lines, 60)

    # 随机打乱最后的行列表
    random.shuffle(output_lines)

    # 写入最终文件
    with open('E:/newclassified_polished_appbased/full/output_test111.txt', 'w') as f:
        for line in output_lines:
            f.write(line)

if __name__ == "__main__":
    main()