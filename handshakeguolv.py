import os
import subprocess

# 指定输入文件夹路径
input_folder = "E:/FERN/111/weibo.com"

# 指定输出文件夜路径
output_folder = "E:/FERN/111/no-handshake/weibo.com"

# 确保输出文件夹存在，如果不存在则创建
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有 pcap 文件
for filename in os.listdir(input_folder):
    if filename.endswith(".pcap"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        print(f"正在处理文件: {filename}")

        # 使用 tshark 命令过滤掉含有 handshake 信息的数据包
        # 确保你的 tshark 版本是使用 'tls.handshake' 还是 'ssl.handshake'
        command = [
            "tshark",
            "-r", input_file,
            "-Y", "!(tls.handshake or ssl.handshake)",
            "-w", output_file
        ]

        try:
            subprocess.run(command, check=True)
            print(f"文件 {filename} 处理完成")
        except subprocess.CalledProcessError as e:
            print(f"处理文件 {filename} 时出错：{e}")

print("过滤完成！")