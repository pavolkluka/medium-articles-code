import sys

with open('schoolma', 'rb') as file_input:
    data_in = file_input.read()

key = bytes('MFAZRS3P8C2CYAES62G', 'utf-8')

key_len = len(key)
data_decoded = bytearray(len(data_in))

for i in range(len(data_in)):
    data_decoded[i] = data_in[i] ^ key[i % key_len]

with open('schoolma.bin', 'wb') as file_output:
    file_output.write(data_decoded)
