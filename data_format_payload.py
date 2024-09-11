import os
import glob as gl
from scapy.all import *
# 实验取facebook-0;hangouts-1;skype-2;youtube-3;
# Define PCAP file path and output file path
pcap_dir = 'E:/111/222/weibo'
output_file_path = 'E:/111/222/PEAN/weibo.txt'

# Open the output file in write mode
with open(output_file_path, 'w') as f:
    # Traverse all PCAP files in the directory
    for i, pcap_file in enumerate(gl.glob(os.path.join(pcap_dir, '*.pcap'))):
        # Read the PCAP file
        packets = rdpcap(pcap_file)
        # Initialize lists for payloads and their lengths
        payload_list = []
        lengths_list = []
        # Iterate over each packet in the PCAP file
        for packet in packets:
            # Check if the packet has a payload
            if packet.haslayer(Raw):
                # Extract the payload
                payload = packet[Raw].load
                # Add the payload and its length to their respective lists
                payload_list.append(payload)
                lengths_list.append(len(payload))
        # Convert payloads to hexadecimal representation
        payload_hex_list = [' '.join('{:02x}'.format(x) for x in payload) for payload in payload_list]
        # Concatenate the hexadecimal strings of payloads
        payload_hex_str = '\t'.join(payload_hex_list)
        # bytes_str = '\t'.join([' '.join([b.hex()[i:i+2] for i in range(0, len(b), 2)]) for b in bytes_list])
        # Concatenate lengths into a space-separated string
        lengths_str = ' '.join(map(str, lengths_list))

        # Write the hexadecimal payload strings and their lengths to the file
        f.write(payload_hex_str + '\t' + lengths_str + '\t12')
        # f.write(bytes_str + '\t' + lengths_str + '\t0') #正常sni字段提取数据集
        # Add a newline character after writing the contents of one file, unless it's the last file
        if i != len(gl.glob(os.path.join(pcap_dir, '*.pcap'))) - 1:
            f.write('\n')