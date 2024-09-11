import os
import random
import shutil

# 定义父文件夹路径
parent_folder = 'D:/partial_hand'

# 定义新文件夹路径
new_folder = 'D:/complete_no_sni_partial'

# 遍历父文件夹下的所有子文件夹
for root, dirs, files in os.walk(parent_folder):
    # 遍历子文件夹中的所有文件
    for filename in files:
        # 判断文件是否为pcap文件
        if filename.endswith('.pcap'):
            # 构建文件的完整路径
            file_path = os.path.join(root, filename)
            # 将文件复制到新文件夹中
            shutil.copy(file_path, new_folder)

# 获取新文件夹中的所有文件列表
file_list = os.listdir(new_folder)

# 将文件列表随机打乱
random.shuffle(file_list)

# 遍历打乱后的文件列表
for filename in file_list:
    # 构建文件的完整路径
    file_path = os.path.join(new_folder, filename)
    # 输出文件路径
    print(file_path)