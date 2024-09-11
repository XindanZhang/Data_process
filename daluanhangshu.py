import os
import random

def read_files(path):
    lines = []
    with open(path, 'r') as f:
        lines = f.readlines()
    print(len(lines))

    return random.sample(lines, 100)

def main():
    lines = []
    for file in os.listdir('E:/111/444'):
        if file.endswith('.txt'):
            path = os.path.join('E:/111/444', file)
            lines += read_files(path)
    
    random.shuffle(lines)
    with open('E:/111/444/output_test.txt', 'w') as f:
        for line in lines:
            f.write(line)

if __name__ == "__main__":
    main()