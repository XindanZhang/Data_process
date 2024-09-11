

def find_lines_in_text(file_path, content):
    line_numbers = []
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if content in line:
                line_numbers.append(line_num)
    return line_numbers

file_path = 'E:/111/222/bigram/cnblogs.txt'
content = '003a 0009 0097 00d8 0095 00ec 00bb 0057 0017 0052 00c5 000a 00d6 0030 00a3 00b3 0031 00f7 0028 0041 0014 0022 0061 007f 00be 0071 00fb 005e 005b 00a7 0016 0047 00a3 004f 00d9 0080 00ec 00a4 00d0 0002 0091 0095 000a 0053 00dd 00e7 006c 00f7 00a9 00a5 0033 00f3 003d 00aa 00ad 0059 0059 002b 0000 0052 0060 00d9 004b 007e 0067 00ba 0066 00ef 00a7 0087 00aa 007b 00f3 0043 00da 0037 0029 004b 00a9 00b7 00b1 00e0 0017 0020 00b3 0032 0037 0064 00d6 00df 0058 00c8 0043 00c1 00a2 00c0 0093 003c 00a1 009b 0060 00e5 0078 00c8 0058 00d2'

line_numbers = find_lines_in_text(file_path, content)
print(line_numbers)