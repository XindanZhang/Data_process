import os
import glob as gl

# Define the input and output file paths
input_file_path = 'E:/111/222/bigram/2test.txt'
output_file_path = 'E:/111/222/bigram/pretrain.txt'

# Open the input and output files
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    # Iterate over each line in the input file
    for line in input_file:
        # Split the line into tab-separated fields
        fields = line.strip().split('\t')

        # Write the payload_hex field to the output file
        output_file.write(fields[0] + '\n')