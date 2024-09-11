import os

# 指定要合并的文件夹路径
folder_path = "E:/FERN/111/222/pretrain"

# 指定合并后的文件名
output_file = "E:/FERN/111/222/pretrain/pretain.txt"

# 获取文件夹中所有txt文件的列表
txt_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

# 打开合并后的文件,用于写入
with open(output_file, "w") as outfile:
    # 遍历每个txt文件
    for txt_file in txt_files:
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, txt_file)

        # 打开当前txt文件,用于读取
        with open(file_path, "r") as infile:
            # 读取文件内容并写入合并后的文件
            outfile.write(infile.read())

            # 在每个文件的内容之后添加一个空行,以作分隔
            outfile.write("\n")

print("文件合并完成!")