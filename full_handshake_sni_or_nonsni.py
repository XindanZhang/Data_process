import os
import subprocess
import shutil

# Step 1: traverse all pcap files in the folder
pcap_folder = "E:/111/alibaba.com"
pcap_files = [f for f in os.listdir(pcap_folder) if f.endswith(".pcap")]

# Step 2: extract TLS handshake packets and save in a dictionary with filename as key
handshake_dict = {}
for pcap_file in pcap_files:
    print("正在处理文件:", pcap_file)
    command = ["tshark", "-r", os.path.join(pcap_folder, pcap_file), "-Y", "tls.handshake"]
    result = subprocess.run(command, capture_output=True)
    output = result.stdout.decode()
    print('output')
    print(output)
    print(len(output.strip()))
    if len(output.strip()) > 0:
        handshake_dict[pcap_file] = output.splitlines()
        print(handshake_dict)
        print(len(handshake_dict))

# Step 3: find pcap files with complete TLS handshake and save in a new folder
# complete_handshake_folder = "E:/111/tls_full_handshake"
# os.makedirs(complete_handshake_folder, exist_ok=True)
partial_handshake_folder = "E:/111/tls_handshake"
os.makedirs(partial_handshake_folder, exist_ok=True)
for pcap_file, handshake_list in handshake_dict.items():

    if len(handshake_list) in range(1, 5):
        print(len(handshake_list))
        print("找到部分TLS握手包：", pcap_file)
        src_path = os.path.join(pcap_folder, pcap_file)
        dst_path = os.path.join(partial_handshake_folder, pcap_file)
        shutil.copy(src_path, dst_path)


    # # 完整握手包提取
    # if len(handshake_list) >= 5:
    #     print("找到完整的TLS握手包：", pcap_file)
    #     src_path = os.path.join(pcap_folder, pcap_file)
    #     dst_path = os.path.join(complete_handshake_folder, pcap_file)
    #     shutil.copy(src_path, dst_path)


# Step 4: find pcap files with SNI field

sni_dict = {}
for pcap_file in os.listdir(partial_handshake_folder):
    print("正在处理文件:", pcap_file)
    command = ["tshark", "-r", os.path.join(partial_handshake_folder, pcap_file), "-Y", "tls.handshake"
                                                                                        ".extensions_server_name"]
    result = subprocess.run(command, capture_output=True)
    output = result.stdout.decode()
    if len(output.strip()) > 0:
        sni_dict[pcap_file] = True
        print("找到SNI")
    else:
        sni_dict[pcap_file] = False

'''
# 完整握手包处理
sni_dict = {}
for pcap_file in os.listdir(complete_handshake_folder):
    print("正在处理文件:", pcap_file)
    command = ["tshark", "-r", os.path.join(complete_handshake_folder, pcap_file), "-Y", "tls.handshake"
                                                                                         ".extensions_server_name"] 
    result = subprocess.run(command, capture_output=True)
    output = result.stdout.decode()
    if len(output.strip()) > 0:
        sni_dict[pcap_file] = True
    else:
        sni_dict[pcap_file] = False
'''
# Step 5: save pcap files with and without SNI field in separate folders

sni_folder = "E:/111/tls_handshake/sni/alibaba"
no_sni_folder = "E:/111/tls_handshake/no_sni/alibaba"

os.makedirs(sni_folder, exist_ok=True)
os.makedirs(no_sni_folder, exist_ok=True)

for pcap_file, has_sni in sni_dict.items():
    print("正在处理文件:", pcap_file)
    src_path = os.path.join(partial_handshake_folder, pcap_file)
    if has_sni:
        dst_path = os.path.join(sni_folder, pcap_file)
    else:
        dst_path = os.path.join(no_sni_folder, pcap_file)
    shutil.copy(src_path, dst_path)


'''
sni_folder = "E:/111/tls_handshake/sni/alibaba"
no_sni_folder = "E:/111/tls_handshake/no_sni/alibaba"
os.makedirs(sni_folder, exist_ok=True)
os.makedirs(no_sni_folder, exist_ok=True)
for pcap_file, has_sni in sni_dict.items():
    print("正在处理文件:", pcap_file)
    src_path = os.path.join(complete_handshake_folder, pcap_file)
    if has_sni:
        dst_path = os.path.join(sni_folder, pcap_file)
    else:
        dst_path = os.path.join(no_sni_folder, pcap_file)
    shutil.copy(src_path, dst_path)
'''