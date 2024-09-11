import os
import glob as gl
from scapy.all import *
# 实验取facebook-0;hangouts-1;skype-2;voipbuster-3;youtube-4;netflix-5
# Define PCAP file path and output file path
# 实验取alibaba-0
pcap_dir = 'E:/111/222/weibo'
output_file_path = 'E:/111/222/pretrain/weibo.txt'

# Open the output file in write mode
with open(output_file_path, 'w') as f:

    # Traverse all PCAP files in the directory
    for i, pcap_file in enumerate(gl.glob(os.path.join(pcap_dir, '*.pcap'))):
        # Read the PCAP file
        packets = rdpcap(pcap_file)
        # Initialize lists
        payload_list = []
        lengths_list = []
        window_sizes = []  # List for window sizes

        # Iterate over each packet in the PCAP file
        for packet in packets:
            # Check if the packet has a payload
            if packet.haslayer(Raw):
                # Extract the payload
                payload = packet[Raw].load
                # Add the payload and its length to their respective lists
                payload_list.append(payload)
                lengths_list.append(len(payload))

            # Extract window size if the packet is a TCP packet, otherwise set window size to 0
            window_size = packet[TCP].window if packet.haslayer(TCP) else 0
            window_sizes.append(window_size)

        # Convert lists to strings
        payload_hex_list = [' '.join('{:02x}'.format(x) for x in payload) for payload in payload_list]
        payload_hex_str = '\t'.join(payload_hex_list)
        lengths_str = ' '.join(map(str, lengths_list))
        window_sizes_str = ' '.join(map(str, window_sizes))

        # Write the hexadecimal payload strings, their lengths, and window sizes to the file
        # f.write(f"{payload_hex_str}\t{lengths_str}\t{window_sizes_str}\n")
        # f.write(payload_hex_str + '\t' + lengths_str + '\t' + window_sizes_str + '\t9')
        f.write(payload_hex_str + '\t')
        # Add a newline character after writing the contents of one file
        if i != len(gl.glob(os.path.join(pcap_dir, '*.pcap'))) - 1:
            f.write('\n')
# Note that the newline character '\n' is added after each file's data is written,
# so each PCAP's data starts on a new line in the output file.