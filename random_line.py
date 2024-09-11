import random

# 定义文件路径
pretrain_file = 'E:/FERN/111/222/pretrain/pretrain.txt'
test_file = 'E:/FERN/111/222/pretrain/pretrain_test.txt'
train_file = 'E:/FERN/111/222/pretrain/pretrain_train.txt'

# 读取 pretrain.txt 文件的所有行数据
with open(pretrain_file, 'r') as f:
    lines = f.readlines()

# 计算需要随机选取的行数
num_lines = len(lines)
num_test_lines = int(num_lines * 0.2)

# 随机选取测试数据行
test_lines = random.sample(lines, num_test_lines)

# 将测试数据写入 test.txt 文件
with open(test_file, 'w') as f:
    f.writelines(test_lines)

# 选取训练数据行
train_lines = [line for line in lines if line not in test_lines]

# 将训练数据写入 train.txt 文件
with open(train_file, 'w') as f:
    f.writelines(train_lines)

print('随机选取的测试数据行数：', num_test_lines)
print('生成的 test.txt 文件中的行数：', len(test_lines))
print('生成的 train.txt 文件中的行数：', len(train_lines))