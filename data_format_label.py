'''
import os
import glob as gl
from scapy.all import *
'''
# 该代码可将数据集从pcap格式转换为txt格式，一种加length sequence和label，一种为不加。
# 实验取facebook-0;hangouts-1;skype-2;voipbuster-3;youtube-4;netflix-5
'''
# Define PCAP file path and output file path
pcap_dir = 'E:/complete_handshake/sni/duodeshujuji/facebook'
output_file_path = 'E:/complete_handshake/sni/duodeshujuji/facebook.txt'

# Open the output file in write mode
with open(output_file_path, 'w') as f:
    # Traverse all PCAP files in the directory
    for i, pcap_file in enumerate(gl.glob(os.path.join(pcap_dir, '*.pcap'))):
        # Read the PCAP file
        packets = rdpcap(pcap_file)

        # Initialize byte and length lists for this PCAP file
        bytes_list = []
        lengths_list = []

        # Iterate over each packet in the PCAP file and extract the byte and length information
        for packet in packets:
            bytes_list.append(bytes(packet))
            lengths_list.append(len(packet))

        # Concatenate the byte and length information into strings with appropriate separators
        bytes_str = '\t'.join([' '.join([b.hex()[i:i+2] for i in range(0, len(b), 2)]) for b in bytes_list])
        lengths_str = ' '.join(map(str, lengths_list))

        # Write the byte, length, and label information to the output file separated by tabs
        # f.write(bytes_str + '\t') #若使用pretrain
        f.write(bytes_str + '\t' + lengths_str + '\t0') #正常sni字段提取数据集
        # Add a newline character after writing the contents of one file
        if i != len(gl.glob(os.path.join(pcap_dir, '*.pcap'))) - 1:
            f.write('\n')
'''


################################
#不包含label格式：
import os
import glob as gl
from scapy.all import *
'''
该代码可将数据集从pcap格式转换为txt格式，一种加length sequence和label，一种为不加。
实验取facebook-0;hangouts-1;skype-2;voipbuster-3;youtube-4;netflix-5
'''
# Define PCAP file path and output file path
pcap_dir = 'E:/complete_handshake/sni/duodeshujuji/netflix'
output_file_path = 'E:/complete_handshake/sni/duodeshujuji/netflix1.txt'

# Open the output file in write mode
with open(output_file_path, 'w') as f:
    # Traverse all PCAP files in the directory
    for i, pcap_file in enumerate(gl.glob(os.path.join(pcap_dir, '*.pcap'))):
        # Read the PCAP file
        packets = rdpcap(pcap_file)

        # Initialize byte and length lists for this PCAP file
        bytes_list = []
        # lengths_list = []

        # Iterate over each packet in the PCAP file and extract the byte and length information
        for packet in packets:
            bytes_list.append(bytes(packet))
            # lengths_list.append(len(packet))

        # Concatenate the byte and length information into strings with appropriate separators
        bytes_str = '\t'.join([' '.join([b.hex()[i:i+2] for i in range(0, len(b), 2)]) for b in bytes_list])
        # lengths_str = ' '.join(map(str, lengths_list))

        # Write the byte, length, and label information to the output file separated by tabs
        f.write(bytes_str + '\t') #若使用pretrain
        # f.write(bytes_str + '\t' + lengths_str + '\t0') #正常sni字段提取数据集
        # Add a newline character after writing the contents of one file
        if i != len(gl.glob(os.path.join(pcap_dir, '*.pcap'))) - 1:
            f.write('\n')
