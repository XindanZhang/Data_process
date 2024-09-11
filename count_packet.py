import os
from scapy.all import PcapReader

def count_packets_in_pcap(file_path):
    count = 0
    try:
        with PcapReader(file_path) as pcap_reader:
            for _ in pcap_reader:
                count += 1
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
    return count

def count_packets_in_directory(directory):
    total_packets = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pcap'):
                file_path = os.path.join(root, file)
                packets = count_packets_in_pcap(file_path)
                print(f"{file_path}: {packets} packets")
                total_packets += packets
    return total_packets

# Replace 'your_directory_path' with the path to your folder containing PCAP files
directory_path = 'E:/111/weibo.com'
total_packets = count_packets_in_directory(directory_path)
print(f"Total packets in all PCAP files: {total_packets}")