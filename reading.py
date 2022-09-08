file = input('Enter file: ')

read_file = open(file, 'r')
# r of reading, w of writing

num_words = 0
num_lines = 0

for line in read_file:
    line = line.strip('/n')  # /n separates lines
    counting = line.split(' ')  # space separates words

    num_words = num_words + len(counting)
    num_lines = num_lines + 1

read_file.close()  # close books file


print(f'The file contains {num_lines} lines and {num_words} words.')
