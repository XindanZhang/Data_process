import os
import random


def read_files(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    print(f'{path}: {len(lines)} lines')

    # 确保文件中至少有60行
    if len(lines) < 60:
        raise ValueError(f"The file {path} contains less than 60 lines.")

    # 随机选择60行
    return random.sample(lines, 60)


def main():
    input_dir = 'E:/newclassified_polished_appbased/full'
    output_file = 'E:/newclassified_polished_appbased/full/output_test.txt'

    # 获取所有txt文件
    files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    # 检查我们是否有4个txt文件
    if len(files) != 12:
        raise ValueError(f"Expected 12 txt files, but found {len(files)}.")

    # 从每个文件中读取60行
    file_lines_list = [read_files(os.path.join(input_dir, file)) for file in files]

    # 打乱每个文件的行，以保证随机性
    for file_lines in file_lines_list:
        random.shuffle(file_lines)

    # 组合所有文件的行，确保每24行中有每个文件的6行
    combined_lines = []
    for i in range(60):  # 确保处理所有60行
        for file_lines in file_lines_list:
            combined_lines.append(file_lines[i])

    # 打乱组合后的行列表
    random.shuffle(combined_lines)

    # 写入最终的文件
    with open(output_file, 'w') as f:
        for line in combined_lines:
            f.write(line)


if __name__ == "__main__":
    main()