import os

pcap_dir = 'E:/111/alibaba.com'  # 改为你pcap文件文件夹路径
# specify output directory
output_dir = 'E:/111/333/alibaba'

for filename in os.listdir(pcap_dir):

    if filename.endswith('.pcap'):
        print(f'Processing file: {filename}')

        input_file = os.path.join(pcap_dir, filename)
        output_file = os.path.join(output_dir, filename.replace('.pcap', '.txt'))

        tshark.main([
            '-r', input_file,
            '-T', 'fields',
            '-e', 'tls.record.content',
            '-Y', 'tls.record',
            '-w', output_file
        ])

print(f'Extracted payloads saved to {output_dir} folder')