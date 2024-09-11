import os
import glob as gl
import random
from scapy.all import *

# 设定文件夹路径和输出文件路径
pcap_dir = 'E:/newclassified_polished_appbased/full/youtube11'
output_file_path = 'E:/newclassified_polished_appbased/full/youtube11w.txt'

# 打开输出文件准备写入
with open(output_file_path, 'w') as f:
    # 获取文件夹中所有的.pcap文件
    pcap_files = gl.glob(os.path.join(pcap_dir, '*.pcap'))
    # 如果文件数量多于60，则随机选择60个文件
    if len(pcap_files) > 60:
        pcap_files = random.sample(pcap_files, 60)

    # 遍历选中的PCAP文件
    for i, pcap_file in enumerate(pcap_files):
        # 读取PCAP文件
        packets = rdpcap(pcap_file)
        # 初始化列表
        payload_list = []
        lengths_list = []
        window_sizes = []  # 窗口大小的列表

        # 遍历PCAP文件中的每个数据包
        for packet in packets:
            # 检查数据包是否有有效载荷
            if packet.haslayer(Raw):
                # 提取有效载荷
                payload = packet[Raw].load
                # 将有效载荷及其长度添加到各自的列表中
                payload_list.append(payload)
                lengths_list.append(len(payload))

            # 如果数据包是TCP数据包，提取窗口大小，否则窗口大小设置为0
            window_size = packet[TCP].window if packet.haslayer(TCP) else 0
            window_sizes.append(window_size)

        # 将列表转换成字符串
        payload_hex_list = [' '.join('{:02x}'.format(x) for x in payload) for payload in payload_list]
        payload_hex_str = '\t'.join(payload_hex_list)
        lengths_str = ' '.join(map(str, lengths_list))
        window_sizes_str = ' '.join(map(str, window_sizes))

        # 将十六进制有效载荷字符串、它们的长度和窗口大小写入文件
        f.write(payload_hex_str + '\t' + lengths_str + '\t' + window_sizes_str + '\t11')
        # 在写入一个文件的内容后添加换行符
        if i != len(pcap_files) - 1:
            f.write('\n')