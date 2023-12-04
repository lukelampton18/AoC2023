import numpy as np

input_file = open('input.txt', 'r')
inputs = input_file.read().splitlines()

omissions = ['1','2','3','4','5','6','7','8','9','0','.']
symbols = []

for line in inputs:
    for char in line:
        if char not in omissions:
            symbols.append(char)

symbols = np.unique(symbols)

